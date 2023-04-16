from modules import GUI


def nom():
    """Demande le nom du joueur, et vérifie qu'il est correct"""
    while True:
        GUI.clear_screen()
        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION')

        nom_joueur = input("Comment tu t'appelles ?\n")
        if 10 > len(nom_joueur) > 0 and " " not in nom_joueur:  # si le nom est bon, on sort de la boucle
            return nom_joueur
        else:  # si le nom n'est pas bon, on passe à la prochaine itération
            print("C'est quoi ce nom ?!")
            print("Bon, sérieusement, un nom/pseudo, sans espace, pas trop long, s'il te plait.")
            input("Appuie sur Entrée...")
            pass


def mise_maximale(nom_joueur):
    """:return: mise_max, la mise maximale que le joueur peut parier
    :rtype: float
    """
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION')

        try:  # on essaie de convertir la mise en entier
            mise_max = float(input("Fixe toi une limite de mise :\n"))
            if mise_max > 0 and not len(str(mise_max).split('.')[1]) > 2:
                return mise_max

            elif mise_max < 0:
                print("Ah oui, vaut mieux pas gagner le gros lot avec une telle somme...")
                GUI.attend()
                print("Bon, sérieusement, je veux un nombre positif, s'il te plait.")

            elif len(str(mise_max).split('.')[1]) > 2:
                print("Non, non, non, j'vais pas passer la nuit à compter les mili..mili-centimes...")
        except ValueError:
            print("Désolé, ici on ne gagne pas de dictées...")
            GUI.attend(0.5)
            print("Hum.. parie une somme, un nombre positif, s'il te plait.")
            GUI.attend()
            pass
