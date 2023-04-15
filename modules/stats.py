import os
import csv



def solo():
    return


def multi():
    return


def csv_writer(file_path, dico):
    file = file_path + '\\' + 'stats.csv'
    with open(file, mode='w', newline='') as fichier_csv:
        # Créer un objet "writer" CSV
        writer = csv.writer(fichier_csv, delimiter=';')

        # Écrire les noms des colonnes dans la première ligne
        writer.writerow(dico.keys())

        # Écrire les données dans le tableau
        for row in zip(*dico.values()):
            writer.writerow(row)
# fonction pratique implémentée pour le menu STATISTIQUES ✅


def convert_to_csv(dico):
    """Convertit le dictionnaire en fichier CSV"""
    file_path = os.path.join(os.getcwd(), 'Data')   # Récupérer le chemin du dossier Data
    file = file_path + '\\' + 'stats.csv'
    # Récupérer le chemin du fichier CSV
    # Vérifier si le fichier CSV existe déjà
    while True:
        if os.path.isfile(file):
            # Si le fichier existe, demander à l'utilisateur s'il veut l'écraser
            response = input(f'Le fichier {file} existe déjà. Voulez-vous l\'écraser ? (o/n) ')
            if str(response.lower()) == 'n':  # Si l'utilisateur ne veut pas écraser le fichier, annuler l'opération
                print('Opération annulée.')
                break
            elif str(response.lower()) == 'o':  # Si l'utilisateur veut écraser le fichier, écraser le fichier
                csv_writer(file_path, dico)
                print(f'Le fichier CSV {file} a été créé avec succès !')
                break
            else:  # Si l'utilisateur ne saisit pas "o" ou "n", annuler l'opération
                print('Erreur de saisie, vous devez saisir "o" ou "n".')
                continue
        else:
            # Si le fichier n'existe pas, le créer
            csv_writer(file_path, dico)
            print(f'Le fichier CSV {file} a été créé avec succès !')
            break
    return
# fonction pratique implémentée pour le menu STATISTIQUES ✅