#premiere partie :

class Personne(object):
    def __init__(self,numeroRue,numeroTel,nom='',prenom='',nomRue='',codePostal='',ville=''):
        self.numero=numeroRue
        self.numeroTel=numeroTel
        self.nom=nom
        self.prenom=prenom
        self.nomRue=nomRue
        self.codePostal=codePostal
        self.ville=ville

    def afficher(self):
        print("Nom : ", self.nom)
        print("Prenom : ", self.prenom)
        print("Numero de la rue : ", self.numeroRue)
        print("Nom rue : ",self.nomRue)
        print("Numero de telephone ", self.numeroTel)
        print("Code Postal ", self.codePostal)
        print("Ville : ", self.ville)
        
annuaire=[Personne]

#fonction de saisie pour le remplissage du tableau
def saisie_tab():
    name=input("Saisissez le nom :")
    Sname=input("Saisissez le prenom :")
    Pnumner=input("saisissez le numéro de téléphone :")
    Nrue=input("Saisissez le nom de la rue :")
    NumRue=input("Saisissez le numero de la rue :")
    CodeP=input("Saisissez le code postale :")
    Ville=input("Saisissez la ville :")

    unePersonne= Personne(NumRue,Pnumner,name,Sname,Nrue,CodeP,Ville)

    return unePersonne
    
#fonction critere de recherche
def critere_recherche():
    print("Quel est votre critere de recherche ?")
    print("1(nom)")
    print("2(prenom)")
    print("3(nomRue)")
    print("4(numeroTel)")
    print("5(codePostal)")
    print("6(ville)")
    choix=input()

    return choix

#fonction de recherche 
def recherche(annuaire,critere):
    valeurRecherche=input("Donner la valeur de recherche :")
    tabBool=[]
     #lower permet de mettre les valeurs ajoutes en miniscule

    if critere.lower() == "nom":
        for x in annuaire:
            if x.nom.lower()== valeurRecherche.lower():
                return tabBool.append(x)
    elif critere.lower() == "prenom":
        for x in annuaire:
            if x.prenom.lower()== valeurRecherche.lower():
                return tabBool.append(x)
    elif critere.lower() == "nomRue":
        for x in annuaire:
            if x.nomRue.lower()== valeurRecherche.lower():
                return tabBool.append(x)
    elif critere.lower() == "numeroTel":
        for x in annuaire:
            if x.numeroTel.lower()== valeurRecherche.lower():
                return tabBool.append(x)
    elif critere.lower() == "codePostal":
        for x in annuaire:
            if x.codePostal.lower()== valeurRecherche.lower():
                return tabBool.append(x)
    elif critere.lower() == "ville":
        for x in annuaire:
            if x.ville.lower()== valeurRecherche.lower():
                return tabBool.append(x)

#fonction d'affichage
def affichage(tableauRecherche):
    for i in tableauRecherche:
        i.afficher()

#compilation
annuaireFinal=[Personne]
nbr=input("Combien de personne souhaitez-vous ajouter ? :")
for i in range(0,nbr):
    annuaireFinal.append(saisie_tab())
    
critere=critere_recherche()
tableauRecherche=recherche(annuaireFinal,critere)
affichage(tableauRecherche)