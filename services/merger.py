from pypdf import PdfWriter
import os
from services.version_page import create_version_page
# def merge_sections(section_groups):
#     os.makedirs("./merged", exist_ok=True)

#     for section_name, items in section_groups.items():
#         writer = PdfWriter()

#         # sort versions properly (IMPORTANT)
#         items.sort(key=lambda x: tuple(map(int, x["version"].split("."))))

#         for item in items:
#             doc = item["file"]
#             reader = doc.reader   # ✅ use existing reader

#             for p in range(item["start"], item["end"] + 1):
#                 writer.add_page(reader.pages[p - 1])  # ⚠️ 1-based → 0-based

#         safe_name = section_name.replace(" ", "_").replace(".", "")
#         output_file = f"./merged/{safe_name}.pdf"

#         with open(output_file, "wb") as f:
#             writer.write(f)

#         print(f"✅ Created: {output_file}")

from pypdf import PdfWriter, PdfReader
import os

def merge_sections(section_groups):
    os.makedirs("./merged", exist_ok=True)

    for section_name, items in section_groups.items():
        writer = PdfWriter()

        # sort versions properly
        items.sort(key=lambda x: tuple(map(int, x["version"].split("."))))

        for item in items:
            version = item["version"]

            # 🔥 add version separator page
            version_page_path = create_version_page(version)
            version_reader = PdfReader(version_page_path)
            writer.add_page(version_reader.pages[0])

            # 🔥 add actual section pages
            doc = item["file"]
            reader = doc.reader

            for p in range(item["start"], item["end"] + 1):
                writer.add_page(reader.pages[p - 1])

        safe_name = section_name.replace(" ", "_").replace(".", "")
        output_file = f"./merged/{safe_name}.pdf"

        with open(output_file, "wb") as f:
            writer.write(f)

        print(f"✅ Created: {output_file}")