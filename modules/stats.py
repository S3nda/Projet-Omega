from modules import GUI, data
import main


def stats_casino():
    while True:
        GUI.clear_screen()

        GUI.header('BLUE','STATISTIQUES - CASINO')
        reponse = input("Veux-tu voir les stats casino ? (O/N)\n").lower()
        if reponse == 'o':
            return True
        elif reponse == 'n' :
            return False
        else:
            print("Réponds par O ou N")
            GUI.attend()


def recherche():
    while True:
        nom = input("Qui voulez vous rechercher ? : \n")
        trouve = data.search_nom(nom)
        if trouve:
            return trouve
        else:
            print(f"{nom} n'a jamais fréquenté le casino...\n")
            return None


def pres_stats_casino(stats):
    for clee in stats:
        print('nombre de joueurs uniques: ')
        print(f"chiffre d'affaire:")
        print('bénéfices net :')


def show():
    while True:
        GUI.clear_screen()

        GUI.header(couleur='CYAN', titre="STATISTIQUES - EN COURS D'ANALYSE")

        stats_joueur = recherche()
        if stats_joueur is not None:
            data.pres_stats_joueur(stats_joueur)
        GUI.attend(2)
        if input("\nAppuyez sur une touche pour refaire une recherche, ou entrez O pour revenir :\n").lower() == 'o':
            main.menu_principal()

# fonction pratique implémentée pour le menu STATISTIQUES ✅

