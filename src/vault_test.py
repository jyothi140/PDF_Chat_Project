# Import the 'os' module to look at our computer's environment
import os

# This is a simulation of how we manually check for secrets
def check_vault():
    print("---  Secret Vault Audit ---")
    
    # Check if the .env file exists in the folder
    if os.path.exists(".env"):
        print("SUCCESS: The .env file was found in the Root folder.")
    else:
        print(" ERROR: The .env file is missing! Create it in the main project folder.")

    # In a real app, we use a library to load the key. 
    # For now, we are just confirming the vault is built.
    print("\nNote: In the next lesson, we will install the 'dotenv' tool")
    print("to automatically pull your key into the code.")

# Run the audit
if __name__ == "__main__":
    check_vault()
