"""
Module pour realiser des opérations mathématiques de base
tel que l'addition, la multiplication ou la soustraction
"""

def division(a, b):
    """Divise deux nombre entier et retourne le résultat de l'opération

    Args:
        a (int): le premier nombre
        b (int): le deuxieme nombre

    Returns:
        int: le résultat de l'opération
        str: le résultat du message en cas d'erreur
    """
    
    try:
        return a / b
    except ZeroDivisionError:
        return "Division par 0 impossible"
    except TypeError:
        return "Svp, entrez deux nombres entiers"

def multiplicacion(a, b):
    """Multiplie deux nombres et retourne le résultat de l'opération
    
    :param a:   le premier nombre
    :param b:   le deuxieme nombre
    :type a:    int
    :type b:    int
    :return:    Le resultat de la multiplication
    :rtype:     int
    
    :Example:
    
    >>>multiplication(2, 5)
    10
    
    """
    return a * b