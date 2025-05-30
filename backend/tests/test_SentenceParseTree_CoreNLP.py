import nltk
from nltk.tokenize import sent_tokenize
from nltk.parse import CoreNLPParser

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Multi-line string
text = """This is the first sentence.
Here is another sentence.
And finally, this is the last one."""

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Initialize the CoreNLP parser for Treebank parsing
parser = CoreNLPParser(url='http://localhost:9000')  # Ensure Stanford CoreNLP server is running

# Parse each sentence and display the parse tree
for sentence in sentences:
    print(f"Parsing sentence: {sentence}")
    parse_tree = next(parser.raw_parse(sentence))
    parse_tree.draw()