# security_tools.py
# A module containing reusable cybersecurity functions

import random
import string


# 1. Validate password length and character variety
def validate_password(password):
    # Check that the password has at least 10 characters
    if len(password) < 10:
        return False

    # Check for at least one letter, digit, and symbol
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    return has_letter and has_digit and has_symbol


# 2. Check the format of an IPv4 address
def validate_ip(ip):
    # An IPv4 address must contain four numbers separated by dots
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        # Each part must contain digits only
        if not part.isdigit():
            return False

        # Each number must be between 0 and 255
        number = int(part)
        if number < 0 or number > 255:
            return False

    return True


# 3. Generate a strong random password
def generate_password():
    # Choose a random password length between 10 and 16
    length = random.randint(10, 16)

    # Create groups of characters
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Select at least one character from each group
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Combine all character groups
    all_characters = uppercase + lowercase + digits + symbols

    # Fill the remaining password positions
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the characters to make their order unpredictable
    random.shuffle(password)

    # Convert the list into a string and return it
    return "".join(password)

