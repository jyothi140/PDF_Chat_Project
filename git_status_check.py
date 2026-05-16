# Import the 'subprocess' module to run a terminal command from Python
import subprocess

def check_git_status():
    # We try to run the 'git status' command and capture the output
    try:
        # 'check_output' runs the command 'git status'
        result = subprocess.check_output(['git', 'status'], stderr=subprocess.STDOUT).decode('utf-8')
        print("--- Git Status Report ---")
        # If successful, we print what Git says about our files
        print(result)
        print("\n SUCCESS: Git is initialized and watching your files!")
    except subprocess.CalledProcessError:
        # If Git is NOT initialized, this error will trigger
        print("--- Git Status Report ---")
        print(" ERROR: Git is not initialized in this folder.")

# Run the function
check_git_status()
