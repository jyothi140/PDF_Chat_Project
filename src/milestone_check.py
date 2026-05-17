# Import the sys module to check our Python environment
import sys
# Import the os module to check our workspace folders
import os

def run_milestone_check():
    # 1. Define the colors for the terminal output
    print("\n --- MODULE 1 MILESTONE CHECK --- ")
    
    # 2. Check if we are in the Virtual Environment (.venv)
    if ".venv" in sys.executable:
        print(" ENV: Virtual Environment is ACTIVE.")
    else:
        print(" ENV: Not using .venv! Please select the correct interpreter.")

    # 3. Check if the project structure is correct
    required_folders = ['src', 'docs', 'data']
    missing = [f for f in required_folders if not os.path.exists(f)]
    
    if not missing:
        print("STRUCTURE: All project folders (src, docs, data) exist.")
    else:
        print(f"STRUCTURE: Missing folders: {missing}")

    # 4. Final 'Hello World' with a twist
    print("\n RESULT: System ready for 'Chat with your PDF' course!")
    print(f"Running on: {sys.version.split()[0]}")

# Execute the check function
if __name__ == "__main__":
    run_milestone_check()