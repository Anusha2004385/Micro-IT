import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password with specified criteria."""
    characters = string.ascii_lowercase  # Start with lowercase letters

    # Include uppercase letters if requested
    if use_uppercase:
        characters += string.ascii_uppercase

    # Include numbers if requested
    if use_numbers:
        characters += string.digits

    # Include special characters if requested
    if use_special_chars:
        characters += string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    """Get user input for the password generation criteria."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:
                print("Password length should be at least 6 characters for security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for the length.")

    # Ask the user about including different character types
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_numbers, use_special_chars

def main():
    print("Welcome to the Password Generator!")
    
    # Get the user input for password criteria
    length, use_uppercase, use_numbers, use_special_chars = get_user_input()

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    # Display the generated password
    print(f"Your generated password is: {password}")

# Run the password generator program
if __name__ == "__main__":
    main()
