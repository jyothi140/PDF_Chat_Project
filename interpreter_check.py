# Import the sys module to see where our 'engine' is located
import sys

# Get the path of the current Python executable being used
current_path = sys.executable

# Check if the word '.venv' is in the path
if ".venv" in current_path:
    # This means you successfully activated your environment!
    print("SUCCESS: You are inside your Virtual Environment!")
    print(f"Toolbox Location: {current_path}")
else:
    # This means you are still using the 'Global' Python
    print(" WARNING: You are still in the Global Environment.")
    print("Please select the Interpreter again using Ctrl+Shift+P.")

# Print a tip for the student
print("\nTip: Always check the bottom-right 'Status Bar' in VS Code!")

import sys

current_path = sys.executable

if "venv" in current_path:
    print("SUCCESS: You are inside your Virtual Environment!")
    print(f"Toolbox Location: {current_path}")
else:
    print(" WARNING: You are still in the Global Environment.")

print("\nTip: Always check the bottom-right Status Bar in VS Code!")