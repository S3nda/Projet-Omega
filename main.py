import subprocess


def modules_check():
    """Vérifie si les modules sont installés
    :return: None
    nécessite toutefois l'importation de subprocess"""
    try:
        import colorama
        import os
        import random
        import time
    except ImportError:
        print(f"\"Des modules sont manquants, veuillez les installer pour pouvoir lancer le programme.")
        reponse = input("Voulez-vous les installer maintenant ? (o/n) ")
        if reponse.lower() == 'o':
            print("Installation des modules...")
            subprocess.run(['pip', 'install', 'colorama'])
            subprocess.run(['pip', 'install', 'os'])
            subprocess.run(['pip', 'install', 'random'])
            subprocess.run(['pip', 'install', 'time'])
            print("Les modules sont installés, le programme peut maintenant s'exécuter correctement.\n"
                  "Si il y a toujours des modules manquants, veuillez les installer manuellement. "
                  "(pip install <nom du module>)")
        else:
            print(
                "Les modules ne sont pas installés, le programme ne peut pas s'exécuter correctement. ")
            exit()

# menus principaux


def roulette_menu():
    """Menu de la roulette, permet de jouer en solo, en multi, ou de voir les règles de la roulette"""

    while True:  # choix des options
        GUI.clear_screen()

        GUI.header(couleur='YELLOW', titre='ROULETTE')

        GUI.options_listees('SOLO', 'MULTI', 'REGLES', 'RETOUR')

        choix = input("Veuillez sélectionner parmi 1,2,3,4 : \n")

        if choix == '1':  # SOLO, appelle la fonction solo() du module roulette
            roulette.solo()  # appelle la fonction solo() du module roulette
            break

        elif choix == '2':  # MULTI, appelle la fonction multi() du module roulette
            roulette.multi()
            break

        elif choix == '3':  # REGLES, appelle la fonction regles() du module roulette
            roulette.regles()
            break

        elif choix == '4':  # Retour au menu principal
            menu_principal()
            break

        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont 1,2,3 et 4, et non des lettres ou autres    ⚠')
# fonction implémentée pour le menu principal ✅


def statistiques_menu():
    while True:  # choix des options
        GUI.clear_screen()

        GUI.header(couleur='CYAN', titre='STATISTIQUES')

        GUI.options_listees('Stats solo', 'Stats multi', 'Retour')

        choix = input("Veuillez sélectionner parmi (1/2/3) : \n")

        if choix == '1':  # Stats du mode solo, appelle la fonction solo() du module stats
            stats.solo()
            break

        elif choix == '2':  # Stats du mode multi, appelle la fonction multi() du module stats
            stats.multi()
            break

        elif choix == '3':  # Retour au menu roulette, appelle la fonction roulette_main()
            menu_principal()
            break
        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont 1,2,3, et non des lettres ou autres    ⚠')
# fonction implémentée pour le menu principal ✅


def simulation_menu():
    while True:  # choix des options

        GUI.clear_screen()

        GUI.header(couleur='BLUE', titre='SIMULATION')

        GUI.options_listees('Simulation', 'Réglages', 'Retour')

        choix = input("Veuillez sélectionner parmi 1,2,3,4 : \n")

        if choix == '1':  # SOLO
            sim.simulation()
            break

        elif choix == '2':  # REGLAGES
            sim.reglages()
            break
        elif choix == '3':  # Retour au menu principal
            menu_principal()
            break
        else:
            print('⚠    Seuls choix possibles sont 1,2 et 3 et non des lettres ou autres    ⚠')


def menu_principal():
    """ Fonction principale, permet la sélection des modes """
    while True:

        GUI.clear_screen()

        GUI.menu_principal()

        GUI.options_listees('Roulette', 'Statistiques', 'Simulation', 'Quitter')

        choix = input("\nChoisissez le mode, ou quittez le programme (1/2/3/4) : \n")

        if choix == '1':
            roulette_menu()  # appelle la fonction roulette_main(), qui permet de choisir entre solo, multi, ou regles
            break
        elif choix == '2':
            statistiques_menu()  # appelle la fonction statistiques_main(), qui permet de choisir entre solo, multi,
            # ou archives
            break
        elif choix == '3':  # appelle la fonction simulation_main(), qui permet de choisir entre solo, multi,
            # ou archives
            simulation_menu()
            break
        elif choix == '4':  # quitte le programme, avec un petit message de départ :D
            print("à la prochaine, hehe")
            time.sleep(0.5)
            exit()
        else:  # mauvais input, on recommence (while True), pas de break
            print('⚠    Seuls choix possibles sont 1,2,3 et 4, et non des lettres ou autres    ⚠')
# menu principal implémenté ✅


if __name__ == '__main__':
    print("Lancement du programme...")
    modules_check()  # vérifie que les modules sont bien installés
    from modules import roulette, stats, sim, GUI
    import time
    menu_principal()
# condition pour lancer le programme, si on lance le fichier main.py, alors on lance la fonction main() ✅