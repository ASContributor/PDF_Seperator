import os
from pypdf import PdfReader
from models.document import Document

def load_all_pdfs(folder):
    documents = []

    for filename in sorted(os.listdir(folder)):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder, filename)

            try:
                doc = Document(path)
                documents.append(doc)

                print(f"✅ Loaded: {doc.name} ({doc.total_pages} pages📃) rendered: {doc.reader} path: {doc.path}")

            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")

    return documents