# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°1 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par resolution analytique


from statistics import variance
from statistics import covariance
from statistics import mean

x = [32, 50, 21, 23]
y = [36.3, 5, 21.6, 22]

def trouverA(x, y):
    return covariance(x, y) / variance(x)

def trouverB(x, y, a):
    return mean(y) - a * mean(x)

def regressionLineaire(x, y):
    a = trouverA(x, y)
    b = trouverB(x, y, trouverA(x, y))
    return "a = " + str(a) + "\nb = " + str(b)

print(regressionLineaire(x,y))
