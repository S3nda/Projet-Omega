import csv
import os
import pandas as pd
from colorama import Fore
import datetime


def search_nom(nom):
    from modules import GUI
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")
    try:
        dataframe = pd.read_csv(path_fichier)
        dataframe = dataframe[dataframe['nom'] == nom]
        if not dataframe.empty:
            GUI.attend()
            return dataframe.iloc[0].to_dict()
        else:
            return None
    except pd.errors.EmptyDataError:
        GUI.attend(0.5)
        return None
    except FileNotFoundError:
        raise FileNotFoundError("Il n'y a pas de fichier stats.csv dans le dossier Data. Il faut donc le recréer.")


def crea_dico_dans_csv(dico_stats):
    if "nom" not in dico_stats:
        raise ValueError("Le dictionnaire passé en paramètre ne contient pas de clé 'nom'")
    """Créé un fichier csv avec les stats d'un joueur"""
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")
    dico_trouve = search_nom(dico_stats['nom'])
    if dico_trouve is not None:
        dataframe = pd.read_csv(path_fichier)
        index = dataframe.index[dataframe['nom'] == dico_stats['nom']].tolist()[0]
        dataframe.loc[index] = dico_stats
        dataframe.to_csv(path_fichier, index=False)
    else:
        with open(path_fichier, 'a+', newline='') as write_obj:     # sinon, on crée une nouvelle ligne avec ses stats
            dict_writer = csv.DictWriter(write_obj, fieldnames=dico_stats.keys())
            if os.path.getsize(path_fichier) == 0:
                dict_writer.writeheader()   # on écrit les headers si le fichier est vide
            dict_writer.writerow(dico_stats)


def pres_stats_joueur(stats):
    data = {
        'Nom': [stats['nom']],
        'Nbr_sess': [stats['num_entree'], "sessions"],
        'Nbr_tours_total': [stats['nbr_tours_total'], "tours"],
        'Avg_tour/sess': [stats['nbr_tours_total'] / stats['num_entree'], "tours"],
        'Avg_mise/tour': [stats['argent_total'] / stats['nbr_tours_total'], "€"],
        'Avg_Gain/tour': [stats['gain_total'] / stats['nbr_tours_total'], "€"],
        'Avg_depenses/sess': [stats['argent_total'] / stats['num_entree'], "€"],
        'Avg_Gain_sess': [stats['gain_total'] / stats['num_entree'], "€"],
        'Depenses_totales': [stats['argent_total'], "€"],
        'Gain_total': [stats['gain_total'], "€"],
        '%_Gain': [str(abs(stats['gain_total'] / stats['argent_total'] * 100)), "%"],
        'Prem_entree': [stats['premiere_entree'], "UTC"]

    }

    print("Voici les statistiques de", Fore.YELLOW + stats['nom'] + Fore.RESET, ":")
    max_key_len = max(len(key) for key in data.keys())
    for key, value in data.items():
        key_string = Fore.LIGHTBLUE_EX + key.ljust(max_key_len) + Fore.RESET
        value_string = Fore.YELLOW + str(value[0]) + Fore.RESET
        print(f"{key_string} | {value_string}")


def stats_casino():
    path_fichier = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Data", "stats.csv")
    try:
        dataframe = pd.read_csv(path_fichier)
        nb_joueurs = len(dataframe["nom"].unique())
        nb_sessions = dataframe["num_entree"].sum()
        chiffre_affaire = dataframe["argent_total"].sum()
        gains_totaux = (dataframe["gain_total"].sum())
        nbr_tours = (dataframe["nbr_tours_total"].sum())
        return {
            "Nombre de joueurs uniques": nb_joueurs,
            "Nombre de sessions": nb_sessions,
            "Chiffre d'affaire": chiffre_affaire,
            "Gains_totaux": gains_totaux,
            "Nombre de tours": nbr_tours
        }
    except pd.errors.EmptyDataError:
        print("Il n'y a pas de statistiques à afficher.\n"
              "Il faut croire que personne n'a encore joué :(")
        return None
    except FileNotFoundError:
        raise FileNotFoundError("Il n'y a pas de fichier stats.csv dans le dossier Data. Il faut donc le recréer.")


def pres_stats_casino(stats):
    data = {
        'Nbr_jrs': [stats['Nombre de joueurs uniques']],
        'Nbr_sess': [stats['Nombre de sessions'], "sessions"],
        'Avg_dep_joueur': [stats['Chiffre d\'affaire'] / stats['Nombre de joueurs uniques'], "€"],
        'Avg_gain_joueur': [stats['Gains_totaux'] / stats['Nombre de joueurs uniques'], "€"],
        'Avg_tours_sess': [stats['Nombre de tours'] / stats['Nombre de sessions'], "tours"],
        'Avg_dep_sess': [stats['Chiffre d\'affaire'] / stats['Nombre de sessions'], "€"],
        'Avg_gain_sess': [stats['Gains_totaux'] / stats['Nombre de sessions'], "€"],
        'Avg_mise_tour': [stats['Chiffre d\'affaire'] / stats['Nombre de tours'], "€"],
        'Avg_gain_tour': [stats['Gains_totaux'] / stats['Nombre de tours'], "€"],
        'Chiffre_affaire': [stats['Chiffre d\'affaire'], "€"],
        'Bénéfices': [-stats["Gains_totaux"], "€"]
    }

    print("Voici les statistiques du casino :")
    max_key_len = max(len(key) for key in data.keys())
    for key, value in data.items():
        key_string = Fore.LIGHTBLUE_EX + key.ljust(max_key_len) + Fore.RESET
        value_string = Fore.YELLOW + str(value[0]) + Fore.RESET
        print(f"{key_string} | {value_string}")


def default():
    return {
        'nom': None,
        'num_entree': 0,
        'nbr_tours_total': 0,
        'argent_total': 0,
        'gain_total': 0,
        'premiere_entree': datetime.date.today()
    }
