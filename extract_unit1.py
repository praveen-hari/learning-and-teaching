import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# Unit 1 starts around page 9 and ends around page 62 (Unit 2 starts at page 63)
# Adding a few pages buffer
print("Extracting Unit 1 (pages 9-65) from PDF...")
print("This may take several minutes...\n")

images = convert_from_path(pdf_path, first_page=9, last_page=65, dpi=150)

all_text = ""
for i, image in enumerate(images):
    page_num = i + 9
    print(f"Processing page {page_num}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {page_num} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/unit1_raw.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nUnit 1 OCR extraction complete! Saved to {output_path}")
print(f"Total characters extracted: {len(all_text)}")
