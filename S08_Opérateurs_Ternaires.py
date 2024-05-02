# Maniere traditionnelle de le faire
def authorisation_age(age):
    if age >= 18:
        res = "Majeur"
    else:
        res ="Mineur"
    return res

res = authorisation_age(15)
print(res)
    
# Maniere avancee de le faire
def authorisation_age_ternaire(age):
    return "Majeur" if age >= 18 else "Mineur"

res = authorisation_age_ternaire(23)
print(res)

def authorisation_age_ternaire_print(age):
    print("Vous etes majeur") if age >= 18 else print("Vous etes mineur")

authorisation_age_ternaire_print(17)

# Exercice 06 : Opérateurs ternaires
"""En fonction de la valeur de la variable
âge, récupérer grâce à un operateur ternaire
si la personne est majeure ou non dans la variable
'majeur'.
Si la personne est majeur, la variable
contiendra la chaîne de caractère 'majeur'.
Si la personne est mineur, la variable
contiendra la chaîne de caractère 'mineur'"""
age = 17
majeur = print("majeur") if age>18 else print("mineur")


"""Récupérer dans la variable extension le mot 'python'
si le fichier déclaré dans la variable 'fichier' est de
type Python (extension .py). Si le fichier n'est pas
de type Python, retourner la chaîne de caractère 'invalide'"""
fichier = 'C:/Python/mon_script.py'
extension = "Python" if fichier.endswith(".py") else "invalide"
print('Le fichier {} est de type {}'.format(fichier, extension))
