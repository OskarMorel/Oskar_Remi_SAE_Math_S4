# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°2 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par descente de gradient
from matplotlib import pyplot as plt

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

def derivePartielleA(x,y,a,b):
    sommeXAuCarre = 0
    sommeX = 0
    sommeXY = 0
    for i in range(len(x)):
        sommeXAuCarre = sommeXAuCarre + (x[i] * x[i])
        sommeX = sommeX + x[i]
        sommeXY = sommeXY + (x[i] * y[i])

    resultat = 2 * ((a * sommeXAuCarre) + (b * sommeX) - sommeXY)
    return resultat

def derivePartielleB(x,y,a,b):
    sommeX = 0
    sommeY = 0
    for i in range(len(x)):
        sommeX = sommeX + x[i]
        sommeY = sommeY + y[i]

    resultat = 2 * ((a * sommeX) + (len(x) * b) - sommeY)
    return resultat

def descenteGradient(x,y,a,b):
    pas = 0.00001
    fini = False
    while not fini:

        if abs(derivePartielleB(x,y,a,b)) <= 0.0001 and abs(derivePartielleA(x,y,a,b)) <= 0.0001:
            fini = True

        b -= derivePartielleB(x,y,a,b) * pas
        a -= derivePartielleA(x,y,a,b) * pas

    return a, b

print(descenteGradient(x,y,1,1))

def graphique(x, y):
    a, b = descenteGradient(x, y, 1, 1)
    y_regression = [a * xi + b for xi in x]

    plt.scatter(x, y)
    plt.plot(x, y_regression, color='red')
    plt.xlabel("Surface d'un appartement")
    plt.ylabel("Prix de l'appartement")
    plt.show()

graphique(x,y)
