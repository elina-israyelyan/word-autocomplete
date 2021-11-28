import pickle
import re

import numpy as np


class TrieNode:

    # Trie node class
    def __init__(self, weight=0):
        self.path_from_root = []
        self.children = [None] * 26
        self.isEndOfWord = False
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode(weight=0)

    def getNode(self, weight):

        # Returns new trie node (initialized to NULLs)
        return TrieNode(weight)

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key, heuristic):
        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node and reduces the prefixes' weights.
        key = key.lower()
        regexp = re.compile(r'[^a-z]')
        if not regexp.search(key):
            curr_node = self.root
            length = len(key)
            for level in range(length):
                index = self._charToIndex(key[level])
                # if current character is not present
                if not curr_node.children[index]:
                    curr_node.children[index] = self.getNode(heuristic + level + 1)
                    path_from_root = [*curr_node.path_from_root, chr(index + 97)]
                    curr_node.children[index].path_from_root = path_from_root
                else:
                    if curr_node.children[index].weight > 1:
                        curr_node.children[index].weight -= 1
                curr_node = curr_node.children[index]

            # mark last node as leaf
            curr_node.isEndOfWord = True

    def search(self, key):
        key = key.lower()
        curr_node = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not curr_node.children[index]:
                return False
            curr_node = curr_node.children[index]
        return curr_node.isEndOfWord

    def autocomplete(self, key):
        """
        Autocomplete the given key based on nodes in the constructed tree.
        Parameters
        ----------
        key: str
            The string to autocomplete

        Returns
        -------
        str
            the autocompleted part and if we add it to our key we will have a complete word.

        """
        # getting to initial state
        curr_node = self.root
        length = len(key)
        key = key.lower()
        for level in range(length):
            index = self._charToIndex(key[level])
            if not curr_node.children[index]:
                return False
            curr_node = curr_node.children[index]
        # starting the autocomplete
        frontier = [i for i in curr_node.children if i is not None]
        while True:
            best_child = frontier.pop(np.argmin(frontier))
            if best_child.isEndOfWord:
                return "".join(best_child.path_from_root)
            curr_node = best_child
            frontier.extend([i for i in curr_node.children if i is not None])

    def save_tree(self, save_path):
        with open(save_path, 'wb') as pickle_file:
            pickle.dump(self.root, pickle_file)

    def load_tree(self, load_path):
        with open(load_path, "rb") as file:
            self.root = pickle.load(file)
