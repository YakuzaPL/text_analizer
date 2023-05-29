from collections import Counter
import re
import string

import PyPDF2
import docx2txt


class TextAnalyzer():

    def __init__(self, file_path):
        self.file_path = file_path

    def word_count(self):
        if self.file_path.endswith('.txt'):
            with open(self.file_path, "r") as f:
                read_file = f.read()

        elif self.file_path.endswith('.docx'):
            read_file = docx2txt.process(self.file_path)

        elif self.file_path.endswith('.pdf'):
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                read_file = ""
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    read_file += page.extract_text()
        word_count = Counter(re.findall('\w+', read_file.lower()))
        return dict(word_count)

    def letter_count(self):
        if self.file_path.endswith('.txt'):
            with open(self.file_path, "r") as f:
                read_file = f.read()

        elif self.file_path.endswith('.docx'):
            read_file = docx2txt.process(self.file_path)

        elif self.file_path.endswith('.pdf'):
            with open(self.file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                read_file = ""
                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    read_file += page.extract_text()

        text = read_file.translate(str.maketrans('', '', string.whitespace + string.punctuation))
        # Converting text to lowercase
        text = text.lower()
        # Counting the frequency of each letter
        letter_count = Counter(text)
        return dict(letter_count)


test = TextAnalyzer('test_files/txt_test.txt')

print(test.word_count())