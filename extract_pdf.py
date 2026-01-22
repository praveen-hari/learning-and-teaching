import PyPDF2

# Open the PDF file
pdf_path = "/Users/praveenkumarh/Development/learning and teaching/LEARNING AND TEACHING(English).pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Get total number of pages
    num_pages = len(reader.pages)
    print(f"Total pages in PDF: {num_pages}")
    
    # Extract text from all pages to understand the structure
    print("\n--- Extracting text to find Unit 1 ---\n")
    
    all_text = ""
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        all_text += f"\n\n--- PAGE {i+1} ---\n\n{text}"
    
    # Save to a temporary file for inspection
    with open("/Users/praveenkumarh/Development/learning and teaching/extracted_full.txt", "w") as f:
        f.write(all_text)
    
    print("Full text extracted and saved to extracted_full.txt")
    print("\nFirst 3000 characters of extracted text:\n")
    print(all_text[:3000])
