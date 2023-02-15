# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°1 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par resolution analytique

from Outils import *

# Utilise trouveA et trouver B puis le renvoies sous forme de chaine de caractère pour un affichage plus simple
# x, y : tableau des valeurs

def regressionLineaire(x, y):
    a = trouverA(x,y)
    b = trouverB(x,y,trouverA(x,y))
    return "a = " + str(a) + "\nb = " + str(b)


