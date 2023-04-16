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


def solo():
    joueurs = {}
    nom_joueur = data.nom()

    if nom_joueur not in joueurs:
        nouveau_joueur = Joueur(nom_joueur)
        nouveau_joueur.entree()
        print(f'{nom_joueur}... Enchanté !')
        GUI.attend(1)
        joueurs[nom_joueur] = nouveau_joueur
        nouveau_joueur.mise_max()
        while True:
            nouveau_joueur.tour()
            jeu.continuer(nouveau_joueur.argent)
            if jeu.continuer(nouveau_joueur.argent):
                nouveau_joueur.tour()
            else:
                exit()
    else:
        joueur_habitue = nom_joueur
        joueur_habitue.entree()
        print("Ah oui, c'est bien toi  !")
        GUI.attend(1)
        print("On fait comme d'habitude alors...")
        joueur_habitue.mise_max()
        while True:
            joueur_habitue.tour()

            jeu.continuer(joueur_habitue.argent)
            if jeu.continuer(joueur_habitue.argent):
                joueur_habitue.tour()
            else:
                print("éteins la lumière quand tu sors !")
                exit()


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.date = datetime.datetime.now()
        self.num_entree = 0
        self.argent_debut = 0
        self.argent = None
        self.num_tour = 0
        self.resultat = None
        self.pari = None
        self.mise = None
        self.gain_session = None

    def entree(self):
        self.num_entree = + 1
        pass

    def mise_max(self):
        self.argent = data.mise_maximale(self.nom)
        pass

    def mise(self):
        self.mise = jeu.mise(self.argent, self.nom)
        pass

    def pari_choix(self):
        self.pari = jeu.pari_choix(["Pair", "Impair", "Rouge", "Noir", "Nombre"])
        pass

    def choix_nombre(self):
        self.pari = jeu.choix_nombre()
        pass

    def result_roulette(self):
        self.resultat = jeu.result_roulette()
        pass

    def passage_a_la_caisse(self):
        self.argent, self.pari, self.resultat, = jeu.passage_a_la_caisse(self.pari, self.resultat, self.mise, self.argent)
        pass

    def tour(self):
        self.argent_debut = self.argent
        self.num_tour = + 1
        self.mise = jeu.mise(self.argent, self.nom)
        self.pari = jeu.pari_choix(["pair", "impair", "rouge", "noir", "nombre"])
        print("Voulez vous parier sur autre chose ?")
        if self.pari['type'] == "nombre":
            self.pari = jeu.choix_nombre()
        self.resultat = jeu.result_roulette()
        GUI.attend(1)
        jeu.passage_a_la_caisse(self.pari, self.resultat, self.mise, self.argent)
        self.gain_session = self.argent - self.argent_debut
        GUI.attend(3)


def multi():
    return


def regles():
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
