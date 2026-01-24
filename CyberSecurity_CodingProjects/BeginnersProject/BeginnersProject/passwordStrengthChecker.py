import os
import re

def clear_screen():
    os.system('cls')  

def validate_password(password):
    """
    Validates a password based on multiple criteria:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 12:
        return False, "Password must be at least 12 characters long."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[^a-zA-Z0-9_\s]", password):
        return False, "Password must contain at least one special character."
    
    return True, "Password is valid."

# --- Signup ---
username = input("Username: ")
password = input("Password: ")

is_valid, message = validate_password(password)
print(f"'{password}': {message}")

if not is_valid:
    print("Signup failed. Please try again.")
    exit()

print("\n----- Signup Successful -----\n")
input("Press Enter to continue...")
clear_screen()


print("Welcome to the website\n")
print("Login")

attempts = 3
while attempts > 0:
    input_username = input("Username: ")
    input_password = input("Password: ")

    if input_username == username and input_password == password:
        print("\nLogin Successful.\n")
        break
    else:
        attempts -= 1
        print(f"Try Again. Attempts Left: {attempts}")

if attempts == 0:
    print("\nLogin Locked.\n")