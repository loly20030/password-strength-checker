import re

def check_password(password):
    score = 0
    feedback = []

    # Critères de sécurité
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Au moins 8 caractères")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Ajouter une majuscule")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Ajouter une minuscule")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Ajouter un chiffre")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Ajouter un symbole spécial")

    # Résultat
    print("\n--- Analyse du mot de passe ---")

    if score <= 2:
        print("🔴 Mot de passe FAIBLE")
    elif score <= 4:
        print("🟠 Mot de passe MOYEN")
    else:
        print("🟢 Mot de passe FORT")

    # Afficher les améliorations
    if feedback:
        print("\nAméliorations recommandées :")
        for f in feedback:
            print(f)

# Programme principal
if __name__ == "__main__":
    password = input("Entrez un mot de passe : ")
    check_password(password)