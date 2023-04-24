from modules import GUI, data
import main


def recherche():
    while True:
        nom = input("Qui voulez vous rechercher ? : \n")
        trouve = data.search_nom(nom)
        if trouve:
            return trouve
        else:
            print(f"{nom} n'a jamais fréquenté le casino...\n")
            return None


def show(mode):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='CYAN', titre="STATISTIQUES - EN COURS D'ANALYSE")

        if mode == 'joueur':
            stats_joueur = recherche()
            if stats_joueur is not None:
                data.pres_stats_joueur(stats_joueur)
            if input("\nAppuyez sur entrée pour refaire une recherche, ou entrez N pour revenir :\n").lower() == 'n':
                main.menu_principal()

        elif mode == 'casino':
            try:
                stats_casino = data.stats_casino()
                data.pres_stats_casino(stats_casino)
            except ZeroDivisionError:
                print("Aucun joueur n'a encore fréquenté le casino...Fait donc quelques parties !\n")
            input("\nAppuyez sur entrée pour revenir au menu principal :\n")
            main.menu_principal()
