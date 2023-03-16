# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Outils mathématiques statistiques pour aider aux différents calculs du projet
import math

# from matplotlib import pyplot as plt
from RegressionLineaireResolutionAnalytique import *

# Ouvre un fichier est vérifie que la tabulation entre les x et les y est bien faite
# url : l'url du fichier
# return : x et y sous forme de tableau
def ouvertureFichier(url):
    with open(url, "r") as f:
        x = list()
        y = list()
        for line in f:
            # vérifie qu'il y ai bien une tabulation entre chaques x et y
            try:
                line = line.strip()
                data = line.split(chr(9))
                x.append(float(data[0]))
                y.append(float(data[1]))
            # si il n'y a pas que des tabulations entre les x et y alors affichage d'une erreur
            except:
                print("Erreur, vous ne respectez pas le format voulu")
                x.clear()
                y.clear()
    return x, y


# calcule la moyenne
# x : tableau des valeurs où on va calculer la moyenne
# return : la moyenne
def moyenne(x):
    return sum(x) / len(x)

# calcule la covariance
# x : tableau des x
# y : tableau des y
# return : la covariance
def covariance(x, y):
    covariance = 0
    for i in range(len(x)):
        covariance += (x[i] - moyenne(x)) * (y[i] - moyenne(y))
    covariance /= (len(x) - 1)

    return covariance

# calcule la variance
# x : tableau des x
# return : la variance
def variance (x):
    variance = 0
    for i in range(len(x)):
        variance += (x[i] - moyenne(x)) ** 2
    variance /= (len(x) - 1)
    return variance

# Trouve A pour la régréssion linéaire par méthode analytique
# x , y : tableau avec les valeurs
# return A
def trouverA(x,y):
    return covariance(x,y) / variance(x)

# Trouve B pour la régréssion linéaire par méthode analytique
# x , y : tableau avec les valeurs
# a : la valeure calculée avec la méthode TrouverA(x, y)
# return B
def trouverB(x,y,a):
    return moyenne(y) - a * moyenne(x)


# Calcule la médiane (valeure au milieu)
# x : tableau avec les valeurs
# return la médiane
def mediane(x):
    xTrie = sorted(x)
    n = len(x)

    if n % 2 == 0:
        mediane = (xTrie[n // 2 - 1] + xTrie[n // 2]) / 2
    else:
        mediane = xTrie[n // 2]

    return mediane

# calcul l'étendue
# x : tableau des valeurs
# return : l'étendue
def etendue(x):
    return max(x) - min(x)

# calcul l'écart type
# x : tableau des valeurs
# return : écarts type
def ecartsType(x):
     return math.sqrt(variance(x))

# calcul du coefficient de corrélation linéaire
# x : tableau des valeurs x
# y : tableau des valeurs y
# return : le coefficient de corrélation linéaire
def coefCorrelationLineaire(x,y):
    diffDesX = [xi - moyenne(x) for xi in x]
    diffDesY = [yi - moyenne(y) for yi in y]

    multiplicationDesDiff = [diffDesX[i] * diffDesY[i] for i in range(len(x))]

    SommeRacineDifDesX = sum([x_i ** 2 for x_i in diffDesX])
    SommeRacineDifDesY = sum([y_i ** 2 for y_i in diffDesY])

    return sum(multiplicationDesDiff) / math.sqrt(SommeRacineDifDesX * SommeRacineDifDesY)

# Affiche un graphique nuage de points avec une droite de régression. Utilisation de
# la libairie mathplotlib et pyplot. Utilise la méthode analytique
# x, y : les tableaux contenant les valeurs

 #def graphique(x, y):
   # a = trouverA(x, y)
    #b = trouverB(x, y, a)

    #droiteRegression = [a * xi + b for xi in x]

    #plt.scatter(x, y)
    #plt.plot(x, droiteRegression, color='red')
    #plt.xlabel("Surface d'un appartement")
    #plt.ylabel("Prix de l'appartement")
    #plt.show()



