from modules import GUI
import main, re, random
from colorama import Fore, Style


def mise(argent_joueur, nom_joueur):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - MONTANT DE LA MISE')

        try:
            mise_du_joueur = float(input(f'Entre ta mise, {nom_joueur} : '""))
            if 0 < mise_du_joueur <= argent_joueur and len(str(mise_du_joueur).split('.')[1]) <= 2:
                return mise_du_joueur
            else:
                print(f"Mettez une mise supérieure à 0 et dans ton budget, c'est à dire {argent_joueur} €.\n"                                                                                                               
                      f"Aussi, je vais pas perdre mon "
                      "temps à compter les centimes")
                GUI.attend()
        except ValueError:
            print("Un nombre, entier, s'il te plait.")
            GUI.attend()


def choix_nombre():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - CHOIX DU NOMBRE')
        try:
            choix_nombre = int(input("Choisis donc un nombre entre 0 et 36 : "))
            if 0 <= choix_nombre <= 36:
                return choix_nombre
            else:
                print("Tu dois choisir un nombre entre 0 et 36")
                GUI.attend()
                pass
        except ValueError:
            print("Tu dois choisir un nombre entre 0 et 36")
            GUI.attend()
            pass


def pari_choix(pari, argent, nom):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - PARIE DONC !')

        choix = input(f"{nom}, Tu choisis de parier sur quoi ?\n"
                      "(Pair/Impair/Rouge/Noir/Nombre): \n").lower()
        if choix in ['nombre']:
            nombre = choix_nombre()
            if nombre in pari:
                print("Comme tu as déjà parié sur ce nombre, je vais donc rajouter ta mise à la mise précédente sur "
                      "ce nombre")
                GUI.attend()
                pari[nombre] += mise(argent, nom)
            else:
                pari[nombre] = mise(argent, nom)
            argent_post_mise = argent - pari[nombre]
            return pari, argent_post_mise

        elif choix in ['pair', 'impair', 'rouge', 'noir']:
            if choix in pari:
                print("Je vais donc rajouter ta mise à la mise précédente sur ce nombre")
                GUI.attend()
                pari[choix] += mise(argent, nom)
            else:
                pari[choix] = mise(argent, nom)
            argent_post_mise = argent - pari[choix]
            return pari, argent_post_mise
        else:
            print("Tu dois choisir un type de pari parmi ceux proposés")
            GUI.attend()


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
    GUI.attend()
    return resultat


def passage_a_la_caisse(mise, resultat, argent, choix, nom):
    GUI.clear_screen()

    GUI.header(couleur='YELLOW', titre='EN JEU - PASSAGE À LA CAISSE')

    if choix == resultat['numero_aleatoire']:
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.GREEN}+{mise*35} €{Fore.RESET}")
        argent += mise * 36
    if choix == resultat['couleur_numero']:
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.GREEN}+{mise} €{Fore.RESET}")
        argent += mise*2
    if resultat['numero_aleatoire'] == 0 and choix != 0 and choix != 'pair':
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.GREEN}+{mise*0.5} €{Fore.RESET}")
        argent += mise*1.5
    if resultat['numero_aleatoire'] % 2 == 0:
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.GREEN}+{mise} €{Fore.RESET}")
        if choix == 'pair':
            argent += mise*2
    if resultat['numero_aleatoire'] % 2 == 1:
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.GREEN}+{mise} €{Fore.RESET}")
        if choix == 'impair':
            argent += mise*2
    else:  # pour s'il a faux
        print(f"Pour toi, {Fore.YELLOW}{nom}{Fore.RESET}, {Fore.RED}-{mise} €{Fore.RESET}")
        pass
    return argent


def continuer(nom, argent_joueur, mode):
    GUI.clear_screen()

    GUI.header(couleur='YELLOW', titre='EN JEU - BILAN')

    print(f'{Fore.YELLOW}{nom}{Style.RESET_ALL}, Tu as maintenant {argent_joueur} € ! Voyons voir...')
    GUI.attend()

    if argent_joueur != 0:
        while True:
            GUI.clear_screen()

            GUI.header(couleur='YELLOW', titre='CONTINUER ?')
            reponse_continuer = input("Veux-tu continuer à jouer ? (O/N) ")
            if reponse_continuer.lower() == 'o':
                return True
            elif reponse_continuer.lower() == 'n':
                return False
            else:
                print("Tu dois répondre par O ou N")
                GUI.attend()
    else:
        print(f"Mmmh... Désolé, {Fore.YELLOW}{nom}{Style.RESET_ALL}, {Fore.RED}mais tu n'as plus d'argent.{Style.RESET_ALL}")
        GUI.attend()
        if mode == 'solo':
            GUI.body_game_over()
        GUI.attend()
        return False


