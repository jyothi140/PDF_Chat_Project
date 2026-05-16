# Import os to look at our folder structure
import os

# Define the folders we expect to see in a professional project
expected_folders = ["src", "docs", "data", ".venv"]

print("--- Workspace Structure Audit ---")

# Loop through our expected list and check if they exist
for folder in expected_folders:
    # check if the path exists on our computer
    if os.path.exists(folder):
        # Print a success message if found
        print(f" FOUND: {folder} folder is ready.")
    else:
        # Print a warning if a folder is missing
        print(f" MISSING: Please create the '{folder}' folder.")

# Check for the .gitignore file specifically
if os.path.exists(".gitignore"):
    print("FOUND: .gitignore is protecting your project.")
else:
    print(" MISSING: You need a .gitignore file in the root!")