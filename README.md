# Password Strength Checker

##  Description

Ce projet est un outil simple de cybersécurité permettant d’analyser la robustesse d’un mot de passe.
Il a été développé dans un objectif d’apprentissage des bases de la sécurité des mots de passe et de la validation des entrées utilisateur.

Le projet existe en deux versions :
- Version Python (terminal)
- Version Web (HTML/CSS/JavaScript)

---

##  Objectifs du projet

- Comprendre les bonnes pratiques de sécurité des mots de passe
- Appliquer des règles de validation
- Utiliser les expressions régulières (Regex)
- Construire un projet structuré et professionnel

---

##  Fonctionnalités

### Version Python
- Analyse d’un mot de passe en ligne de commande
- Vérification des critères de sécurité :
  - Longueur minimale
  - Majuscules
  - Minuscules
  - Chiffres
  - Caractères spéciaux
- Score de robustesse
- Feedback détaillé

### Version Web
- Interface interactive en temps réel
- Affichage dynamique de la force du mot de passe
- Indication visuelle (faible / moyen / fort)
- Vérification instantanée à la saisie

---

## Technologies utilisées

- Python 3
- HTML5
- CSS3
- JavaScript
- Regex (module `re` en Python)

---

##  Structure du projet

password-strength-checker/
│
├── python_version/
│ └── main.py
│
├── web_version/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md


---

##  Comment exécuter le projet

###  Version Python

```bash
cd python_version
python3 main.py
