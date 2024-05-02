# Maniere traditionelle de le faire
liste = ["Bonjour", "tout", "le", "monde"]
for i in range(len(liste)):
    if i > 0:
        print(liste[i])
        
# Maniere avancee de le faire
liste = ["Bonjour", "tout", "le", "monde"]
for i, mot in enumerate(liste, 1):
    print(i, mot)

dic = { "User1" : "John",
        "User2" : "Peter",
        "User3" : "Julie",}

for i, (cle, valeur) in enumerate(dic.items(), 1):
    print(i, cle, valeur)
    
# Exercice 02 : Convertir une phrase en camelCase
phrase = 'Phrase en camel case'
mots = phrase.lower().split(' ')
phrase_convertie = mots[0]
for i, mot in enumerate(mots):
    if i > 0:
        phrase_convertie += mot.capitalize()
print(phrase_convertie)