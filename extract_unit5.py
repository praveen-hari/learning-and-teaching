import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# Unit 5 (TEACHING AS A PROFESSION) starts at page 116
# Need to extract until the end of the book or until the next unit/appendix

print("Extracting Unit 5: TEACHING AS A PROFESSION")
print("Converting PDF pages 116-306 to images and running OCR...")
print("This may take several minutes...\n")

# Extract pages 116 to 306 for Unit 5
images = convert_from_path(pdf_path, first_page=116, last_page=306, dpi=150)

all_text = ""
for i, image in enumerate(images):
    page_num = 116 + i
    print(f"Processing page {page_num}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {page_num} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/unit5_raw.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nOCR extraction complete! Saved to {output_path}")
print(f"Total pages extracted: {len(images)}")
print(f"Total characters: {len(all_text)}")
print("\nFirst 3000 characters:\n")
print(all_text[:3000])
