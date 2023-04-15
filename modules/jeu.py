from modules import GUI
import random

def mise(joueur_data):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU')

        try:
            mise_du_joueur = int(input(f'"Entrez votre mise, {joueur_data["nom"]} : '""))
            if 0 < mise_du_joueur < joueur_data["mise_max"]:
                return mise_du_joueur
        except:
            print("Mettez une mise supérieure à 0 et inférieure à votre mise maximale "
                  "(non, vous ne pouvez pas créer d'argent, désolé)")


def pari_choix(paris_possibles_type):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU')

        pari = input("Choisissez votre pari (Pair/Impair/Rouge/Noir/Nombre) : ")
        if pari in paris_possibles_type:
            return pari
        else:
            print("Vous devez choisir un type de pari parmi ceux proposés")


def pari_nombre():
    while True:
        try:
            nombre_pari = int(input("Choisissez donc un nombre entre 0 et 36 : "))
            if 0 <= nombre_pari <= 36:
                break
        except:
            print("Vous devez choisir un nombre entre 0 et 36")
            pass

    return nombre_pari


def result_roulette():
    liste_vide = []
    num = [i for i in range(37)]
    for i in num:
        variable_aleatoire = random.choice(["Noir", "Rouge"])
        liste_vide.append([i, variable_aleatoire])
    liste_vide.append([0, "Vert"])  # on rajoute le fameux 0
    # élément allant dans le csv
    numero_aleatoire = random.randint(1, 36)
    couleur_numero = liste_vide[numero_aleatoire][1]

    print("Et la roulette s'arrête sur....")
    GUI.attends()
    print(f"{numero_aleatoire} et {couleur_numero} !!!")

    resultat = {'numero_aléatoire': numero_aleatoire, "couleur_numéro": couleur_numero}
    return resultat


def passage_a_la_caisse(joueur_data, resultat):
    if liste_pari[2] == data_joueur[]:  # pour si resultat correcte pour nombre pile
        print(f"Vous avez gagné! 🏆🏆 Vous avez donc gagnez {liste_data[0] * 36} €")
        mise_max = joueur_data["mise max"] + liste_pari[0] * 35
        print(f"Il vous reste {mise_max} €")


    elif resultat["numéro aléatoire"] == liste_pari[1]:  # pour si resultat correcte pour couleur
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = joueur_data["mise max"] + liste_pari[0]
        print(f"Il vous reste {mise_max} €")


    elif numero_aleatoire // 2 == 0 and pari == "Pair":  # pour si resultat correcte <-----  pour parité du nombre
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = joueur_data["mise max"] + liste_pari[0]
        print(f"Il vous reste {mise_max} €")


    elif numero_aleatoire // 2 == 1 and pari == "Impair":
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = joueur_data["mise max"] + liste_pari[0]
        print(f"Il vous reste {mise_max} €")

    elif numero_aleatoire == 0 and not nombre_parier == numero_aleatoire:
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 1.5} €")
        mise_max = joueur_data["mise max"] + liste_pari[0]
        print(f"Il vous reste {mise_max} €")

    else:  # pour s'il a faux
        print(f"Dommage! Vous avez perdu 😭😭. Vous avez donc perdu {liste_data[0]}")
        mise_max = joueur_data["mise max"] - liste_pari[0]
        print(f"Il vous reste {mise_max} €")

    nouvelle_partie = input("Voulez-vous rejouer un partie(y/n) : ")
    if nouvelle_partie == "y":
        print("C'est reparti pour ...")
        roulette_solo(mise_max)
    else:
        print("Dommage vous avez potentiellement perdu beaucoup d'argent")



