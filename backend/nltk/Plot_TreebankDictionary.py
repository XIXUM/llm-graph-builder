import nltk
import re
from typing import List

# Ensure NLTK sentence tokenizer is available
nltk.download('punkt')


def import_text_file(file_path):
    """
    Imports a text file and returns its content as a string.

    :param file_path: Path to the text file
    :return: Content of the file as a string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("File imported successfully!")
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for accessing the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class TextStructure:
    def __init__(self, text: str):
        self.text = text
        self.structure = self._parse_text()

    def _parse_text(self):
        """
        Parses the input text into a nested structure:
        [ { "caption": str, "paragraphs": [ [sentences] ] }, ... ]
        """
        sections = []
        blocks = re.split(r'\n{2,}', self.text.strip())

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
                or text.endswith(':')
                or len(text.split()) <= 5
            )
        return False

    def get_structure(self):
        return self.structure

    def print_structure(self):
        for section in self.structure:
            print(f"\n=== Caption: {section['caption']} ===")
            for i, paragraph in enumerate(section['paragraphs'], 1):
                print(f"  Paragraph {i}:")
                for sentence in paragraph:
                    print(f"    - {sentence}")

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

# # Example usage
# file_content = import_text_file("example.txt")
# if file_content:
#     print("File Content:", file_content)

    ts = TextStructure(sample_text)
    ts.print_structure()