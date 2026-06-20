# Import 'os' to talk to the system
import os 
# Import the 'load_dotenv' function from our new library
from dotenv import load_dotenv 

# 1. Tell the guard to go to the vault (.env file) and load the keys
load_dotenv() 

# 2. Ask the guard for the specific key named 'GOOGLE_API_KEY'
# os.getenv is like saying 'Hey, give me the value of this secret'
api_key = os.getenv("GOOGLE_API_KEY")

print("---  Security Guard Report ---")

# 3. Verify if the guard successfully found the key
if api_key:
    # We show only the first 4 characters for safety
    print(f"SUCCESS: Guard found the key! Starts with: {api_key[:4]}...")
    print("Your code is now authenticated and ready for AI.")