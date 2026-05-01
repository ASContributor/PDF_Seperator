from collections import defaultdict
import re
from pypdf import PdfReader

from services.section_builder import build_sections
from services.extractor import extract_index, extract_version
def group_sections(pdf_files):

    section_groups = defaultdict(list)

    for item in pdf_files:
        file, version, sections = item
    
        for name, start, end in sections:
            clean_name = clean_section_name(name)
            section_groups[clean_name].append({
                "file": file,
                "start": start,
                "end": end,
                "version": version
            })
    for section in section_groups:
        section_groups[section].sort(
            key=lambda x: tuple(map(int, x["version"].split(".")))
        )
    return section_groups

def clean_section_name(name):
    # remove dotted leaders like "....."
    name = re.sub(r"\.{2,}", "", name)

    # remove Roman numeral prefix (I., II., IV., etc.)
    name = re.sub(r"^[IVXLCDM]+\.\s*", "", name)

    # normalize spaces
    name = re.sub(r"\s+", " ", name)

    return name.strip()