from datetime import datetime

import nltk
import re
from typing import List
from neomodel import StructuredNode, StringProperty, IntegerProperty
from Neo4jAccess import Neo4jDatabaseClient
from pathlib import Path
import inspect

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

def creationStamp() -> str:
    return f"created: {apoc_timestamp()}, createdby: '{get_frame_by_index(2)}'"

def set_creationStamp(node : str) -> str:
    return f"h.created = '{apoc_timestamp()}', h.createdby = '{get_frame_by_index(2)}'"

def apoc_timestamp() -> str:
    return f"apoc.date.toISO8601(datetime().epochMillis, \"ms\")"

def get_current_method_name():
    """
    Returns the name of the current method or function.
    """
    return inspect.currentframe().f_back.f_code.co_name

def get_frame_by_index(index):
    """
    Retrieves the method or function name at a specific index in the call stack.

    :param index: The number of frames to look back (0 = current frame).
    :return: Name of the method or function at the specified frame, or None if out of range.
    """
    frame = inspect.currentframe()
    try:
        # Navigate back "index" frames in the call stack
        for _ in range(index):
            if frame is None:
                return None  # If we run out of frames, return None
            frame = frame.f_back
        return frame.f_code.co_name if frame else None
    finally:
        # Avoid reference cycles by explicitly deleting the current frame (best practice)
        del frame

class TextStructure:
    def __init__(self, document: TextDocument):
        self.document = document
        self.structure = self._parse_text()
        self.neo4j_context_client = Neo4jDatabaseClient(database="context", password="test1234")

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
        self._createDocument()
        for sec, section in enumerate(self.structure):
            self._createSection(section, sec)
            print(f"\n=== Caption: {section['caption']} ===")
            for p, paragraph in enumerate(section['paragraphs'], 1):
                self._createParagraphs(paragraph, p, sec)
                print(f"  Paragraph {p}:")
                for ss, sentence in paragraph:
                    self._createSentence(sentence, ss, p)
                    print(f"    - {sentence}")

    def _createDocument(self):
        """
        method that creates a node of label document in the graph database neo4j with a node
        Returns:
            record of the document node
        """
        #TODO: 05.06.2025 requires to add infrastructure for context
        vars = ["d"]
        queryStr = f"""
        MERGE (d:document {{name: \"{self.document.file_path.name}\", {creationStamp()}}})
        RETURN {", ".join(vars)}
        """
        result = self.neo4j_context_client.run_query(queryStr)
        return result

    def _createSection(self, section, i ):
        """
        method that creates a node of label section in the graph database neo4j with a node
        of label heading containing the value of the dictionary key caption
        Args:
            section:

        Returns: record of the section node

        """
        vars = ["d", "s", "h"]
        queryStr = f"""
        MATCH (d:document) WHERE d.name = '{self.document.file_path.name}'
        """
        if i > 0:
            vars.append("pr")
            queryStr += f"""
            MATCH (d)-[:has_section]->(pr) WHERE pr.order = {i-1}
            """
        queryStr += f"""
        MERGE (s:section {{order: {i}, {creationStamp()}}})
        MERGE (h:heading {{caption: "{section['caption']}"}})
        ON CREATE SET {set_creationStamp('h')}
        MERGE (s)-[:has_heading]->(h)
        MERGE (d)-[:has_section]->(s)
        """
        if i > 0:
            queryStr += f"""
            MERGE (pr)-[:successor]->(s)
            """
        queryStr += f"""
        RETURN {", ".join(vars)}
        """
        result = self.neo4j_context_client.run_query(queryStr)
        return result

    def _createParagraphs(self, paragraph, para_num, sec_num):
        """
        method that creates a paragraph node of label paragraph in the graph database neo4j
        Args:
            paragraph:
            i:

        Returns:

        """
        vars = ["s", "p"]
        queryStr = f"""
        MATCH (s:section) WHERE s.order = {sec_num}
        """
        if para_num > 0:
            vars.append("op")
            queryStr +=f"""
            MATCH (s)-[:has_paragraph]->(op) WHERE op.order = {para_num-1}
            """
        queryStr +=f"""
        MERGE (p:paragraph {{order: {para_num}, {creationStamp()}}})
        MERGE (s)-[:has_paragraph]->(p)
        """
        if para_num > 0:
            queryStr+= f"""
            MERGE (op)-[:successor]->(p)
            """
        queryStr +=f"""
        RETURN {", ".join(vars)}
        """
        result = self.neo4j_context_client.run_query(queryStr)
        return result

    def _createSentence(self, sentence, sent_num, para_num):
        """
        creates the sentence representation
        Args:
            sentence:
            para_num:
            sent_num:

        Returns:

        """

        vars = ["p", "ss"]
        queryStr = f"""
        MATCH (p:paragraph) WHERE p.order = {para_num}
        """
        if sent_num > 0:
            vars.append("pr")
            queryStr += f"""
            MATCH (p)-[:has_sentence]->(pr) WHERE pr.order = {sent_num - 1}
            """
        queryStr += f"""
        MERGE (ss:sentence {{order: {sent_num}, content: \"{sentence}\", {creationStamp()}}})
        MERGE (p)-[:has_sentence]->(ss)
        """
        if sent_num > 0:
            queryStr += f"""
            MERGE (pr)-[:successor]->(ss)
            """
        queryStr += f"""
        RETURN {", ".join(vars)}
        """
        result = self.neo4j_context_client.run_query(queryStr)
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