import re
from unittest import result
from config import INDEX_SEARCH_PAGES, VERSION_PATTERN


def extract_version(filename):
     
    
    match = re.search(VERSION_PATTERN, filename)
    if match:
        return match.group(1)
    return None




import re

def extract_index(reader):
    index = []

    for i in range(INDEX_SEARCH_PAGES):
        text = reader.pages[i].extract_text()

        if not text:
            continue

        if "Table of Contents" in text:
            lines = text.split("\n")

            for line in lines:
                line = line.strip()

                # skip garbage
                if not line or "copyright" in line.lower():
                    continue

                # normalize dots → spaces
                line = re.sub(r"\.{2,}", " ", line)

                # collapse spaces
                line = re.sub(r"\s+", " ", line)

                # now match
                match = re.search(r"^(.*?)(\d+)$", line)

                if match:
                    name = match.group(1).strip()
                    page = int(match.group(2))
                    index.append((name, page))

    return index