
import json


class professeur:
    def __init__(self,n,p,a,s):
        self.tel=""
        self.prenom=p
        self.nom=n
        self.specialite=""
        self.anciennte=0
        self.statfamilial=""
        self.adresse=a
        self.salaire=s
        self.email=""
        self.datnaissance=""

    def calculersalairetotal(self):
        return self.salaire+(self.anciennte//5*2000)
    def todictr(self):
        discprof={"nom":self.nom,
                  "prenom":self.prenom,
                  "adresse":self.adresse,
                  "salaire":self.salaire,
                  "anciennte":self.anciennte,
                  "tel":self.tel,
                  "specialite":self.specialite,
                  "statfamilial":self.statfamilial,
                  "email":self.email,
                  "datnaissance":self.datnaissance}
        return discprof
    def fromdict(self,disct):
        p=professeur(disct["nom"],disct["prenom"],disct["adresse"],disct["salaire"])
        p.tel=disct["tel"]
        p.specialite=disct["specialite"]
        p.anciennte=disct["anciennte"]
        p.statfamilial=disct["statfamilial"]
        p.email=disct["email"]
        p.datnaissance=disct["datnaissance"]
        return p
        


    def enregistrer(self):
        with open("prof{self.nom}_{self.prenom}.json","w") as f:
            json.dump(self.todictr(),f)
        