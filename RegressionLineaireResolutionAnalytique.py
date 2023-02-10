# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°1 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par resolution analytique

from matplotlib import pyplot as plt
from Outils import *

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

def trouverA(x, y):
    return covariance(x, y) / variance(x)

def trouverB(x, y, a):
    return moyenne(y) - a * moyenne(x)

def regressionLineaire(x, y):
    a = trouverA(x, y)
    b = trouverB(x, y, trouverA(x, y))
    return "a = " + str(a) + "\nb = " + str(b)

print(regressionLineaire(x,y))


def graphique(x, y):
    a = trouverA(x,y)
    b = trouverB(x, y ,a)
    y_regression = [a * xi + b for xi in x]

    plt.scatter(x, y)
    plt.plot(x, y_regression, color='red')
    plt.xlabel("Surface d'un appartement")
    plt.ylabel("Prix de l'appartement")
    plt.show()

graphique(x, y)

