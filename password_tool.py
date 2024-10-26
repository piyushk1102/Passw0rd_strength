import random
import string
import math

def analyze_password(password):
    """Analyze the strength of a password."""
    strength = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one digit.")

    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Calculate entropy
    entropy = math.log2(len(password) ** len(password)) if password else 0

    return strength, entropy, feedback

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    """Generate a random password."""
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password