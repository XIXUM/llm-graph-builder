from nltk.corpus import wordnet

# Download WordNet data
import nltk

nltk.download('wordnet')

def test_wordnet():
    # Get word types for a word
    word = "run"
    synsets = wordnet.synsets(word)
    for synset in synsets:
        print(f"Word: {word}, Type: {synset.pos()}, Definition: {synset.definition()}")

if __name__ == "__main__":
    test_wordnet()