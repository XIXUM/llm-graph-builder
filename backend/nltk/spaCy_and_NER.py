from typing import List

import spacy
from spacy import displacy
from spacy.tokens import Span

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a paragraph with multiple sentences
paragraph = """
Apple Inc. was founded by Steve Jobs in 1976. The company is based in Cupertino, California.
In 2021, Apple reported annual revenue of $365 billion. The iPhone is one of their most popular products.
"""
def entity_relation():
    # Process the paragraph with spaCy
    doc = nlp(paragraph)

    # Visualize the named entities using displaCy
    displacy.render(doc, style="ent", jupyter=False)

    sentence_spans: list[Span | Span] = list(doc.sents)
    # displacy.serve(sentence_spans, style="dep")

    displacy.serve(doc, style="ent")

if __name__ == "__main__":
    entity_relation()
    print("END")