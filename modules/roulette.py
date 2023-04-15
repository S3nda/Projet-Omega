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
def init_var():
    num_partie = 0
    return


def init_joueur():
    # date
    date = datetime.datetime.now()

    # numéro de partie, incrémenté à chaque nouvelle partie
    num_partie = + 1

    # nom du joueur
    nom_joueur = data.nom()  # fonction nom, :return: nom_joueur

    # mise maximale
    mise_max = data.mise_maximale()  # fonction mise_maximale(), :return: mise_max

    joueur_data = {"nom": nom_joueur, "mise_max": mise_max, "date": date, "num_partie": num_partie}
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


def roulette_solo():
    init_joueur()
    tour()

    liste_data = initialisation_roulette_solo()
    liste_pari = tour(liste_data)
    liste_resultat = result_roulette()


def solo():
    if init:
        init()


def multi():
    return


def regles():
    '''Menu des règles, permet de lister les règles de la roulette'''
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
