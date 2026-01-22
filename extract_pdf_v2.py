import fitz  # PyMuPDF

# Open the PDF file
pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

doc = fitz.open(pdf_path)

print(f"Total pages in PDF: {len(doc)}")

# Extract text from first 30 pages to understand structure
print("\n--- Extracting text from first 30 pages ---\n")

all_text = ""
for i in range(min(30, len(doc))):
    page = doc[i]
    text = page.get_text()
    all_text += f"\n\n{'='*50}\n--- PAGE {i+1} ---\n{'='*50}\n\n{text}"

# Save to file
with open("/Users/praveenkumarh/Development/learning and teaching/extracted_sample.txt", "w") as f:
    f.write(all_text)

print("Sample extracted and saved to extracted_sample.txt")
print("\n" + all_text[:5000])

doc.close()
