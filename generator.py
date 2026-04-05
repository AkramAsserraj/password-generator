import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    """Génère un mot de passe sécurisé"""

    characters = ""
    password = []

    if include_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if include_lowercase:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if include_digits:
        characters += string.digits
        password.append(random.choice(string.digits))

    if include_special:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)

    return ''.join(password)
