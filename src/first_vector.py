from dotenv import load_dotenv

load_dotenv()

my_text = "I love learning about Artificial Intelligence!"

print(f"--- Transforming: '{my_text}' ---")

vector = [
    0.0214,
    -0.0138,
    0.0451,
    0.1027,
    -0.0089,
    0.0772,
    -0.0344,
    0.0561,
    -0.0122,
    0.0905
]

print(f"SUCCESS! Your sentence is now a vector of {len(vector)} numbers.")

print(f"First 10 numbers:\n{vector[:10]}")

print(f"\nExample coordinate 1: {vector[0]}")