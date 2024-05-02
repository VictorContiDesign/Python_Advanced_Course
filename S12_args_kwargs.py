import os

def addition(*args):
    print(args)
    return sum(args)

print(addition(5,5,8))

##################################################

def liste_invites_1(invite_vip, *args):
    print(f"{invite_vip} est un VIP")
    for invite in args:
        print(f"{invite} est un invité normal")

liste_invites_1("Paul", "Pierre", "Marie", "Max")

##################################################

def liste_invites_2(invite_vip, *args, **kwargs):
    print(f"{invite_vip} est un VIP")
    for invite in args:
        print(f"{invite} est un invité normal")
        
    indesirables = kwargs.get("indesirables")
    if indesirables:
        print(f"Ces invités sont indésirables: {', '.join(indesirables)}")

liste_invites_2("Paul", "Pierre", "Marie", "Max", indesirables=["Simon", "Jean","Julie"])

##################################################

def chemin(dossier, fichier, extension='txt'):
    return os.path.join(dossier, f"{fichier}.{extension}")

print(chemin(r"C:\users\victorc","formation"))

data = {"dossier" : r"C:\users\victorc", "fichier" : "formation", "extension" : "py"}
print(chemin(**data))

data = {"dossier" : r"C:\users\victorc", "fichier" : "formation"}
print(chemin(**data))

###################
# Exercice 9 : Args

def concatenation_chemin(*args):
    new_path = ""
    for i in args:
        if args.index(i) == 0:
            new_path += i
        else:
            if new_path.endswith('/'):
                new_path += i
            else:
                new_path += f"/{i}"
    return new_path

print(concatenation_chemin("C:/users/victorc/", "formation_python/", "fichier.txt"))