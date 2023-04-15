from modules import GUI


def nom():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='DEBUT DE PARTIE')

        nom_joueur = input("Entrez votre nom ou pseudonyme s'il vous plaît : ")
        if 10 > len(nom_joueur) > 0 and " " not in nom_joueur:  # si le nom est bon, on sort de la boucle
            return nom_joueur
        else:  # si le nom n'est pas bon, on passe à la prochaine itération
            print("Vous devez mettre un bon nom")


def mise_maximale():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='DEBUT DE PARTIE')

        try:  # on essaie de convertir la mise en entier
            mise_max = int(input("Fixez vous une limite de mise :"))
            if mise_max > 0:
                return mise_max
        except:  # si la mise n'est pas un entier, on passe à la prochaine itération
            print("Veuillez mettre un nombre supérieur a 0")
            pass
