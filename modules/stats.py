from modules import GUI, data
import main


def stats_casino():
    while True:
        GUI.clear_screen()

        GUI.header('CYAN','STATISTIQUES - CASINO')
        reponse = input("Veux-tu voir les stats casino ? (O/N)\n").lower()
        if reponse == 'o':
            return True
        elif reponse == 'n':
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


def show(mode):
    while True:
        GUI.clear_screen()

        GUI.header(couleur='CYAN', titre="STATISTIQUES - EN COURS D'ANALYSE")

        if mode == 'joueur':
            stats_joueur = recherche()
            if stats_joueur is not None:
                data.pres_stats_joueur(stats_joueur)
            GUI.attend(2)
            if input("\nAppuyez sur entrée pour refaire une recherche, ou entrez N pour revenir :\n").lower() == 'n':
                main.menu_principal()

        elif mode == 'casino':
            stats_casino = data.stats_casino()
            if stats_casino is not None:
                data.pres_stats_casino(stats_casino)
            else:
                print("Aucun joueur n'a encore fréquenté le casino...\n")
            GUI.attend(2)
            if input("\nAppuyez sur entrée pour refaire une recherche, ou entrez N pour revenir :\n").lower() == 'n':
                main.menu_principal()
