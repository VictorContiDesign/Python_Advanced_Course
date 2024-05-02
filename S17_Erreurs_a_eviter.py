####################################################
# Récupérer une clé inexistante dans un dictionnaire
dic = {
    'Pierre' : 'Serveur',
    'Julien' : 'Libraire',
    'Marie' : 'Ingénieur'
}

prenom = "Jaques"

profession = dic.get(prenom, f"{prenom} n'est pas dans le dictionnaire")
print(profession)

##########################################################
# Utiliser une liste vide comme argument dans une fonction
import random

def generateur_liste(liste=None):
    if liste is None:
        liste = []
    liste.extend([random.randint(1, 100) for i in range(5)])
    return liste
    
for i in range(5):
    print(generateur_liste())

#########################################    
# Mélanger les espaces et les tabulations
a = 18
if a >= 18:
    print("Bravo")
    print("Vous etes majeur")
else:
    print("Vous etes mineur")
    
####################################################
# Récupérer une clé inexistante dans un dictionnaire
liste = range(10)
index = 10

try:
    r = liste[index]
    print(r)
except IndexError:
    print(f"L'index {index} n'existe pas")
    
r = liste[index] if len(liste) > index else None
print(r)

######################################
# Modifier une liste en itérant dedans
prenoms = ["Pierre", "Julien", "Marie", "Paul"]

prenoms_nouvelle_liste = [p for p in prenoms if p != "Julien"]
print(prenoms_nouvelle_liste)

##################
# Copier une liste
liste = [1, 2, 3]

# Il faut etre sur que l'id en memoire est bien different

# 1ere maniere
liste_copie = liste[:]
liste.append(5)
print(liste)
print(liste_copie)

# 2eme maniere
liste_copie = list(liste)
liste.append(6)
print(liste)
print(liste_copie)

# 3eme maniere
liste_copie = liste.copy()
liste.append(7)
print(liste)
print(liste_copie)

#########################
# L'égalité avec is et ==
a = 5
b = 5

print(a == b)
# Juste fonctionnel de -5 a 256
print(a is b)
print(id(a))
print(id(b))

a = 2364
b = 2364

print(a == b)
print(a is b)
print(id(b))
print(id(b))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = [1, 2, 3, 4, 5]
b = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))

############################
# Utiliser des noms réservés
mon_objet = "voiture"
type_ = "Renault"

print(type(mon_objet))

############################
# from module import *
path = "C:/mon_fichier.txt"
# C'est une mauvaise idée d'importer directement tous les module d'un package
# car en déclarant des variables qui ont les memes noms que certains modules
# il y a un conflit. Tous les noms des modules sont inclus dans le namespace global.
from os import *
print(path)

######################
# Les erreurs de scope
variable = "Bonjour"

def ma_fonction():
    variable = "Salut"
    print(variable)
    
ma_fonction()
print(variable)