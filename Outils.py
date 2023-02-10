# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Outils mathématiques statistiques pour aider aux différents calculs du projet
import math

from matplotlib import pyplot as plt
from RegressionLineaireResolutionAnalytique import *

def ouvertureFichier(url):
    with open(url, "r") as f:
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
                x.clear()
                y.clear()
    return x, y

def moyenne(x):
    return sum(x) / len(x)


def covariance(x, y):
    covariance = 0
    for i in range(len(x)):
        covariance += (x[i] - moyenne(x)) * (y[i] - moyenne(y))
    covariance /= (len(x) - 1)

    return covariance

def variance (x):
    variance = 0
    for i in range(len(x)):
        variance += (x[i] - moyenne(x)) ** 2
    variance /= (len(x) - 1)

    return variance

def mediane(x):
    xTrie = sorted(x)
    n = len(x)

    if n % 2 == 0:
        mediane = (xTrie[n // 2 - 1] + xTrie[n // 2]) / 2
    else:
        mediane = xTrie[n // 2]

    return mediane

def etendue(x):
    return max(x) - min(x)

def ecartsType(x):
     return math.sqrt(variance(x))

def coefCorrelationLineaire(x,y):
    diffDesX = [xi - moyenne(x) for xi in x]
    diffDesY = [yi - moyenne(y) for yi in y]

    multiplicationDesDiff = [diffDesX[i] * diffDesY[i] for i in range(len(x))]

    SommeRacineDifDesX = sum([x_i ** 2 for x_i in diffDesX])
    SommeRacineDifDesY = sum([y_i ** 2 for y_i in diffDesY])

    return sum(multiplicationDesDiff) / math.sqrt(SommeRacineDifDesX * SommeRacineDifDesY)

def trouverA(x,y):
    return covariance(x,y) / variance(x)

def trouverB(x,y,a):
    return moyenne(y) - a * moyenne(x)

def graphique(x, y):
    a = trouverA(x, y)
    b = trouverB(x, y, a)
    y_regression = [a * xi + b for xi in x]

    plt.scatter(x, y)
    plt.plot(x, y_regression, color='red')
    plt.xlabel("Surface d'un appartement")
    plt.ylabel("Prix de l'appartement")
    plt.show()
