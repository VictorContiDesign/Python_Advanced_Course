import os
from PySide2 import QtWidgets, QtCore

# Maniere traditionelle de le faire
def multiplication(a, b):
    return a * b

resultat = multiplication(5, 10)
print(resultat)

def print_bonjour():
    print("Bonjour")
    
print_bonjour()

# Maniere avancee de le faire
multiplication = lambda a, b: a * b
resultat = multiplication(5, 10)
print(resultat)

print_bonjour = lambda: print("Bonjour")
print_bonjour()

print_mot = lambda m: print(m)
print_mot("Python")

fichiers = ["C:/Users/victorc/Documents/Python_Avanzado/S3_Enumerate.txt",
            "C:/Users/victorc/Documents/Python_Avanzado/S4_Fonctions_Anonymes.py",
            "C:/Users/victorc/Documents/Python_Avanzado/S4_Comprehension_Liste.cs"]

get_fichier = lambda f: os.path.split(f)[-1]
get_ext = lambda f: os.path.splitext(f)[-1]
del_point = lambda f: f.replace(".", "")
process = lambda f: del_point(get_ext(get_fichier(f)))

liste_extensions = [process(f) for f in fichiers]
print(liste_extensions)

users = [("User1" , "John"),
         ("User2" , "Peter"),
         ("User3" , "Julie"),]

users.sort(key=lambda x: x[1])
print(users)

# Exercice 03 : Fonctions lambda avec PySide2 - 01
"""
Le but de l'exercice est d'afficher le mot 'Bonjour'
a l'aide de la methode 'afficher_mot' quand on clique sur
le bouton 'Print Bonjour!' et d'afficher 'Au revoir' quand
on clique sur le bouton 'Print Au Revoir!'
"""

from PySide2 import QtWidgets, QtCore

#class MainUi(QtGui.QWidget):
class MainUi(QtWidgets.QWidget):
    def __init__(self):
        super(MainUi, self).__init__()
        
        self.setWindowTitle('Printer')

        main_layout = QtWidgets.QHBoxLayout(self)
        button = QtWidgets.QPushButton('Print Bonjour!')
        button2 = QtWidgets.QPushButton('Print Au revoir!')
        main_layout.addWidget(button)
        main_layout.addWidget(button2)

        button.clicked.connect(lambda f: print("Bonjour"))
        button2.clicked.connect(lambda f: print("Au revoir"))

#   def afficher_mot(self, mot):
#       print(mot)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MainUi()
    win.show()
    app.exec_()

# Exercice 04 : Fonctions lambda avec PySide2 - 02
"""
Le but de l'exercice est d'afficher le resultat
de l'addition de la case 'a' avec la case 'b' dans
la case 'c'.

Pour afficher du texte a l'interieur de la case 'c'
vous aurez besoin d'utiliser: c.setText('texte a afficher')
"""


from PySide2 import QtWidgets, QtCore

class MainUi(QtWidgets.QWidget):
    def __init__(self):
        super(MainUi, self).__init__()
        
        self.setWindowTitle('Calculatrice')

        main_layout = QtWidgets.QHBoxLayout(self)
        button = QtWidgets.QPushButton('Calcul')
        a = QtWidgets.QLineEdit('1')
        b = QtWidgets.QLineEdit('5')
        label_plus = QtWidgets.QLabel('+')
        c = QtWidgets.QLineEdit()
        label_egal = QtWidgets.QLabel('=')
        main_layout.addWidget(a)
        main_layout.addWidget(label_plus)
        main_layout.addWidget(b)
        main_layout.addWidget(label_egal)
        main_layout.addWidget(c)
        main_layout.addWidget(button)

        button.clicked.connect(lambda: c.setText(str(int(a.text())+int(b.text()))))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MainUi()
    win.show()
    app.exec_()