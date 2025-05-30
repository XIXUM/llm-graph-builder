import nltk
from nltk.corpus import treebank, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tree import Tree

# Ensure required NLTK data is downloaded
nltk.download('treebank')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    """
    Convert Penn Treebank tag to WordNet POS tag
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default fallback

def lemmatize_treebank_sentence(tree: Tree):
    """
    Takes a parsed Treebank sentence, extracts (word, pos),
    and returns (original, pos, lemma) for each word.
    """
    leaves = tree.pos()  # List of (word, pos_tag) tuples from the tree
    lemmatized = [
        (word, pos, lemmatizer.lemmatize(word, get_wordnet_pos(pos)))
        for word, pos in leaves
    ]
    return lemmatized

def show_lemmatized_output(num_sentences=3):
    parsed_sents = treebank.parsed_sents()
    print(f"\nShowing lemmatized output for {num_sentences} sentences:\n")
    for i in range(num_sentences):
        print(f"--- Sentence {i + 1} ---")
        tree = parsed_sents[i]
        #tree.draw()
        tree.pretty_print()
        lemmatized = lemmatize_treebank_sentence(tree)
        for word, pos, lemma in lemmatized:
            print(f"{word:15} ({pos}) → {lemma}")
        print()

if __name__ == "__main__":
    show_lemmatized_output(num_sentences=3)
