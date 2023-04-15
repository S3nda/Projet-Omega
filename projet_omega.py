import datetime
import random

def initialisation_roulette_solo() :
    date = datetime.datetime.now()          #affichage date et heure
    numero_partie =+ 1                      #le numéro de partie    
    
    nom_joueur = ""                                                                          #le nom du joueur
    while True:
        if len(nom_joueur) < 10 and " " not in nom_joueur and len(nom_joueur) > 0:
            break
        else :
            print("Vous devez mettre un bon nom")
            nom_joueur = input("Entrez votre nom ou pseudonyme s'il vous plaît : ") 
    
    mise_max = "54"
    tmp = False 
    while True :
        try:
            print("Veuillez mettre un nombre superieur a 0")
            mise_max = int(input("Mettez votre mise maximale que vous pouvez parier : "))
            if mise_max > 0:
               break
        except:
            pass

        liste_data_joueur = [mise_max,numero_partie,date,nom_joueur]
        return liste_data_joueur
            

            
    
    
def tour(liste_data_joueur):   
    mise_du_joueur = 0
    while True :
        try:
            print("Mettez une bonne mise!")
            mise_du_joueur = int(input("Entrez votre mise : "))
            if mise_du_joueur < liste_data_joueur[0] and mise_du_joueur > 0:
               break
        except:
            pass
            

    liste_de_pari = ["Pair","Impair","Rouge","Noir","Nombre"]
    pari = 0
    while True:
        if pari in liste_de_pari:
            break
        else:
            print("Choisissez un bon pari!")
            pari = input("Choisissez votre pari (Pair/Impair/Rouge/Noir/Nombre) : ")


    nombre_parier = "je"       
    if pari == "Nombre":
        while True:
            try:
                print("Salope")
                nombre_parier = int(input("Choisissez un nombre entre 0 et 36 : "))
                if 0 <= nombre_parier <= 36:
                    break
            except:
                pass
    liste_parier = [mise_du_joueur,pari,nombre_parier]
    return liste_parier




        
def roulette():
    liste_clean = []
    numero = [i for i in range(37)]
    for i in numero:
        variable_aleatoire = random.choice(["Noir","Rouge"])
        liste_clean.append([i,variable_aleatoire])
    liste_clean.append([0,"Vert"])
    
    
                          #élément allant dans le csv

    numero_aleatoire = random.randint(1,36)
    couleur_numero = liste_clean[numero_aleatoire][1]
    

    print(f"C'est le numéro {numero_aleatoire} et la couleur {couleur_numero}")
    liste_resultat = [numero_aleatoire,couleur_numero]
    return liste_resultat


def conclusion_roulette_solo(liste_data,liste_pari,liste_resultat):
    if liste_pari[2] == liste_resultat[0]:                         #pour si resultat correcte pour nombre pile
        print(f"Vous avez gagné! 🏆🏆 Vous avez donc gagnez {liste_data[0] * 36} €")
        mise_max = mise_max + liste_pari[0] * 35
        print(f"Il vous reste {mise_max} €")


    elif liste_resultat[1] == liste_pari[1]:                                                #pour si resultat correcte pour couleur
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = mise_max + liste_pari[0]   
        print(f"Il vous reste {mise_max} €")                                         


    elif numero_aleatoire//2 == 0 and pari == "Pair" :                                          #pour si resultat correcte pour parité du nombre
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = mise_max + liste_pari[0]
        print(f"Il vous reste {mise_max} €")


    elif numero_aleatoire//2 == 1 and pari == "Impair":
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 2} €")
        mise_max = mise_max + liste_pari[0]
        print(f"Il vous reste {mise_max} €")
    
    elif numero_aleatoire == 0 and not nombre_parier == numero_aleatoire:
        print(f"Vous avez gagné! 🏆🏆 Vous gagnez donc {liste_data[0] * 1.5} €")
        mise_max = mise_max + liste_pari[0]
        print(f"Il vous reste {mise_max} €")

    else:                                                #pour s'il a faux
        print(f"Dommage! Vous avez perdu 😭😭. Vous avez donc perdu {liste_data[0]}")
        mise_max = mise_max - liste_pari[0]
        print(f"Il vous reste {mise_max} €")




    nouvelle_partie = input("Voulez-vous rejouer un partie(y/n) : ")
    if nouvelle_partie == "y":
        print("C'est reparti pour ...")
        roulette_solo(mise_max)
    else:
        print("Dommage vous avez potentiellement perdu beaucoup d'argent")
        
        





def roulette_solo():
    liste_data =initialisation_roulette_solo()
    liste_pari = tour(liste_data)
    liste_resultat = roulette()
    conclusion_roulette_solo(liste_data,liste_pari,liste_resultat)


roulette_solo()