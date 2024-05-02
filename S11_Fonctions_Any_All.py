######################
# fonctions Any et All
# Any : permet de verifier si au moins une valeur d'un itérable est vraie
# All : permet de verifier si toutes les valeurs d'un itérable sont vraies

exemple_any = any([False, False, True, False])
print(exemple_any)

exemple_any = any([False, False, False, False])
print(exemple_any)

exemple_all = all([True, True, True, True])
print(exemple_all)

exemple_all = all([True, False, True, True])
print(exemple_all)

## AVEC Any
age_invites = [5, 15, 12, 16, 20, 17]

# En France
autorisation = any(age >= 18 for age in age_invites)
print(autorisation)

# Aux USA
autorisation = any(age >= 21 for age in age_invites)
print(autorisation)

# AVEC All
age_invites = [19, 20, 22, 41, 18, 25]
# En France
autorisation = all(age >= 18 for age in age_invites)
print(autorisation)

# Aux USA
autorisation = all(age >= 21 for age in age_invites)
print(autorisation)

####################################################
# Exercice 08 : Any et All
import os

fichiers = ["C:/dossier_test/fichier_01.jpg",
            "C:/dossier_test/fichier_02.tif",
            "C:/dossier_test/fichier_03.png",
            "C:/dossier_test/fichier_04.jpg",
            "C:/dossier_test/fichier_05.jpg"]

liste_temp = [os.path.splitext(f)[-1].replace(".", "") for f in fichiers]
# Any
liste_temp_1 = [True if f == "png" else False for f in liste_temp]
print(liste_temp_1)
au_moins_un_png = any(liste_temp_1)
print(au_moins_un_png)
# All
liste_temp_2 = [True if f == "jpg" else False for f in liste_temp]
print(liste_temp_2)
tous_des_jpg = all(liste_temp_2)
print(tous_des_jpg)

# Solution du formateur
au_moins_un_png = any(x.endswith('.png') for x in fichiers)
tous_des_jpg = all(x.endswith('.jpg') for x in fichiers)
