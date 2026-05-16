# Import the subprocess module to run git commands from python
import subprocess

def get_commit_count():
    # We try to run the 'git rev-list --count HEAD' command
    try:
        # This git command returns the total number of commits made in this project
        count = subprocess.check_output(['git', 'rev-list', '--count', 'HEAD']).decode('utf-8').strip()
        # This git command gets the message of the very last commit
        last_msg = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode('utf-8').strip()
        
        print("--- Professional Git Audit ---")
        # Print the total number of snapshots saved
        print(f"Total Snapshots (Commits): {count}")
        # Print the last message we wrote in the VS Code GUI
        print(f"Latest Snapshot Message: {last_msg}")
        print("\nSUCCESS: Your work is safely recorded in the history!")
    except Exception as e:
        # If something goes wrong, print the error
        print(f" ERROR: Could not read git history. Detail: {e}")

# Run the audit function
if __name__ == "__main__":
    get_commit_count()
