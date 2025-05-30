import nltk
from nltk.tokenize import sent_tokenize
from nltk.parse import ChartParser
from nltk.grammar import CFG

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

# Multi-line string
raw_text = """This is the first sentence.
Here is another sentence.
And finally, this is the last one."""

def gen_tree(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Define a simple grammar for parsing
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> DT NN | DT NNS | PRP
        VP -> VBZ NP | VBP NP | VB NP | VB PP
        PP -> IN NP
        DT -> 'the' | 'this' | 'another'
        NN -> 'sentence'
        NNS -> 'sentences'
        PRP -> 'I' | 'Here'
        VBZ -> 'is'
        VBP -> 'are'
        VB -> 'run'
        IN -> 'in' | 'on'
    """)

    # Initialize the Treebank parser
    parser = ChartParser(grammar)

    # Parse each sentence and display the parse tree
    for sentence in sentences:
        print(f"Parsing sentence: {sentence}")
        # Tokenize the sentence into words
        words = nltk.word_tokenize(sentence.lower())
        try:
            # Generate the parse tree
            parse_tree = next(parser.parse(words))
            parse_tree.draw()
        except StopIteration:
            print(f"Could not parse the sentence: {sentence}")

if __name__ == "__main__":
    gen_tree(raw_text)