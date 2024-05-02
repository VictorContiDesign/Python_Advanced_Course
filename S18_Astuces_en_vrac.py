##################################
# Trouver le chemin vers un module

import os

print(os.__file__)

print(__file__)
dossier_courant = os.path.dirname(__file__)
print(dossier_courant)

##################
# La fonction join

tags_photo = ["vacances", "italie", "juin", "2018", None]

nom_fichier = "_".join(filter(None,tags_photo))
print(nom_fichier)

nom_fichier = "_".join([i for i in tags_photo if i])
print(nom_fichier)

##########################
# Chainer les comparateurs

nombre = 25
if 1 < nombre < 50:
    print("Le nombre est compris entre 1 et 50")

##########
# For else

invites = ["Julien", "Marie", "Pierre", "Pascal"]
for invite in invites:
    if invite == "Pascal":
        print("Pascal a deja ete invite !")
        break
else:
    print("Pascal n'a pas ete invite")
    
####################################################
# Inverser les clés et les valeurs d'un dictionnaire

from pprint import pprint
LONG_NAMES = {
    "anm_snc" : "Animation Scene",
    "anm_out" : "Animation Publish",
    "sim_snc" : "Simulation Scene",
    "sim_out" : "Animation Publish",    
}

pprint(list(zip(LONG_NAMES.values(), LONG_NAMES.keys())))

SHORT_NAMES = dict((zip(LONG_NAMES.values(), LONG_NAMES.keys())))

pprint(SHORT_NAMES)

print(LONG_NAMES.get("anm_snc"))
print(SHORT_NAMES.get("Animation Scene"))

###########################################
# Aplatir une liste et enlever les doublons

ma_liste = [[1, 7, 3], [3, 4], [12, 1, 4, 8], [1, 3, 3]]
ma_liste_applatie = sum(ma_liste, [])
print(ma_liste_applatie)

ma_liste_sans_doublons = sorted(list(set(ma_liste_applatie)))
print(ma_liste_sans_doublons)

#######################################
# Enlever certains éléments d'une liste

prenom = "Pierre"
nom = "Dupont"
id_membre = "142352"

liste = [id_membre, nom, prenom]
nom_complet = "_".join(liste)
print(nom_complet)

prenom = "Pierre"
nom = "Dupont"
id_membre = None

liste = filter(None, [id_membre, nom, prenom])
liste = [e for e in [id_membre, nom, prenom] if e]
nom_complet = "_".join(liste)
print(nom_complet)

#############################################
# utiliser les defaultdict et les OrderedDict

from collections import defaultdict, OrderedDict

mot = "anticonstitutiellement"

d = {}
for lettre in mot:
    if not d.get(lettre):
        d[lettre] = 1
    else:
        d[lettre] += 1
    
print(d.items())

# Le defaultdict permet d'initialiser la clé d'un dictionnaire avec une valeur
# par défaut si celle-ci n'existe pas
d = defaultdict(int)
for lettre in mot:
    d[lettre] += 1
    
print(d.items())

mon_dict = OrderedDict()
#mon_dict = {}

mon_dict["Un"] = "Pierre"
mon_dict["Deux"] = "Paul"
mon_dict["Trois"] = "Marie"
mon_dict["Quatres"] = "Jacques"
mon_dict["Cinq"] = "Julie"

print(mon_dict.items())

####################################
# Pretty Print avec le module pprint

from pprint import pprint

mon_dict = {"prenom" : "Victor", 
            "nom" : "Conti", 
            "age" : 35, 
            "adresse" : "Hipolito Yrigoyen 1045",
            "telephone" : [{"type" : "mobil",
                            "loc" : "France",
                            "numero" : "+33617843605"},
                           {"type" : "mobil", 
                            "loc" : "Argentine", 
                            "numero" : "+5491124022891"}]
            }

print(mon_dict)
print("="*100)
pprint(mon_dict, indent=4)

###########################################
# Utilisation avancée de la fonction format

text = "{} {}".format("Pierre", "Dupont")
print(text)

text = "{0} {1}".format("Pierre", "Dupont")
print(text)

text = "{1} {0}".format("Pierre", "Dupont")
print(text)

text = "{0} {0}".format("Pierre", "Dupont")
print(text)

text = "{} a {} ans".format("Pierre", 18)
print(text)

text = "{:10} {}".format("Debut", "Fin")
print(text)

text = "{:>10} {}".format("Debut", "Fin")
print(text)

text = "{} {:=>10}".format("Debut", " Fin")
print(text)

text = "{:+^25}".format(" Partie 01 ")
print(text)

text = "{:+^50}".format(" Partie 01 ")
print(text)

text = "{:.3}".format("Pierre")
print(text)

text = "{:.3}".format(2.51458)
print(text)

user = {"prenom" : "Pierre", "nom" : "Dupont"}
text = "Bonjour, je m'appelle {d[prenom]} {d[nom]}".format(d=user)
print(text)

class MaVoiture(object):
    def __init__(self):
        self.couleur = "Rouge"
        self.marque = "Mercedes"
        
text = "J'ai une {o.marque} de couleur {o.couleur}".format(o=MaVoiture())
print(text)

#################################
# La fonction print avec python 3

rangees = [1, None, 3, 4, 5, 12, 4, 3, 8]

print(*rangees, sep=" - ")

############################
# Eviter trop de tabulations

# Mauvaise maniere de faire
def verifier_fichier(fichier):
    if fichier.endswith(".py"):
        if len(fichier) > 3:
            if fichier.startswith("C:/"):
                return True
    return False

print(verifier_fichier("C:/mon_programme/test.py"))

# Bonne maniere de faire
def verifier_fichier(fichier):
    if fichier.startswith("C:/") and fichier.endswith(".py") and len(fichier) > 3:
        return True
    return False

print(verifier_fichier("C:/mon_programme/test.py"))

# Mauvaise maniere de faire
def recuperer_extension(fichier):
    if fichier.startswith("C:/"):
        fichier, extension = os.path.splitext(fichier)
        extension = extension.replace(".", "")
        return extension

    return None

print(recuperer_extension("C:/mon_programme/test.py"))

# Bonne maniere de faire
def recuperer_extension(fichier):
    if not fichier.startswith("C:/"):
        return None
    fichier, extension = os.path.splitext(fichier)
    extension = extension.replace(".", "")
    return extension

print(recuperer_extension("C:/mon_programme/test.py"))