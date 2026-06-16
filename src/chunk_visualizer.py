# Import the recursive splitter we learned in Topic 7
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Import sys to check if we can print colors in your specific terminal
import sys

# 1. Define 'ANSI' color codes for the terminal (Manual method)
# This allows us to print green and blue text without extra libraries
GREEN = '\033[92m'
BLUE = '\033[94m'
ENDC = '\033[0m' # This 'resets' the color back to white

# 2. A sample dataset about Space to visualize
long_text = """
The Moon is Earth's only natural satellite. It is about one-quarter the size of Earth. 
The first human landing was in 1969.

Mars is known as the Red Planet. It has the largest volcano in the solar system.
Scientists are looking for signs of ancient water.
"""

# 3. Initialize our 'Smart Chef' (Recursive Splitter)
# We set a small chunk size so we get multiple 'slices' to see
splitter = RecursiveCharacterTextSplitter(
    chunk_size=60,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)

# 4. Perform the split
chunks = splitter.split_text(long_text)

print(f"---  Visualizing {len(chunks)} Data Slices ---")

# 5. Loop through each chunk and print with color separators
for i, chunk in enumerate(chunks):
    # Print a bright Green separator line
    print(f"{GREEN}{'='*30} CHUNK {i+1} {'='*30}{ENDC}")
    
    # Print the actual text in Blue to make it stand out
    print(f"{BLUE}{chunk}{ENDC}")
    
# 6. Print a final closing line
print(f"{GREEN}{'='*70}{ENDC}")

print("\n DEBUG TIP: Check the end of each chunk to see the 'Overlap' in action!")
