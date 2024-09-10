import fonctions as f

while True:
    try:
        # Demander à l'utilisateur de saisir les deux nombres
        a = float(input("Nombre entier : "))
        b = float(input("Exposant entier : "))

        # Vérifier si les valeurs sont des entiers
        if not a.is_integer() or not b.is_integer():
            raise ValueError("Valeurs entières nécéssaire")

        # Convertir les valeurs en entiers
        a = int(a)
        b = int(b)

        # Calculer la puissance en utilisant la fonction
        resultat = f.puissance(a, b)

        # Afficher le résultat
        print(f"{a} puissance {b} égal à {resultat}.")
    
    except (ValueError, TypeError) as e:
        print(f"Erreur : {e}")

