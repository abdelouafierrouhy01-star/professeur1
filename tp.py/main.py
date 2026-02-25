from file1 import professeur

import json 
with open("professeur.json",mode="r",encoding="utf-8") as file:
    lista=json.load(file)
    listeprof=[]
    for dictp in lista:
       
       
        listeprof.append(professeur.fromdict(dictp))
       
       
        print("nombre de professeure est:",len(lista))
        print("le professeur 61 est:",listeprof[61].nom,"habite a",listeprof[61].adresse)



  


