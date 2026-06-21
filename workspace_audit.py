import os # Import the system module to look at files

# 1. Define the 'Gold Standard' for a professional project
essential_files = ['app.py', 'requirements.txt', 'README.md', '.gitignore', '.env']
essential_folders = ['src', 'docs', '.venv', '.vscode']

# 2. Get a list of everything currently in your folder
current_items = os.listdir('.')

print("--- Workspace Audit Started ---")

# 3. Loop through every item to find 'Clutter'
for item in current_items:
    # Check if the item is NOT in our essential lists
    if item not in essential_files and item not in essential_folders and not item.startswith('.'):
        print(f"CLUTTER FOUND: {item}")
        print(f"Action: Move {item} to a 'trash' folder or delete it if not needed.")

# 4. Final professional check
print("\nAudit complete. Your goal: Only Essential items should remain in the Root.")