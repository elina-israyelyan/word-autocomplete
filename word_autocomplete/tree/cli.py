import datetime
import os
import time

import click
import numpy as np
from nltk.corpus import nps_chat

from tree.trie_tree import *
from utils.word_processing import get_heuristics


@click.group("tree")
def commands():
    """
    Package's starting point, responsible for tree creation.
    """
    pass


@commands.command("construct_tree", help="Transform the given words to Trie data structure")
@click.option("--words_file_path", type=str, default=None,
              help="Path to get the words for the tree construction. "
                   "The path should be for a .txt file and have the words on each line separately")
@click.option("--save_path", type=str, default="./",
              help="Directory to save the tree to")
def construct_tree(words_file_path, save_path):
    try:
        if os.path.exists(words_file_path):

            words = []
            with open(words_file_path, 'r') as data_file:
                for line in data_file:
                    words.extend(line.split())
            heuristics_dict = get_heuristics(words)
            t = Trie()
            for k, v in heuristics_dict.items():
                t.insert(k, v)

            print("Tree is constructed")
            t.save_tree(save_path + "tree_latest.p")
            t.save_tree(save_path + f"tree_{datetime.datetime.now()}.p")

        else:
            raise Exception("The file doesnt exist")
    except Exception as e:
        print(f"error: {e}")


@commands.command("search_tree", help="Search the inputted word in the tree.")
@click.option("--word_to_search", type=str, default=None,
              help="A single word to search in the tree.")
@click.option("--tree_path", type=str, default=".",
              help="Path to save the tree.")
def search_tree(word_to_search, tree_path):
    t = Trie()
    t.load_tree(tree_path)
    if t.search(word_to_search):
        print(word_to_search + " is in the tree")
    else:
        print(word_to_search + " is not in the tree")


@commands.command("construct_global_tree",
                  help="Transform the words from nltk corpus of nps_chat to Trie data structure and save it.")
@click.option("--save_path", type=str, default="./",
              help="Directory to save the tree to.")
def construct_global_tree(save_path):
    try:
        words_list = [i.lower() for i in nps_chat.words() if len(i) >= 2]
    except:
        import nltk
        nltk.download('nps_chat')
        words_list = [i.lower() for i in nps_chat.words() if len(i) >= 2]

    heuristics_dict = get_heuristics(words_list)

    t = Trie()
    for k, v in heuristics_dict.items():
        t.insert(k, v)
    t.save_tree(save_path + "tree_latest.p")
    t.save_tree(save_path + f"tree_{datetime.datetime.now()}.p")


@commands.command("evaluate_autocomplete", help="Autocomplete given words and evaluate the algorithm on it.")
@click.option("--test_words", type=str, default="./example-files/words_example.txt",
              help="Path to get the words for the tree testing."
                   "The path should be for a .txt file and have the words on each line separately. ")
@click.option("--tree_path", type=str, default="./example-files/tree_latest.p",
              help="Path to the pickle file that contains the tree.")
def evaluate_autocomplete(test_words, tree_path):
    if os.path.exists(test_words):
        words = []
        with open(test_words, 'r') as data_file:
            for line in data_file:
                words.extend(line.split())
    t = Trie()
    t.load_tree(tree_path)
    results = []
    for word in words:
        start = time.time()
        try:
            print(t.autocomplete(word) + "")
        except Exception as e:
            pass
        results.append(time.time() - start)
    print(np.mean(results))
