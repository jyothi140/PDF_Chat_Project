# Import the subprocess module to talk to Git
import subprocess

def check_visibility():
    print("--- Git Invisibility Test ---")
    
    # This command asks Git to list every file it is currently tracking
    # We use 'git ls-files' which is like Git's 'packing list'
    try:
        packing_list = subprocess.check_output(['git', 'ls-files']).decode('utf-8')
        
        # We check if '.env' appears in that list
        if ".env" in packing_list:
            print("DANGER: Your .env file is VISIBLE to Git!")
            print("Action: Remove it from Git immediately using the terminal.")
        else:
            print("SAFE: Your .env file is invisible to Git.")
            print("You can now safely share your code without leaking keys.")
            
    except Exception as e:
        print(f"Error checking Git: {e}")

# Run the test
if __name__ == "__main__":
    check_visibility()
