import random
import string

def generate_password(length, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        print("Please include at least one character set.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    # Check for the presence of uppercase letters, lowercase letters, digits, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Calculate the strength based on the criteria
    strength = sum([has_upper, has_lower, has_digit, has_special])

    return strength

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return

        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, include_upper, include_lower, include_digits, include_special)
        print("Generated Password: ", password)

        strength = password_strength(password)
        print("Password Strength:", strength)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
