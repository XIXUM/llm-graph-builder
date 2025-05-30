from datetime import datetime

import nltk
import re
from typing import List
from Neo4jAccess import Neo4jDictionaryClient
from pathlib import Path

# Ensure NLTK sentence tokenizer is available
nltk.download('punkt')


class ContextObject:
    """
    Prototype of any Contextual Wrapper Object.
    """
    pass


class AbstractDocument(ContextObject):
    def __init__(self, file_path: Path):
        self.file_path = file_path


class TextDocument(AbstractDocument):
    """
    class that povides text document context
    """
    def __init__(self, text: str, file_path: Path):
        super().__init__(file_path)
        self.text = text


def import_text_file(file_path: Path):
    """
    Imports a text file and returns its content as a string.

    :param file_path: Path to the text file
    :return: Content of the file as a string
    """
    try:
        with open(str(file_path), 'r', encoding='utf-8') as file:
            document = TextDocument(file.read(), file_path)
# TODO: replace by logger:
        print("File imported successfully!")
        return document
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def hasChapterNum(text):
    """
    function that checks weather a string is prefixed by a chapter number that follows the rule
    of chapter numbering in a book.
    Args:
        text:

    Returns: boolean

    """
    re.compile(r"^(\d+\.)?")
    return bool(re.match(r"^(\d+\.)?", text))

class TextStructure:
    def __init__(self, document: TextDocument):
        self.document = document
        self.structure = self._parse_text()
        self.neo4j_client = Neo4jDictionaryClient()

    def _parse_text(self):
        """
        Parses the input text into a nested structure:
        [ { "caption": str, "paragraphs": [ [sentences] ] }, ... ]
        """
        sections = []
        blocks = re.split(r'\n{2,}', self.document.text.strip())

        current_caption = None
        current_section = {"caption": None, "paragraphs": []}

        for block in blocks:
            block = block.strip()
            if not block:
                continue

            # Heuristic: caption = ALL CAPS or line ends with ':' or a line by itself
            if self._is_caption(block):
                # Save previous section if it has content
                if current_section["caption"] or current_section["paragraphs"]:
                    sections.append(current_section)
                # Start new section
                current_caption = block
                current_section = {"caption": current_caption, "paragraphs": []}
            else:
                # Treat block as a paragraph
                sentences = nltk.sent_tokenize(block)
                current_section["paragraphs"].append(sentences)

        # Add the last section
        if current_section["caption"] or current_section["paragraphs"]:
            sections.append(current_section)

        return sections

    def _is_caption(self, text: str) -> bool:
        """
        Determines if a line is likely a caption based on simple rules.
        """
        lines = text.splitlines()
        if len(lines) == 1:
            return (
                text.isupper()
                or hasChapterNum(text)
                or len(text.split()) <= 5
            )
        return False

    def get_structure(self):
        return self.structure

    def print_structure(self):
        _createDocument()
        for section, i in self.structure:
            _createSection(section, i)
            print(f"\n=== Caption: {section['caption']} ===")
            for i, paragraph in enumerate(section['paragraphs'], 1):
                print(f"  Paragraph {i}:")
                for sentence in paragraph:
                    print(f"    - {sentence}")

    def _createDocument(self):
        """
        method that creates a node of label document in the graph database neo4j with a node
        Returns:
            record of the document node
        """
        queryStr = f"""
        MERGE (d:document {{name: {self.document.file_path.name}, created: {datetime.now()}}})
        RETURN d
        """

    def _createSection(self, section, i ):
        """
        method that creates a node of label section in the graph database neo4j with a node
        of label heading containing the value of the dictionary key caption
        Args:
            section:

        Returns: record of the section node

        """
        #TODO: requires to add infrastructure
        queryStr = f"""
        MATCH (d:document) WHERE d.name = {self.document.file_path.name}
        MERGE (s:section {{oder: {i}, created: {datetime.now()}}})
        MERGE (h:heading {{caption: "{section['caption']}"}})
        ON CREATE SET h.created = {datetime.now()}
        MERGE (s)-[:has_heading]->(h)
        RETURN s
        """
        result = self.neo4j_client.run_query(queryStr)
        return result

# Example usage
if __name__ == "__main__":
    sample_text = """
INTRODUCTION

This is the first paragraph. It has two sentences.
Here is the second paragraph of the introduction.

METHODS

We conducted several experiments. The data was collected from multiple sources.
Results were statistically significant.

CONCLUSION

The findings support our hypothesis.
    """
    documentPath = Path("../../experiments/ASchoolEssay.txt")
    # Example usage
    try:
        file_content = import_text_file(documentPath)
        if file_content:
            ts = TextStructure(file_content)
            ts.print_structure()
    except Exception as e:
            print(f"An error occurred: {e}")