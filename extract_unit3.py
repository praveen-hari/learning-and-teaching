import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

# Unit 3 is from page 67 to page 87 (THEORY OF CONSTRUCTVISM AND LEARNER-CENTERED TEACHING)
# Unit 4 (MODELS OF TEACHING) starts on page 88

print("Extracting Unit 3: THEORY OF CONSTRUCTIVISM AND LEARNER-CENTERED TEACHING")
print("Converting PDF pages 67-87 to images and running OCR...")
print("This may take a few minutes...\n")

# Extract pages 67-87 for Unit 3
images = convert_from_path(pdf_path, first_page=67, last_page=87, dpi=150)

all_text = ""
for i, image in enumerate(images):
    page_num = 67 + i
    print(f"Processing page {page_num}...")
    text = pytesseract.image_to_string(image)
    all_text += f"\n\n{'='*60}\n--- PAGE {page_num} ---\n{'='*60}\n\n{text}"

# Save to file
output_path = "/Users/praveenkumarh/Development/learning and teaching/unit3_raw.txt"
with open(output_path, "w") as f:
    f.write(all_text)

print(f"\n\nOCR extraction complete! Saved to {output_path}")
print(f"Total pages extracted: {len(images)}")
print(f"Total characters: {len(all_text)}")
print("\nFirst 3000 characters:\n")
print(all_text[:3000])
