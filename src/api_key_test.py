# Create a variable to hold your key (We will replace this 'placeholder' later)
# For now, just paste your key between the quotes to see if Python can hold it
my_secret_key ="YOUR_FULL_REAL_KEY" 

# We create a function to check if the key 'looks' valid
def check_key_format(key):
    # Check if the key is still the placeholder text
    if key == "PASTE_YOUR_KEY_HERE":
        print("ERROR: You haven't pasted your actual key yet!")
    # Check if the key is too short (most keys are at least 30 characters)
    elif len(key) < 20:
        print(" WARNING: That key looks a bit too short to be real.")
    else:
        # If it passes, we hide most of it for safety
        hidden_key = key[:4] + "...." + key[-4:]
        print(f" SUCCESS: Key detected! (Formatted as: {hidden_key})")
        print("Your Python script is now ready to talk to the AI.")

# Run the check
if __name__ == "__main__":
    check_key_format(my_secret_key)
