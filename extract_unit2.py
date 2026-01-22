import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# Unit 2 starts around page 63 (after Unit 1 ends)
# Based on content structure, Unit 2 likely ends around page 115-120
# Let's extract pages 63 to 120 to capture the full Unit 2
print("Extracting Unit 2 (pages 63-120) from PDF...")
print("This may take several minutes...\n")

images = convert_from_path(pdf_path, first_page=63, last_page=120, dpi=150)

all_text = ""
for i, image in enumerate(images):
    page_num = i + 63
    print(f"Processing page {page_num}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {page_num} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/unit2_raw.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nUnit 2 OCR extraction complete! Saved to {output_path}")
print(f"Total characters extracted: {len(all_text)}")
