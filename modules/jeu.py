from modules import GUI
import random


def mise(argent_joueur, nom_joueur):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - MONTANT DE LA MISE')

        try:
            mise_du_joueur = int(input(f'Entre ta mise, {nom_joueur} : '""))
            if 0 < mise_du_joueur <= argent_joueur:
                return mise_du_joueur
        except ValueError:
            print("Mettez une mise supérieure à 0 et inférieure à votre mise maximale "
                  "(non, vous ne pouvez pas créer d'argent, désolé)")
            GUI.attend()


def pari_choix(paris_possibles_type):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - CHOIX DU TYPE DE PARI')

        choix_pari = input("Choisissez votre pari (Pair/Impair/Rouge/Noir/Nombre) : ").lower()
        pari = {'type': choix_pari}

        if choix_pari in paris_possibles_type:
            return pari
        else:
            print("Vous devez choisir un type de pari parmi ceux proposés")
            GUI.attend()


def choix_nombre():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - CHOIX DU NOMBRE')
        try:
            choix_pari = int(input("Choisissez donc un nombre entre 0 et 36 : "))
            if 0 <= choix_pari <= 36:
                pari = {'choix_pari': choix_pari, 'type': 'nombre'}
                return pari
            else:
                print("Tu dois choisir un nombre entre 0 et 36")
                GUI.attend()
                pass
        except ValueError:
            print("Tu dois choisir un nombre entre 0 et 36")
            GUI.attend()
            pass


def result_roulette():
    GUI.clear_screen()

    GUI.header(couleur='YELLOW', titre='EN JEU - RÉSULTAT DE LA ROULETTE')
    liste_vide = []
    num = [i for i in range(37)]
    for i in num:
        variable_aleatoire = random.choice(["noir", "rouge"])
        liste_vide.append([i, variable_aleatoire])
    liste_vide.append([0, "vert"])  # on rajoute le fameux 0
    # élément allant dans le csv1
    numero_aleatoire = random.randint(1, 36)
    couleur_numero = liste_vide[numero_aleatoire][1]

    print("Et la roulette s'arrête sur....")
    GUI.attend()
    print(f"{numero_aleatoire} et {couleur_numero} !!!")

    resultat = {'numero_aleatoire': numero_aleatoire, "couleur_numero": couleur_numero}
    return resultat


def passage_a_la_caisse(pari, resultat, mise, argent):
    GUI.clear_screen()

    GUI.header(couleur='YELLOW', titre='EN JEU - PASSAGE À LA CAISSE')

    if pari['type'] == resultat['numero_aleatoire'] and pari['type'] == 'nombre':
        print(f"J A C K P O T! Vous gagnez {mise * 36} €")
        argent += mise * 35
        print(f"Il vous reste {argent} €")
    elif pari['type'] == resultat['couleur_numero'] and pari['type'] in ['rouge', 'noir']:
        print(f"La chance vous a souri! Vous gagnez {mise * 2} €")
        argent += mise
        print(f"Il vous reste {argent} €")
    elif pari['type'] == 'pair' and resultat['numero_aleatoire'] % 2 == 0:
        print(f"La chance vous a souri! Vous gagnez {mise * 2} €")
        argent += mise
        print(f"Il vous reste {argent} €")
    elif pari['type'] == 'impair' and resultat['numero_aleatoire'] % 2 == 1:
        print(f"La chance vous a souri ! Vous gagnez {mise * 2} €")
        argent += mise
        print(f"Il vous reste {argent} €")

    else:  # pour s'il a faux
        print(f"Aïe! Vous perdez {mise}€")
        argent -= mise
        print(f"Il vous reste {argent} €")


def continuer(argent_joueur):
    print(f"Vous avez {argent_joueur} €")
    if argent_joueur == 0:
        print("C la desh")
        return False
    else:
        while True:
            GUI.clear_screen()

            GUI.header(couleur='YELLOW', titre='CONTINUER ?')
            reponse_continuer = input("Voulez-vous continuer à jouer ? (O/N) ")
            if reponse_continuer.lower() == 'o':
                return True
            elif reponse_continuer.lower() == 'n':
                return False
            else:
                print("Vous devez répondre par O ou N")
                GUI.attend()


