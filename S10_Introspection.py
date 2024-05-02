import random
import sys
import pprint
import os

###############
# fonction help

#help(random)
help(random.randint)

############
# module sys
# Permet d'inspecter le système d'exploitation et la version de Python qu'on utilise

print(sys.version)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.platform)
print(sys.path)
print(sys.getwindowsversion().major)
print(sys.executable)
print(sys.argv)

#help(sys)

##############
# fonction dir
# Permet d'instrospecter tous les attributs disponibles sur un objet

#pprint.pprint(dir(os))
#pprint.pprint(dir({}))
print([].append.__doc__)

###############
# fonction type

print(type(pprint))
print(type(pprint.pprint))
print(type(type))

#############
# fonction id

liste_originale = [1, 2, 3, 4]
liste_duplique_mauvaise = liste_originale

print(id(liste_originale))
print(id(liste_duplique_mauvaise))

liste_duplique_bonne = liste_originale[:]

print(id(liste_originale))
print(id(liste_duplique_bonne))

liste_originale.append(5)

print(liste_originale)
print(liste_duplique_mauvaise)
print(liste_duplique_bonne)