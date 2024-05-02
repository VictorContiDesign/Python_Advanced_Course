# Les éléments d'un set sont uniques et immuables
# Le set en tant que tel est immuable
# Le set supprime automatiquement les éléments repetés
# Les éléments du set en tant que tel ne sont pas ordonnés

mon_set = {1, 2, 3, 3, "Julien", "Julien", (255, 0, 0), (255, 0, 0)}
print(mon_set)
mon_set.add(5)
print(mon_set)
mon_set.update(["Pierre", 6])
print(mon_set)
# mon_set.remove("Julien")
# mon_set.remove("Jules")
mon_set.discard("Julien")
mon_set.discard("Jules")
print(mon_set)

# On peut utiliser un set pour filter une liste avec des éléments en double

liste = [99, 1, 2, 4, 5, 6, 7, 5, 4, 1, 3, 2, 1, 1, 2, 1, 34, 20]
liste = set(liste)
liste = list(liste)
liste = sorted(liste)
print(liste)

# Opération sur les sets : unions, intérsections, différences simples, différences symétriques

# Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
print(a | b)
# output : {1, 2, 3, 4, 5, 6}

# Intérsections
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))
print(a & b)
# output : {3, 4}

# Différences simple
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))
print(a - b)
print(b - a)
# output : {1, 2}
# output : {5, 6}

# # Différences symétrique : On prend l'union moins l'intérsection
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.symmetric_difference(b))
print(a ^ b)
# output : {1, 2, 5, 6}

########################
# Exercice 10 : Les sets

import os

cur_dir = os.path.dirname(__file__)
print(cur_dir)

dossier_rendu_01 = os.path.join(cur_dir, "rendus_01")
if not os.path.exists(dossier_rendu_01):
    os.makedirs(dossier_rendu_01)
    for i in range(101):
        with open("rendus_01/" + f"{i}".zfill(3) + ".jpg", "x") as file:
            pass
fichiers_01 = os.listdir(dossier_rendu_01)
fichiers_01 = set(fichiers_01)
print(len(fichiers_01))


dossier_rendu_02 = os.path.join(cur_dir, "rendus_02")
if not os.path.exists(dossier_rendu_02):
    os.makedirs(dossier_rendu_02)
    for i in range(101):
        with open("rendus_02/" + f"{i}".zfill(3) + ".jpg", "x") as file:
            pass
fichiers_02 = os.listdir(dossier_rendu_02)
fichiers_02 = set(fichiers_02)

fichiers_presentes = fichiers_01 | fichiers_02

fichier_complete = set([f"{i}".zfill(3) + ".jpg" for i in range(101)])

fichier_manquant = fichier_complete - fichiers_presentes
print(f"Entre les deux répértoire il y a {len(fichier_manquant)} fichiers manquant : ")
fichier_manquant = list(fichier_manquant)
fichier_manquant.sort()
for i in fichier_manquant:
    print(i)
    