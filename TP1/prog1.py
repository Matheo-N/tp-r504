print ( " Hello , World ! " )

while True:
    try:
        # Demander à l'utilisateur de saisir un nombre
        nombre = float(input("Entrez un nombre (ou appuyez sur CTRL-C pour quitter) : "))

        # Calculer le carré du nombre
        carre = nombre ** 2

        # Afficher le carré du nombre
        print(f"Le carré de {nombre} est {carre}.")
        
    except ValueError:
        print("Veuillez entrer un nombre valide.")

