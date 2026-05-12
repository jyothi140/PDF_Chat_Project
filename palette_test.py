# We are creating a simple list of common Command Palette tasks
pro_shortcuts = {
    "Ctrl+Shift+P": "Open Command Palette",
    "Ctrl+`": "Toggle Terminal",
    "Ctrl+S": "Save File"
}

# Let's print these out to see our 'Cheat Sheet'
print("--- VS Code Pro-Tips ---")

# We loop through the dictionary to display the key and the action
for shortcut, action in pro_shortcuts.items():
    # This prints the shortcut and what it does in a clean format
    print(f"To {action}, press: {shortcut}")

# A final message to encourage keyboard-only navigation
print("\nSuccess: You are learning to code like a Senior Engineer!")
