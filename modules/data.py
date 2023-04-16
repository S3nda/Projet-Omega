from modules import GUI


def nom():
    """Demande le nom du joueur, et vérifie qu'il est correct"""
    while True:
        GUI.clear_screen()
        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION')

        nom_joueur = input("Comment tu t'appelles ? : ")
        if 10 > len(nom_joueur) > 0 and " " not in nom_joueur:  # si le nom est bon, on sort de la boucle
            return nom_joueur
        else:  # si le nom n'est pas bon, on passe à la prochaine itération
            print("C'est quoi ce nom ?!")
            GUI.attend(1)
            print("Bon, sérieusement, un nom/pseudo, sans espace, pas trop long, s'il te plait.")
            GUI.attend(1)


def mise_maximale(nom_joueur):
    """:return: mise_max, la mise maximale que le joueur peut parier
    :rtype: float
    """
    print(f'{nom_joueur}... Enchanté !')
    GUI.attend(1)
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION')

        try:  # on essaie de convertir la mise en entier
            mise_max = float(input("Fixe toi une limite de mise :"))
            if mise_max > 0 and not len(str(mise_max).split('.')[1]) > 2:
                return mise_max

            elif mise_max < 0:
                print("Ah oui, vaut mieux pas gagner le gros lot avec une telle somme...")
                GUI.attend(1)
                print(" Bon, sérieusement, je veux un nombre positif, s'il te plait.")

            elif len(str(mise_max).split('.')[1]) > 2:
                print("non, non, non, j'vais pas passer la nuit à compter les mili..mili-centimes...")
        except ValueError:  # si la mise n'est pas un entier...
            print("Désolé, ici on ne gagne pas de dictées...")
            GUI.attend(1)
            print(" Bon, sérieusement, parie une somme, un nombre positif, s'il te plait.")
            GUI.attend(1)
            pass
