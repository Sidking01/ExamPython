import random

class Personne:
    def __init__(self, nomPersonne):
        self.nomPersonne = nomPersonne
        self.annee = None
        self.temps = None

def saisiePersonne():
    tab = []
    while True:
        nomPersonne = input("Entrez le nom de la personne ou q  si vous voulez quittez : ")
        if nomPersonne == 'n':
            break
        personne = Personne(nomPersonne)
        tab.append(personne)
    return tab

def calculAnnee(tab, annee_min, annee_max):
    for personne in tab:
        print(f"{personne.nomPersonne}, choissisez une période ?")
        print(f"choisissez entre {annee_min} et {annee_max} : ")
        annee_depart = int(input())
        personne.annee = random.randint(annee_depart, annee_max)

def calculTemps(tab):
    anneeActuelle = 2017
    anneeSaut = 10
    tempsSaut = 10
    for personne in tab:
        personne.temps = (personne.annee - anneeActuelle) * (tempsSaut / anneeSaut)

def programme():
    t = saisiePersonne()
    calculAnnee(t, -10000, 10000)
    calculTemps(t)

    for personne in t:
        print(f"Nom : {personne.nom}")
        print(f"Annee : {personne.annee}")
        print(f"Temps : {personne.temps} secondes")

    print("Prendrez-vous ce risque ?")

programme()
