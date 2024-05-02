from random import randint

#################################

def exemple_generateur():
    yield "a"
    yield "b"
    yield "c"

generateur = exemple_generateur()
print(type(generateur))
print(generateur.__next__())
print(generateur.__next__())    
print(generateur.__next__())           


#################################

def custom_range(n):
    for i in range(1, n + 1):
        yield i
        
res = custom_range(10)
for i in res:
    print(i)

#################################

def lettre_random(nom):
    nom_liste = list(nom)
    for i in range(len(nom)):
        rand_index = randint(0, len(nom_liste) - 1)
        yield nom_liste.pop(rand_index)
        
for l in lettre_random("Bonjour"):
    print(l)
    
str_recover = [l for l in lettre_random("Bonjour")]
    
nom_shuffle = "".join(str_recover)
print(nom_shuffle.capitalize())
