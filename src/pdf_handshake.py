# Import the OS module to find files on our computer
import os
# Import the specialized PDF Loader tool from LangChain
from langchain_community.document_loaders import PyPDFLoader

# 1. Define exactly where our PDF 'crate' is sitting
# We use os.path.join to make sure this works on Windows and Mac
pdf_path = os.path.join("docs", "handshake_sample.pdf")

print(f"---  Initiating PDF Handshake: {pdf_path} ---")

try:
    # 2. Create the 'Loader' object (Our Librarian)
    # We give it the path so it knows which book to grab
    loader = PyPDFLoader(pdf_path)

    # 3. Tell the Librarian to 'load' the file into memory
    # This creates a list of 'Document' objects (one for each page)
    pages = loader.load()

    # 4. Count the number of items in the list (The Page Count)
    page_count = len(pages)

    # 5. The Moment of Truth: Print the results
    print(f" HANDSHAKE SUCCESSFUL!")
    print(f" Total Pages Found: {page_count}")
    
    # 6. Peek at the first page to confirm it can read text
    print(f" Content Preview: {pages[0].page_content[:50]}...")

except Exception as e:
    # 7. If the 'Handshake' fails, tell us exactly why
    print(f" HANDSHAKE FAILED: {e}")
    print(" Tip: Check if the filename in the 'docs' folder matches 'handshake_sample.pdf' exactly.")
