import csv
import os
from csv import DictWriter
import pandas as pd
from colorama import Fore
import datetime


def search_nom(nom):
    '''Recherche un joueur dans le fichier stats.csv, grâce à pandas'''
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")
    try:
        df = pd.read_csv(path_fichier)
        df = df[df['nom'] == nom]
        if not df.empty:
            return df.iloc[0].to_dict()
        else:
            return None
    except pd.errors.EmptyDataError:
        return None
    except FileNotFoundError:
        raise FileNotFoundError("Il n'y a pas de fichier stats.csv dans le dossier Data. Il faut donc le recréer.")


def crea_dico_dans_csv(dico_stats):
    from modules import GUI
    """Créé un fichier csv avec les stats d'un joueur"""
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")    # la path m'a l'air bonne
    with open(path_fichier, 'w', newline='') as write_obj:
        if search_nom(dico_stats['nom']) is not None:       # si le joueur est déjà dans le csv, on modifie ses stats
            search_nom(dico_stats['nom']).update(dico_stats)
        else:    # sinon, on crée une nouvelle ligne avec ses stats
            dict_writer = csv.DictWriter(write_obj, fieldnames=dico_stats.keys())
            # Vérifie si le fichier est vide
            if os.path.getsize(path_fichier) == 0:
                # Écrit l'en-tête pour la première fois
                dict_writer.writeheader()
            # Écris
            dict_writer.writerow(dico_stats)


def pres_stats_joueur(stats):
    data = {
        'Nom': [stats['nom']],
        'Nbr_sess': [stats['num_entree']],
        'Avg_tour/sess': [stats['nbr_tours_total'] / stats['num_entree']],
        'Avg_mise/tour': [stats['argent_total'] / stats['nbr_tours_total']],
        'Avg_Gain/tour': [stats['gain_total'] / stats['nbr_tours_total']],
        'Avg_depenses/sess': [stats['argent_total'] / stats['num_entree']],
        'Avg_Gain_sess': [stats['gain_total'] / stats['num_entree']],
        'Depenses_totales': [stats['argent_total']],
        'Gain_total': [stats['gain_total']],
        'Prem_entree': [stats['premiere_entree']]

    }
    df = pd.DataFrame(data)
    print("Voici les statistiques de", Fore.YELLOW + stats['nom'] + Fore.RESET, ":")
    max_key_len = max(len(key) for key in data.keys())
    for key, value in data.items():
        key_string = Fore.LIGHTBLUE_EX + key.ljust(max_key_len) + Fore.RESET
        value_string = Fore.YELLOW + str(value[0]) + Fore.RESET
        print(f"{key_string} | {value_string}")


#row = [re.sub(r"^'|'$", '', col) if re.match(r"^'.+'$", col) else float(col) for col in row]
def chiffres_casino():
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")
    with open(path_fichier, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = ['num_entree', 'nbr_tours_total', 'argent_total', 'gain_total', 'nbr_clients']

    return None


def pres_stats_casino(stats):
    return


def default():
    return {
        'nom': None,
        'num_entree': 0,
        'nbr_tours_total': 0,
        'argent_total': 0,
        'gain_total': 0,
        'premiere_entree': datetime.date.today()
    }
