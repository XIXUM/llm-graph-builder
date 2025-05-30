from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

lemmatizer = WordNetLemmatizer()

# Helper to map Treebank POS tags to WordNet POS
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

def sample_lemmantize():
    # Example
    sentence = "He twisted the rope tightly and then twists it again."
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)

    lemmatized = [
        (word, lemmatizer.lemmatize(word, get_wordnet_pos(tag)))
        for word, tag in tagged
    ]

    print(lemmatized)

if __name__ == "__main__":
    sample_lemmantize()