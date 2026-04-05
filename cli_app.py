import random
import string

# ==============================
# Fonctions
# ==============================

def generate_password():
    """Génère un mot de passe sécurisé"""

    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    symboles = "#_@!?*/"

    # Saisie longueur avec contrôle
    try:
        longueur = int(input("Entrer la longueur du mot de passe (min 12) : "))
        while longueur < 12:
            longueur = int(input("La longueur doit être au moins 12 : "))
    except:
        print("Entrée invalide.")
        return

    # Garantir chaque type
    password_list = [
        random.choice(minuscules),
        random.choice(majuscules),
        random.choice(chiffres),
        random.choice(symboles)
    ]

    all_chars = minuscules + majuscules + chiffres + symboles

    # Compléter
    while len(password_list) < longueur:
        password_list.append(random.choice(all_chars))

    random.shuffle(password_list)

    password = ''.join(password_list)

    print("Mot de passe généré :", password)


def test_password():
    """Teste la sécurité d'un mot de passe"""

    password = input("Entrer votre mot de passe : ")
    score = 0

    if len(password) >= 12:
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
        print("Mot de passe très sécurisé")
    elif score == 4:
        print("Mot de passe sécurisé")
    elif score == 3:
        print("Mot de passe moyen")
    else:
        print("Mot de passe faible")


def show_help():
    """Affiche l'aide utilisateur"""

    print("\n========== AIDE ==========")
    print("1 : Générer un mot de passe sécurisé")
    print("2 : Tester un mot de passe")
    print("3 : Quitter")
    print("==========================\n")


# ==============================
# Programme principal
# ==============================

def main():

    while True:
        print("\n======== MENU ========")
        print("1. Générer mot de passe")
        print("2. Tester mot de passe")
        print("3. Quitter")
        print("4. Aide")

        choix = input("Votre choix : ")

        if choix == "1":
            generate_password()

        elif choix == "2":
            test_password()

        elif choix == "3":
            print("Au revoir !")
            break

        elif choix == "4":
            show_help()

        else:
            print("Choix invalide")


# Lancement
if __name__ == "__main__":
    main()
        