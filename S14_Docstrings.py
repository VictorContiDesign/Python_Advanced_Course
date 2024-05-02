import S14_multiplication_def
from S14_multiplication_def import multiplicacion

print(S14_multiplication_def.__doc__)
help(S14_multiplication_def.multiplicacion)
#print(S14_multiplication_def.multiplicacion.__doc__)

#######################
# Syntaxes de Docstring

"""Docstring de style Epytext

@param param1: un premier paramètre
@param param2: un autre paramètre
@return: description de ce qui est retourné

"""

"""Docstring de style reST

:param param1: un premier paramètre
:param param2: un autre paramètre
:returns: description de ce qui est retourné

"""

"""Docstring de style Google

Args:
    param1: un premier paramètre
    param2: un autre paramètre
    
Returns:
    Description de ce qui est retourné
"""

# Exemple de génération automatique de Docstring
def fonction_ex(nom, age):
    """_summary_

    Args:
        nom (_type_): _description_
        age (_type_): _description_

    Returns:
        _type_: _description_
    """
    return True

