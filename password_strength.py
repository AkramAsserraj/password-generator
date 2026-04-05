import string

def check_password_strength(password):
    """Évalue la force d’un mot de passe"""

    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        return "Mot de passe très sécurisé"
    elif score == 4:
        return "Mot de passe sécurisé"
    elif score == 3:
        return "Mot de passe moyen"
    else:
        return "Mot de passe faible"
    