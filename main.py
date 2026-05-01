from  cryptography import *

from services.extractor import extract_index, extract_version
from services.section_builder import build_sections
from services.grouper import group_sections
from services.merger import merge_sections
from utils.file_utils import load_all_pdfs

def main():
    PDF_FOLDER = "./pdf"
    documents = load_all_pdfs(PDF_FOLDER)

    all_sections = []

    for doc in documents:
        index = extract_index(doc.reader)
        # print(f"Index for {doc.name}: {index}")
        sections = build_sections(index, doc.total_pages)
        # print(f"Sections for {doc.name}: {sections}")
        version = extract_version(doc.path)
        # print(f"Version for {doc.name}: {version}")
        all_sections.append((doc,version, sections))
        # print(f"✅ Processed: {doc.name} with version: {version} and sections: {sections}")

    grouped = group_sections(all_sections)
    print(f"Grouped Sections: {grouped}") # print section names and count of versions

    merge_sections(grouped)

if __name__ == "__main__":
    main()