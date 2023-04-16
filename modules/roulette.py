#   pour revenir au menu :
from main import roulette_menu, menu_principal

#   pour l'interface graphique
from modules import GUI

#   fonctions pour initialiser et datas
from modules import data

#   fonctions primaires du module roulette
from modules import jeu

#   pour le tirage aléatoire et les stats
import datetime


# premiere fois que le logiciel est lancé

def init_joueur(init, joueur_data):
    if init:
        num_entree = 1
        nom_joueur = data.nom()
    else:
        num_entree = + 1
        nom_joueur = joueur_data['nom']

    # date à laquelle le joueur commence sa session de jeu
    date = datetime.datetime.now()

    num_tour = 0  # numéro de tour

    # mise maximale
    mise_max = data.mise_maximale(nom_joueur)
    # fonction mise_maximale(), :return: mise_max

    joueur_data = {"nom": nom_joueur, "argent_joueur": mise_max, "date": date, "num_entree": num_entree,
                   "num_tour": num_tour}
    # on crée un dictionnaire avec les données du joueur : nom, mise, date, numéro de partie
    return joueur_data


def tour(joueur_data):
    jeu.mise(joueur_data)

    pari_types = ["Pair", "Impair", "Rouge", "Noir", "Nombre"]
    jeu.pari_choix(pari_types)

    jeu.result_roulette()

    if pari == "Nombre":
        jeu.nombre_pari()

    return liste_parier


def roulette_solo(joueur_data):
    data_initiale = joueur_data
    while True:
        jeu.mise(joueur_data)

        pari_types = ["Pair", "Impair", "Rouge", "Noir", "Nombre"]
        pari = jeu.pari_choix(pari_types)
        if pari == "Nombre":
            pari = jeu.choix_nombre()
        else:
            pari = pari
            pass
        resultat = jeu.result_roulette()
        jeu.passage_a_la_caisse(resultat, joueur_data, pari)

        continuer = input("Voulez-vous continuer à jouer ? (O/N) ")
        if continuer.lower() == 'o':
            joueur_data['num_partie'] = + 1
            gain_brut = joueur_data['argent_joueur'] - data_initiale['argent_joueur']
            continue
        else:
            gain_moyen = gain_brut / joueur_data['num_partie']
            # Sinon, on quitte le jeu
            GUI.clear_screen()
            GUI.header(couleur='YELLOW', titre='MERCI D\'AVOIR JOUÉ')
            print(f"Nom du joueur: {joueur_data['nom']}")
            print(f"Mise maximale: {joueur_data['mise_max']} €")
            print(f"Date: {joueur_data['date'].strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Numéro de partie: {joueur_data['num_partie']}")
            print("A bientôt !")
            break


def solo(init=True):
    clients_uniques = {}
    if init:
        joueur_data = init_joueur(init=True, joueur_data={})    # renvoie un dictionnaire avec les données du joueur
        clients_uniques[joueur_data['nom']] = joueur_data   # on ajoute le dictionnaire du joueur
        # dans le dictionnaire des clients uniques
        roulette_solo(joueur_data)  # on lance la partie

    else:
        nom_joueur = data.nom()
        for joueur in clients_uniques:
            if nom_joueur == clients_uniques[joueur]['nom']:
                joueur_data = clients_uniques[joueur]
                print("Ah oui, c'est bien toi  !")
                GUI.attend(1)
                print("On fait comme d'habitude alors...")

                joueur_data = init_joueur(init=False, joueur_data=joueur_data)
                roulette_solo(joueur_data)




def multi():
    return


def regles():
    """Menu des règles, permet de lister les règles de la roulette"""
    GUI.clear_screen()
    header_et_body_regles = ('\n'
                             '    [-----------------------------------------------------------------------------]\n'
                             '                                |REGLES DE LA ROULETTE|                             \n'
                             '\n'
                             'Le joueur peut                             \n'
                             '                                |REGLES DE LA ROULETTE|                             \n'
                             '                                |REGLES DE LA ROULETTE|                             \n'
                             '                                |REGLES DE LA ROULETTE|                             \n'
                             '                                |REGLES DE LA ROULETTE|                             \n'
                             '    [-----------------------------------------------------------------------------]\n')
    print(header_et_body_regles)  # print le header ainsi que le body du menu REGLES DE LA ROULETTE
    print('1) RETOUR\n')  # print les options du menu

    while True:  # choix des options
        choix = input("Entrez 1 pour revenir en arrière: \n")  # input du choix
        if choix != '1':
            print('Tu ne peux mettre que 1...')  # si le choix n'est pas 1, on recommence (while True), pas de break
        else:  # si le choix est 1, on retourne au menu roulette
            roulette_menu()
            break
    return
