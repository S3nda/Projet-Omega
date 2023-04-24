def crea_csv(Dico):
    csv=open("fichier.csv","w")
    liste_cles=list(Dico.keys())
    csv.write(liste_cles[0]+";"+liste_cles[1]+";"+liste_cles[2]+";"+liste_cles[3]+";"+liste_cles[4]+";"+liste_cles[5]+"\n")
    csv.close()

def CSV(Dico):
    csv=open("fichier.csv","a")
    liste_cles=list(Dico.keys())
    for i in range(len(liste_cles)-1):
        csv.write(str(Dico[liste_cles[i]])+";")
    csv.write(str(Dico[liste_cles[-1]])+"\n")
    csv.close()
    return csv


def Dico(nom):
    csv=open("fichier.csv","r")
    descripteurs=csv.readline().rstrip().split(";")
    liste_csv=[]
    for ligne in csv.readlines():
        liste_csv.append(ligne.rstrip().split(";"))
    for joueur in liste_csv:
        if joueur[0]==nom:
            Dico_joueur={}
            for i in range(len(descripteurs)):
                Dico_joueur[descripteurs[i]]=joueur[i]
        return Dico_joueur


















Dict={"1":"5","2":"9","3":"pp","4":"glou","5":"ut","6":"mais"}
crea_csv(Dict)
CSV(Dict)
print(Dico("5"))