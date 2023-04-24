import subprocess

try:
    import colorama
except ImportError:
    try:
        print("colorama n'est pas installé, installation en cours...")
        subprocess.check_call(["pip", "install", "pandas"])
        import colorama
        print("colorama est installé !")
    except subprocess.CalledProcessError:
        print("Le module pip n'est pas présent !")
        print("Vous pouvez faire [chemin de l'executable python] -m install colorama pour installer colorama")


try:
    import pandas
except ImportError:
    try:
        print("pandas n'est pas installé, installation en cours...")
        subprocess.check_call(["pip", "install", "pandas"])
        import pandas
        print("pandas est installé !")
    except subprocess.CalledProcessError:
        print("Le module pip n'est pas présent !")
        print("Vous pouvez faire [chemin de l'executable python] -m install pandas pour installer pandas")


from modules import roulette, stats, sim, GUI


def roulette_menu():
    """Menu de la roulette, permet de jouer en solo, en multi, ou de voir les règles de la roulette"""

    while True:  # choix des options
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='ROULETTE')

        GUI.options_listees('SOLO', 'MULTI', 'REGLES', 'RETOUR')

        choix = input("Veuillez sélectionner parmi (1/2/3/4) : \n")

        if choix == '1':  # SOLO, appelle la fonction solo() du module roulette
            roulette.session_solo()  # appelle la fonction solo() du module roulette
            break

        elif choix == '2':  # MULTI, appelle la fonction multi() du module roulette
            roulette.session_multi()
            break

        elif choix == '3':  # REGLES, appelle la fonction regles() du module roulette
            roulette.regles()
            break

        elif choix == '4':  # Retour au menu principal
            menu_principal()
            break

        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont (1/2/3/4) et non des lettres ou autres    ⚠')
            GUI.attend()
# fonction implémentée pour le menu principal ✅


def statistiques_menu():
    while True:  # choix des options
        GUI.clear_screen()

        GUI.header(couleur='CYAN', titre='STATISTIQUES')

        GUI.options_listees('Stats des joueurs', 'Stats du casino', 'Retour')

        choix = input("Veuillez sélectionner parmi (1/2/3) : \n")

        if choix == '1':  # Stats du mode solo, pour rechercher un joueur
            stats.show('joueur')
            break

        elif choix == '2':  # Retour au menu roulette, appelle la fonction roulette_main()
            stats.show('casino')
            break

        elif choix == '3':  # Retour au menu roulette, appelle la fonction roulette_main()
            menu_principal()
            break
        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont (1/2/3) et non des lettres ou autres    ⚠')
            GUI.attend()
# fonction implémentée pour le menu principal ✅


def simulation_menu():
    while True:  # choix des options

        GUI.clear_screen()

        GUI.header(couleur='BLUE', titre='SIMULATION')

        GUI.options_listees('Simulation', 'Réglages', 'Retour')

        choix = input("Veuillez sélectionner parmi (1/2/3) : \n")

        if choix == '1':  # commencer la simulation
            sim.simulation()
            break

        elif choix == '2':  # réglages de la simulation
            sim.reglages()
            break
        elif choix == '3':  # Retour au menu principal
            menu_principal()
            break
        else:
            print('⚠    Seuls choix possibles sont (1/2/3) et non des lettres ou autres    ⚠')
            GUI.attend()


def menu_principal():
    """ Fonction principale, permet la sélection des modes """
    while True:

        GUI.clear_screen()

        GUI.menu_principal()

        GUI.options_listees('Roulette', 'Statistiques', 'Simulation', 'Quitter')

        choix = input("\nChoisis le mode, ou quitte le programme (1/2/3/4) : \n")

        if choix == '1':
            roulette_menu()  # appelle la fonction roulette_main(), qui permet de choisir entre solo, multi, ou regles
            break
        elif choix == '2':
            statistiques_menu()  # appelle la fonction statistiques_main(), qui permet de choisir entre solo, multi,
            # ou archives
            break
        elif choix == '3':  # appelle la fonction simulation_main(), qui permet de choisir entre solo ou multi
            simulation_menu()
            break
        elif choix == '4':  # quitte le programme, avec un petit message de départ :D
            print("à la prochaine, hehe...")
            GUI.attend()
            exit()
        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont (1/2/3/4) et non des lettres ou autres    ⚠')
            GUI.attend()
# menu principal implémenté ✅


if __name__ == '__main__':
    print("Lancement du programme...")

    # respectivement pour les fonctions roulette_menu(), stats_menu(), simulation_menu() et les fonctions pour le GUI
    menu_principal()
