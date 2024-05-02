liste = [-3, -2, -1, 0, 1, 2, 3]

###################################

res = [i for i in liste]
print(res)
# output : [-3, -2, -1, 0, 1, 2, 3]

res = [i*2 for i in liste]
print(res)
# output : [-6, -4, -2, 0, 2, 4, 6]

res = [i*2 for i in liste if i>0]
print(res)
# output : [2, 4, 6]

res = [i*2 if i>0 else i+1 for i in liste]
print(res)
# output : [-2, -1,  0, 1, 2, 4, 6]

# Exercice 05 : Comprehension de listes

#######################################
# 1ER EXEMPLE

# liste = [1, 2, 3, 4, 5]
# liste_double = []

# for i in liste:
#     liste_double.append(i * 2)

liste1 = [1, 2, 3, 4, 5]
liste_double1 = [i*2 for i in liste1]
print(liste_double1)

#######################################
# 2EME EXEMPLE

# liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# liste_double = []

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)

liste2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double2 = [i*2 for i in liste2]
print(liste_double2)

#######################################
# 3EME EXEMPLE

# liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# liste_double = []

# for i in liste:
#     if i > 0:
#         liste_double.append(i * 2)
#     else:
#         liste_double.append(i * 3)
        
liste3 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_double3 = [i*2 if i>0 else i*3 for i in liste3]
print(liste_double3)

#######################################
# 4EME EXEMPLE

# liste_finale = []
# for a in range(10):
#     for b in range(2):
#         liste_finale.append((a, b))

liste4 = [(a, b) for a in range(10) for b in range(2)]
print(liste4)