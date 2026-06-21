# A simple script with a hidden 'logic' error for us to hunt
def calculate_chunks(total_pages):
    # Imagine we expect 10 chunks per page
    multiplier = 10 
    result = total_pages * multiplier # Perform the math
    return result # Send the answer back

print("---  Bug-Hunting Lab Starting ---")

# 1. Set a variable for our PDF length
pages = 5 

# 2. Call our function
total_chunks = calculate_chunks(pages)

# 3. Print the result
# In a real app, this might be where we see a weird number
print(f"Total chunks created: {total_chunks}")

print("---  Lab Complete ---")