def nom(nbr_joueurs):
    """Demande le nom du joueur, et vérifie qu'il est correct"""
    while True:
        GUI.clear_screen()
        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION')
        # checks if the string contains only letters, numbers and underscores
        nom_joueur = input(f"{('Joueur' + str(nbr_joueurs)) if nbr_joueurs!='solo' else 'Alors ?'}, Comment "
                           f"t'appelles-tu ?\n")
        if 15 > len(nom_joueur) > 0 and " " not in nom_joueur and re.match(r'^[a-zA-Z0-9_]*$', nom_joueur):
            # si le nom est bon, on sort de la boucle
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

        GUI.header(couleur='YELLOW', titre='DEBUT DE SESSION - MISE MAXIMALE')

        try:  # on essaie de convertir la mise en entier
            mise_max = float(input(f"{nom_joueur}, Fixe toi une limite de mise :\n"))
            if mise_max > 0 and not len(str(mise_max).split('.')[1]) > 1:
                return mise_max

            elif mise_max < 0:
                print("Ah oui, vaut mieux pas gagner le gros lot avec une telle somme...")
                GUI.attend()
                print(f"Bon, sérieusement, je veux un {Fore.YELLOW}nombre positif{Fore.RESET}, s'il te plait.")
            elif len(str(mise_max).split('.')[1]) > 2:
                print("Non, non, non, j'vais pas passer la nuit à compter les mili..mili-centimes...")
        except ValueError:
            print("Désolé, ici on ne gagne pas de dictées...")
            GUI.attend(0.5)
            print("Hum.. parie une somme, un nombre positif, s'il te plait."
                  "Si tu veux mettre un décimal, sépare par un point")
            GUI.attend()
            pass


def re_parier(argent):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - REPARIER ?')

        if not argent == 0:
            continuer = input("Veux tu parier sur d'autres choses ? (O/N) \n").lower()
            if continuer == "o":
                return True
            elif continuer == 'n':
                return False
            else:
                print("Tu dois répondre par (O/N)")
        else:
            print(f"{Fore.RED}Désolé, mais tu ne peux plus reparier...{Fore.RESET}")
            GUI.attend()
            return False


def resume_pari(pari):
    GUI.clear_screen()

    GUI.header(couleur='YELLOW', titre='EN JEU - RÉSUMÉ DU PARI')

    print('En résumé : ')
    for choix in pari:
        print(f"Tu as parié {pari[choix]}€ sur {choix}")

    GUI.attend()


def nbr_joueur():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='EN JEU - CHOIX DU NOMBRE DE JOUEURS')

        try:
            nbr_joueur = int(input("Combien de joueurs ? (2-4) \n"))
            if 1 < nbr_joueur < 5:
                return nbr_joueur
            else:
                print("Tu dois répondre par un nombre entre 2 et 4")
                GUI.attend()
        except ValueError:
            print("Tu dois répondre par un nombre entre 2 et 4")
            GUI.attend()


def regles():
    while True:  # choix des options
        GUI.clear_screen()

        GUI.header('YELLOW', 'ROULETTE - REGLES')
        # Centre le texte dans la console
        print(f"{Fore.YELLOW}".center(80))
        print(f"Voici les règles de la roulette:".center(80))
        print("")
        print(f"D'abord, ce jeu se joue avec une roue coupée en 37 cases,")
        print(f"à chaque case est associé un numéro allant de 0 à 36 et une couleur (rouge ou noir).")
        print(f"Les numéros{Fore.RED} ne sont pas triés dans l'ordre et ne sont présents qu'en un unique exemplaire.{Fore.YELLOW}")
        print(f"Il y a le même nombre de cases rouges que de cases noires, en effet le 0 est {Fore.GREEN}vert.")
        print("")
        print(f"{Fore.YELLOW}On lance une bille sur la roue qui tourne horizontalement et on regarde sur quelle case "
              f"s'arrête la bille.")
        print(f"Le but du jeu est de miser sur une ou plusieurs caractéristiques de la case sur laquelle va tomber la "
              f"bille.")
        print("")
        print(f"On peut miser sur la couleur (rouge ou noir), le nombre (de 0 à 36),")
        print(f"la parité du nombre (pair ou impair) de la case ou va s'arrêter la bille.")
        print(f"Bien sûr, plus on mise sur un petit ensemble de cases, plus on gagne d'argent.")
        print(f"Ainsi, en ayant misé sur la bonne parité ou la bonne couleur,")
        print(f"on gagne 2X notre mise alors qu'en misant sur le bon numéro on obtient {Fore.GREEN}36X notre mise.{Fore.YELLOW}")
        print(f"{Fore.RED}Si la bille s'arrête sur 0, tous les joueurs récupèrent 1,5X leur mise.")
        print(f"{Fore.YELLOW}On peut miser plusieurs fois et autant que notre argent le permet.")
        print("")
        print(f"ATTENTION, le jeu n'est {Fore.RED}pas truqué{Fore.YELLOW} et {Fore.RED}aucune réclamation ne sera "
              f"acceptée{Fore.YELLOW}")
        print("auprès du personnel du casino en ligne de la C118.")
        print("")
        print(f"{Fore.GREEN}Bon jeu...{Style.RESET_ALL}")

        choix = input("Entrez 1 pour revenir en arrière: \n")  # input du choix
        if choix != '1':
            print('Tu ne peux mettre que 1...')  # si le choix n'est pas 1, on recommence (while True), pas de break
        else:  # si le choix est 1, on retourne au menu roulette
            main.roulette_menu()