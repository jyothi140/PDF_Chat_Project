# Import the OS module to handle file paths properly
import os
# Import the PDF Loader from LangChain's community toolkit
from langchain_community.document_loaders import PyPDFLoader

# 1. Define the path to our 'Evidence' (The PDF)
file_path = os.path.join("docs", "handshake_sample.pdf")

print(f"---  Metadata Investigation: {file_path} ---")

try:
    # 2. Initialize the Loader
    loader = PyPDFLoader(file_path)

    # 3. Load the document into memory
    # This creates a list of 'Document' objects
    pages = loader.load()

    # 4. Access the FIRST page (index 0)
    first_page = pages[0]

    # 5. Interrogate the 'Metadata' dictionary
    # Every LangChain Document has two main parts: .page_content and .metadata
    evidence_tag = first_page.metadata

    # 6. Extract specific pieces of info
    source_file = evidence_tag.get("source") # Get the file path
    page_number = evidence_tag.get("page")   # Get the page number (starts at 0)

    print(f" Evidence Found!")
    print(f" Source Location: {source_file}")
    print(f" Page Number: {page_number + 1}") # We add 1 because AI counts from 0
    
    # 7. Print the full raw dictionary to see 'Hidden' info
    # Depending on the PDF, you might see 'author', 'creator', or 'date'
    print(f"\n Full Raw Metadata:\n{evidence_tag}")

except Exception as e:
    # 8. Catch errors like missing files
    print(f" INVESTIGATION FAILED: {e}")
