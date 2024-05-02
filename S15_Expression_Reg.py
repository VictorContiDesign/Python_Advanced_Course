import re

# ^[0]{1}[1-7]{1}(-[0-9]{2}){4}$
# 06-81-52-45-32

# .             Le point correspond a tous les caractères possibles (incluant symboles)
# [A-F]         Correspond a une liste de caractères possibles
# (python|c++)  L'un ou l'autre
# ^             Le contraitre de ce qu'on veut
# \d            Uniquement des chiffres. Equivalent a [0-9]
# \D            Tout sauf des chiffres. Equivalent a [^0-9]
# \s            Un espace
# \w            Un caracteres alphanumérique. Equivalent a [a-zA-Z0-9_]
# \W            Tout sauf un caractere alphanumerique. Equivalent a [^a-zA-Z0-9_]
# \             Comme en Python, pour echapper un caractere.

# ?             0 ou 1 fois
# *             0 a l'infini
# +             de 1 a l'infini
# {3}           Exactement 3
# {3,}          de 3 a l'infini
# {,3}          de 0 a 3 fois
# {3,6}         de 3 fois a 6 fois

##################################################################################
# La fonction match

# Pourquoi on met un 'r'
# print('\tBonjour')
# print(r'\tBonjour')

# On cherche le caractere indiqué depuis le début de la chaine de caracteres
# a = re.match(r'.+', 'Pierre Dupont')
# print(a.group())

# a = re.match(r'(\w+)(\s)(\w+)', 'Pierre Dupont')
# print(a.group(0))
# print(a.group(1))
# print(a.group(2))
# print(a.group(3))

# a = re.match(r'(?P<prenom>\w+) (?P<nom>\w+)', 'Pierre Dupont')
# print(a.group("prenom"))
# print(a.group("nom"))

# print(a.groups())
# print(a.groupdict())

#################################
# Exercice 12 : la fonction match

# Pour chaque question, indiquez si le match est valide ou non et ce qu'il retourne.

# a = re.match(r'[a-z]+\d{2}', 'item01')
# print(a.group(0))
# ✅Valide ; output : item01

# a = re.match(r'[a-zA-Z]+\s\w+', 'Pierre Dupont')
# print(a.group(0))
# ✅Valide ; output : Pierre Dupont

# a = re.match(r'\s+', 'pierre dupont')
# print(a.group(0))
# ❎ NON Valide

# a = re.match(r'\w+', 'pierre dupont')
# print(a.group(0))
# ✅Valide ; output : pierre

# a = re.match(r'\w+([-+=]?)', 'pierre-dupont')
# print(a.group(0))
# ✅Valide ; output : pierre-

# a = re.match(r'\w+([-+=]?)', 'pierre/dupont')
# print(a.group(0))
# ✅Valide ; output : pierre

# a = re.match(r'\w+([-+=]+)', 'pierre/dupont')
# print(a.group(0))
# ❎ NON Valide

##################################################################################
# La fonction search

# On cherche dans l'entiereté de la chaine de charactères l'expression qu'on lui indique

# a = re.search(r'\+', 'Pierre Dupont + Paul Martin')
# print(a)

##################################################################################
# La fonction split

# On peut spécifier une expression régulière a la place d'un simple caractère

# texte = "item01 | item02 - item03 - item04 | item05"

# a = re.split(r' \| | - ', texte)
# print(a)

#############################################################
# Exercice 13 : Vérifier la validité d'un numéro de téléphone

numeros_de_telephone = ['06-71-45-34-23',
						'02-12-33-75-12',
						'00-23-14-52-44',
						'514-235-0293',
						'03-52-31-56-34']

for i in range(len(numeros_de_telephone)):
    a = re.match(r'[0]{1}[1-7]{1}(-[0-9]{2}){4}', numeros_de_telephone[i])
    if a != None:
        print(f"Le numéro {numeros_de_telephone[i]} est valide")
    else:
        print(f"Le numéro {numeros_de_telephone[i]} est invalide")

# Le numéro 06-71-45-34-23 est valide
# Le numéro 02-12-33-75-12 est valide
# Le numéro 00-23-14-52-44 est invalide
# Le numéro 514-235-0293 est invalide
# Le numéro 03-52-31-56-34 est valide

########################################################
# Exercice 14 : Vérifier la validité d'une addresse mail

adresses_mail = ['christian_martin@gmail.com',
				 'JaiOublieLarobasegmail.com',
				 'MarieHutchinson03523@yahoo.co.uk',
				 'UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com',
				 'ceciNestPasUneDresseMail']

for i in range(len(adresses_mail)):
    a = re.search(r'.+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+', adresses_mail[i])
    if a != None:
        print(f"L'addresse mail {adresses_mail[i]} est valide")
    else:
        print(f"L'addresse mail {adresses_mail[i]} est invalide")

# L'adresse christian_martin@gmail.com est valide
# L'adresse JaiOublieLarobasegmail.com est invalide
# L'adresse MarieHutchinson03523@yahoo.co.uk est valide
# L'adresse UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com est valide
# L'adresse ceciNestPasUneDresseMail est invalide

