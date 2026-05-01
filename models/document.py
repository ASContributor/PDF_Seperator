import os

from pypdf import PdfReader


class Document:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.reader = PdfReader(path)
        self.total_pages = len(self.reader.pages)