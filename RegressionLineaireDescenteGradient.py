# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°1 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par descente de gradient

from RegressionLineaireResolutionAnalytique import trouverA
from RegressionLineaireResolutionAnalytique import trouverB

with open("values.txt", "r") as f:
    x = list()
    y = list()
    for line in f:
        try:
            line = line.strip()
            data = line.split(chr(9))
            x.append(float(data[0]))
            y.append(float(data[1]))
        except:
            print("Erreur lecture fichier")
            x.clear
            y.clear

a = trouverA(x, y)
b = trouverB(x, y, trouverA(x, y))
deriveF = a

def f(x):
    return a * x + b

# La derivée est une constante donc on est pas sensé faire une itération ça sert à rien mais du coup
# je vais voir comment faut faire


