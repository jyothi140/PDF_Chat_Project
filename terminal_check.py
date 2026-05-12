# Import the 'os' module to interact with your computer's operating system
import os

# Create a variable to store a welcome message
welcome_message = "Welcome to your AI Command Center!"

# Print the welcome message to the terminal below
print(welcome_message)

# Check if our 'config.txt' file exists in the VS Code folder
if os.path.exists("config.txt"):
    # If it exists, print a success message
    print("Success: VS Code sees your project files!")
else:
    # If the file is missing, tell the user what went wrong
    print("Error: config.txt not found in this folder.")
    import os

current_contents = os.listdir('.')

print("--- Terminal Navigation Report ---")

for item in current_contents:
    if os.path.isdir(item):
        print(f"[FOLDER] Found: {item}")
    else:
        print(f"[FILE]   Found: {item}")

print(f"\nCurrently running in: {os.getcwd()}")