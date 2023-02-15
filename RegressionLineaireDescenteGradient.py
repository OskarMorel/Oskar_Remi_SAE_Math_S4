# | Auteurs : Remi Jauzion - Oskar Morel |
# |--------------------------------------|
# Algorithme N°2 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par descente de gradient

# Calcule la dérivée partielle de a
# x, y : tableau des valeurs
# a, b : valeurs initiale
# return : le resultat de la derivee de a
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

# Calcule la dérivée partielle de b
# x, y : tableau des valeurs
# a, b : valeurs initiale
# return : le resultat de la derivee de b
def derivePartielleB(x,y,a,b):
    sommeX = 0
    sommeY = 0
    for i in range(len(x)):
        sommeX = sommeX + x[i]
        sommeY = sommeY + y[i]

    resultat = 2 * ((a * sommeX) + (len(x) * b) - sommeY)
    return resultat

# Utilise les deux méthodes de calcul des dérivées partielles
# maxIter : le nombre max d'itération avant que la boucle s'arrête (pour pas prendre trop de
# ressource ou finir sur un cas infini
# return : a et b calculés avec la descente de gradient

#TODO modifier pas sinon gros fichier passe pas et attention deriver partielle trop de calcul a faire, faut optimiser

def descenteGradient(x,y,a,b, maxIter):
    pas = 0.00001
    fini = False
    i = 0
    while not fini:

        if (abs(derivePartielleB(x,y,a,b)) <= 0.0001 and abs(derivePartielleA(x,y,a,b)) <= 0.0001) or (i >= maxIter):
            fini = True

        b -= derivePartielleB(x,y,a,b) * pas
        a -= derivePartielleA(x,y,a,b) * pas

        i += 1

    return "a = " + str(a) + "\nb = " + str(b)

