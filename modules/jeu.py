from modules import GUI
import random


def mise(joueur_data):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - MISE')

        try:
            mise_du_joueur = int(input(f'"Entrez votre mise, {joueur_data["nom"]} : '""))
            if 0 < mise_du_joueur < joueur_data["argent_joueur"]:
                return mise_du_joueur
        except ValueError:
            print("Mettez une mise supérieure à 0 et inférieure à votre mise maximale "
                  "(non, vous ne pouvez pas créer d'argent, désolé)")


def pari_choix(paris_possibles_type):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - CHOIX DU PARI')

        pari = input("Choisissez votre pari (Pair/Impair/Rouge/Noir/Nombre) : ")
        if pari in paris_possibles_type:
            return pari
        else:
            print("Vous devez choisir un type de pari parmi ceux proposés")


def choix_nombre():
    while True:
        try:
            pari = int(input("Choisissez donc un nombre entre 0 et 36 : "))
            if 0 <= pari <= 36:
                return pari
        except ValueError:
            print("Vous devez choisir un nombre entre 0 et 36")
            pass


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
    GUI.attend()
    print(f"{numero_aleatoire} et {couleur_numero} !!!")

    resultat = {'numero_aleatoire': numero_aleatoire, "couleur_numéro": couleur_numero}
    return resultat


def passage_a_la_caisse(pari, resultat, data_joueur):
    argent_joueur = data_joueur['argent_joueur']
    mise = pari['mise']

    if pari['nombre'] == resultat['numero_aleatoire'] and pari['type'] == 'Nombre':
        print(f"Vous avez gagné! 🏆🏆 Vous avez donc gagné {liste_data[0] * 36} €")
        data_joueur['argent_joueur'] += pari['mise'] * 35
        print(f"Il vous reste {data_joueur['argent_joueur']} €")

    elif pari['type'] == resultat['couleur_numero'] and pari['type'] in ['Rouge', 'Noir']:
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        data_joueur['argent_joueur'] += pari['mise']
        print(f"Il vous reste {data_joueur['argent_joueur']} €")

    elif pari['type'] == 'Pair' and resultat['numero_aleatoire'] % 2 == 0:
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        data_joueur['argent_joueur'] += pari['mise']
        print(f"Il vous reste {data_joueur['argent_joueur']} €")

    elif pari['type'] == 'Impair' and resultat['numero_aleatoire'] % 2 == 1:
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        data_joueur['argent_joueur'] += pari['mise']
        print(f"Il vous reste {data_joueur['argent_joueur']} €")

    else:  # pour s'il a faux
        print(f"Dommage! Vous avez perdu 😭😭. Vous avez donc perdu {liste_data[0]}")
        data_joueur['argent_joueur'] -= pari['mise']
        print(f"Il vous reste {data_joueur['argent_joueur']} €")
