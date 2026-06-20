# Import the faiss library we just installed
import faiss
# Import numpy, which faiss uses to handle mathematical vectors
import numpy as np

# 1. Create a dummy 'database' of 10 random vectors
# Think of these as 10 different paragraphs from a PDF
dimension = 64 # The 'size' of each vector
database_vectors = np.random.random((10, dimension)).astype('float32')

# 2. Initialize the FAISS Index (The Librarian's Index Card system)
# 'IndexFlatL2' is the simplest version for beginner projects
index = faiss.IndexFlatL2(dimension)

print("---  FAISS Engine Health Check ---")

try:
    # 3. Add our 'paragraphs' to the index
    index.add(database_vectors)
    print(f" FAISS successfully indexed {index.ntotal} paragraphs.")
    
    # 4. Success message
    print(" FAISS Engine is installed and ready for Retrieval!")

except Exception as e:
    # 5. Catch any errors if installation went wrong
    print(f" FAISS Engine failure: {e}")

