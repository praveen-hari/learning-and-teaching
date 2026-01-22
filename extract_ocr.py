import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# First, let's extract just a few pages to understand the structure
print("Converting PDF pages to images and running OCR...")
print("This may take a few minutes...\n")

# Extract first 20 pages to understand the structure and find Unit 1
images = convert_from_path(pdf_path, first_page=1, last_page=20, dpi=150)

all_text = ""
for i, image in enumerate(images):
    print(f"Processing page {i+1}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {i+1} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/ocr_sample.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nOCR extraction complete! Saved to {output_path}")
print("\nFirst 5000 characters:\n")
print(all_text[:5000])
