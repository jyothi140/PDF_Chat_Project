# We are creating a list of the extensions we just installed
installed_tools = ["Python Extension", "Pylance", "VS Code Interface"]

# This function will loop through our list and print a status for each
def check_setup(tools):
    # 'for' starts a loop to look at every item in our list
    for tool in tools:
        # We use an 'f-string' to plug the tool name into a sentence
        print(f"Checking status... {tool} is ACTIVE!")

# This line actually 'calls' or runs the function we wrote above
check_setup(installed_tools)

# A final message to confirm everything is running smoothly
print("\nYour IDE is now officially 'Smart'!")
