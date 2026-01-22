import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# Unit 4 is MODELS OF TEACHING - starts on page 88
# Let's extract pages 88-120 first to find where Unit 5 begins

print("Extracting Unit 4: MODELS OF TEACHING")
print("Converting PDF pages 88-120 to images and running OCR...")
print("This may take a few minutes...\n")

# Extract pages 88-120 for Unit 4 (we'll trim later if Unit 5 starts earlier)
images = convert_from_path(pdf_path, first_page=88, last_page=120, dpi=150)

all_text = ""
for i, image in enumerate(images):
    page_num = 88 + i
    print(f"Processing page {page_num}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {page_num} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/unit4_raw.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nOCR extraction complete! Saved to {output_path}")
print(f"Total pages extracted: {len(images)}")
print(f"Total characters: {len(all_text)}")

# Check if Unit 5 marker exists in the extracted text
if "UNIT - V" in all_text or "UNIT — V" in all_text:
    print("\n*** Unit 5 marker found in extracted text - you may need to trim the file ***")
    
print("\nFirst 3000 characters:\n")
print(all_text[:3000])
