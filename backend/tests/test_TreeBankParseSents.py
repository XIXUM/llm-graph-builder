import nltk
from nltk.corpus import treebank
from nltk.tree import Tree
import random

# Ensure the necessary data is downloaded
nltk.download('treebank')


def show_sample_trees(num_sentences=3):
    """
    Display a specified number of parsed sentence trees from the Penn Treebank corpus.
    """
    parsed_sentences = treebank.parsed_sents()
    total = len(parsed_sentences)

    print(f"Total parsed sentences in corpus: {total}")
    indices = random.sample(range(total), num_sentences)

    for idx in indices:
        tree = parsed_sentences[idx]
        print(f"\nSentence {idx + 1}:")
        print(" ".join(tree.leaves()))
        print("Parse Tree:")
        tree.pretty_print()  # Graphical tree in console
        tree.draw()  # Opens a window to visually display the tree (GUI)


if __name__ == "__main__":
    show_sample_trees(num_sentences=3)
