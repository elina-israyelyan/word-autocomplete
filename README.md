# word-autocomplete

This package is for word autocomplete using trie trees and A* search.

## Installation

To install the library requirements for the app please make sure that you have python and pip preinstalled. To avoid
future conflicts we suggest creating a new virtual environment for this project. You can do it either with conda or
venv:

```
conda create -n 'word-autocomplette' python=3.8
```

Then activate created environment to start using it:

```
conda activate word-autocomplette
```

Then we need to install requirements.txt file, which lists all Python libraries that all python files depend on. Make
sure you are inside the project folder, open the terminal and write the following command

```
pip install -r requirements.txt
```

### What is this repository for? ###

1. Construct Trie trees based on nltk word dictionary, where nodes are the letters of words
2. Do a search by appending the letters with minimum weights and find the path to the most optimal word considering
   the path cost where each action cost is 1 and the heuristic is the `max(frequency(of all letters)) - (frequency(of the specific letter)`. 
   Here the desired optimal goal is considered the most frequent and shortest word.
3. The goal of the tree search is to reach to an end of word and the path returned by the search is the autocompleted
   word
4. Evaluate the tree search on multiple word examples.

*** Note *** \
All the above are working with lowercase letters and all the other symbols are just ignored in the processes.

### Who do I talk to if any questions ? ###

You can email to one of the contributors of this git repository: \
[Elina Israyelyan](elina_israyelyan@edu.aua.am) \
[Yeva Tshngryan](yeva_tshngryan@edu.aua.am ) \
[Dawid Arakelyan](dawid_arakelyan@@edu.aua.am)

# Getting Started

### How to run the code

At first, we need to give environmental variables `TREE_PATH` and `PYTHONPATH` to specify the tree path that should be
used and the source root for the project\
For that run the following command in the terminal:

```
export TREE_PATH='{The path to tree}'
export PYTHONPATH='word_autocomplete'
```

#### Run in Dash

After the installation of required libraries and setting the environmental variables you can run the app and test the
autocomplete [here](http://127.0.0.1:8050/) \
For this you need to run the following:

```
 python word_autocomplete/application/app.py 
```

You can type any character in the input section and press the right arrow on your keyboard to see the result of
autocomplete.

#### Construct a Tree

To construct the tree with words from `nltk corpus` and save it as pickle file, we need to run the following in the
command line:

```
python word_autocomplete tree construct_global_tree --save_path {saveing path for the tree}
```

You can also construct a tree with custom words. For this you need a .txt file where you have words on each line. When
you have the file, run the following command:

```
python word_autocomplete tree construct_tree --words_file_path {the .txt file with the words} --save_path {saveing path for the tree}
```

#### Search

To search for a specific word in the constructed tree run the following:

```
python word_autocomplete tree search_tree --word_to_search {word to be searched} --tree_path {path for the tree to be used}
```

#### Evaluate the autocomplete

To evaluate the constructed tree for the autocomplete you need a .txt file with words(or not complete word) on each
line, and then you can run the following:

```
 python word_autocomplete tree evaluate_autocomplete --test_words {the .txt file for the words to test on} --tree_path {the path to the tree}
```

After the execution of the above function you will se the autocompleted words and the average time in seconds that the
word-autocomplete needed to complete each of them In the above function you can specify the path of the tree and the
path to word examples the usage of which you can see by typing:

#### Details for each function

To see the details of options for the functions above type:

```
python word_autocomplete tree {function} --help
```

There are also example files to skip some of the processes and see the tree performance which was built
on `nltk corpus nps_chat` word list. \
You can see those example files in `example-files/` directory.
