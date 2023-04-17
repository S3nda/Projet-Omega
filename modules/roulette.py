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
            jeu.continuer(nouveau_joueur.argent, nouveau_joueur.nom)
            if jeu.continuer(nouveau_joueur.argent, nouveau_joueur.nom):
                nouveau_joueur.tour()
            else:
                print(nouveau_joueur.stats())
                GUI.attend(2)
                menu_principal()
    else:
        joueur_habitue = nom_joueur
        joueur_habitue.entree()
        print("Ah oui, c'est bien toi  !")
        GUI.attend(1)
        print("On fait comme d'habitude alors...")
        joueur_habitue.mise_max()
        joueur_habitue.debut()
        while True:
            joueur_habitue.tour()

            jeu.continuer(joueur_habitue.argent, joueur_habitue.nom)
            if jeu.continuer(joueur_habitue.argent, joueur_habitue.nom):
                joueur_habitue.tour()
            else:
                print(joueur_habitue.stats())
                GUI.attend(2)
                menu_principal()


class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.date = datetime.datetime.now()
        self.num_entree = 0
        self.num_tour = 0
        self.mise_totale = 0
        self.argent_debut = None
        self.argent = None
        self.resultat = None
        self.pari = None
        self.mise = None
        self.gain_tour = None
        self.gain_session = None

    def entree(self):
        self.num_entree = + 1
        pass

    def mise_max(self):
        self.argent = data.mise_maximale(self.nom)
        pass

    def stats(self):
        return {
            'nom': self.nom,
            "nombre d'entrées": self.num_entree,
            'argent moyen dépensé par session': self.mise_totale / self.num_entree,
            'argent dépensé au total': self.mise_totale,
            'mise moyenne par tour': self.mise_totale / self.num_tour,
            'gain par session': self.gain_session,
        }

    def tour(self):
        self.argent_debut = self.argent
        self.num_tour = + 1
        self.mise = jeu.mise(self.argent, self.nom)
        self.mise_totale = self.mise_totale + self.mise
        self.pari = jeu.pari_choix(["pair", "impair", "rouge", "noir", "nombre"])
        print("Voulez vous parier sur autre chose ?")
        if self.pari['type'] == "nombre":
            self.pari = jeu.choix_nombre()
        self.resultat = jeu.result_roulette()
        GUI.attend(1)
        self.argent = jeu.passage_a_la_caisse(self.pari, self.resultat, self.mise, self.argent)
        self.gain_tour = self.argent - self.argent_debut
        self.gain_session = self.gain_tour + self.gain_tour

        GUI.attend(3)


def multi():
    return


def regles():
    GUI.clear_screen()

    GUI.header('YELLOW', 'ROULETTE - REGLES')
    GUI.body('YELLOW', '')
    while True:  # choix des options
        choix = input("Entrez 1 pour revenir en arrière: \n")  # input du choix
        if choix != '1':
            print('Tu ne peux mettre que 1...')  # si le choix n'est pas 1, on recommence (while True), pas de break
        else:  # si le choix est 1, on retourne au menu roulette
            roulette_menu()
            break
    return
