# Import the OS module to handle file paths
import os
# Import the specialized PDF Loader from LangChain
from langchain_community.document_loaders import PyPDFLoader

# 1. Define the path to your PDF file
# We use os.path.join to make sure it works on both Windows and Mac
file_path = os.path.join("docs", "sample.pdf")

print(f"---  Loading Document: {file_path} ---")

try:
    # 2. Initialize the Librarian (The Loader)
    loader = PyPDFLoader(file_path)

    # 3. Tell the librarian to actually read the pages
    # This returns a LIST of 'Document' objects
    pages = loader.load()

    # 4. Check the results
    print(f" SUCCESS: Loaded {len(pages)} pages.")

    # 5. Look at the first page to see the 'Metadata'
    # Every page has 'page_content' (the text) and 'metadata' (the info)
    first_page = pages[0]
    print(f"\n First Page Preview (First 100 chars):")
    print(f"{first_page.page_content[:100]}...")
    
    print(f"\n Metadata Found: {first_page.metadata}")

except Exception as e:
    # 6. Catch common errors (like the file being missing)
    print(f" ERROR: Could not load PDF. {e}")
    print("Check if 'sample.pdf' is inside the 'docs' folder!")
