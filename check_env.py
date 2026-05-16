# Import the 'sys' module to check which Python version we are using
import sys
# Import 'os' to check for folder existence
import os

# Check if the .venv folder exists in our current directory
venv_exists = os.path.isdir(".venv")

print("--- Virtual Environment Check ---")

# Let the user know if the environment was successfully created
if venv_exists:
    print("Status: SUCCESS! The '.venv' folder is present.")
else:
    print("Status: FAILED. No '.venv' folder found.")

# Show the path of the Python 'engine' currently running this script
print(f"Current Python Path: {sys.executable}")
