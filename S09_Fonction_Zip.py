liste_01 = [1, 2, 3, 4]
liste_02 = ["un", "deux", "trois"]

combinaison = list(zip(liste_01, liste_02))
print(combinaison)

# Exercice 07 : La fonction zip

from string import ascii_lowercase

# Variables Globales
liste_ascii_lowercase = list(ascii_lowercase)
liste_index_ascii = []
prenom = "Astrid"

# Fonctions
for i, lettre in enumerate(liste_ascii_lowercase, 1):
    liste_index_ascii.append(i)

zip_package = list(zip(liste_index_ascii, liste_ascii_lowercase))

for i in prenom:
    for j in zip_package:
        if i.lower() == j[1]:
            print(f"{i} -> {j[0]}")