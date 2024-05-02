from random import randint

##########################

iterateur = iter("Udemy")

print(iterateur.__next__())
print(iterateur.__next__())
print(iterateur.__next__())
print(iterateur.__next__())
print(iterateur.__next__())

##########################

class custom_range:
    def __init__(self, maximum):
        self.i = 1
        self.maximum = maximum + 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.maximum:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
        
a = custom_range(10)
print(a.__next__())
print(a.__next__())
for i in a:
    print(i)
    
##########################
    
class lettre_random:
    def __init__(self, nom):
        self.i = 0
        self.max = len(nom)
        self.nom_restant = list(nom)
        
    def __iter__(self):
          return self
    
    def __next__(self):
        if self.i < self.max:
            lettre = self.nom_restant.pop(randint(0, len(self.nom_restant) - 1))
            self.i += 1
            return lettre
        else:
            raise StopIteration()
        
nom = "Bonjour"
nom_random = lettre_random(nom)
for l in nom_random:
    print(l)