# | Auteurs : Remi Jauzion - Oskar Morel |
# |--------------------------------------|
# Algorithme N°2 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par descente de gradient

# Calcule la dérivée partielle de a
# x, y : tableau des valeurs
# a, b : valeurs initiale
# return : le resultat de la derivee de a

def lesSommes(x, y):
    sommeXAuCarre = 0
    sommeX = 0
    sommeXY = 0
    sommeY = 0
    for i in range(len(x)):
        sommeXAuCarre = sommeXAuCarre + (x[i] * x[i])
        sommeX = sommeX + x[i]
        sommeXY = sommeXY + (x[i] * y[i])
        sommeY = sommeY + y[i]
    return sommeX,sommeY,sommeXY,sommeXAuCarre




def derivePartielleA(a,b, sommeXAuCarre, sommeX, sommeXY):
    resultat = 2 * ((a * sommeXAuCarre) + (b * sommeX) - sommeXY)
    return resultat

# Calcule la dérivée partielle de b
# x, y : tableau des valeurs
# a, b : valeurs initiale
# return : le resultat de la derivee de b
def derivePartielleB(x,a,b,sommeX,sommeY):
    resultat = 2 * ((a * sommeX) + (len(x) * b) - sommeY)
    return resultat

# Utilise les deux méthodes de calcul des dérivées partielles
# maxIter : le nombre max d'itération avant que la boucle s'arrête (pour pas prendre trop de
# ressource ou finir sur un cas infini
# return : a et b calculés avec la descente de gradient

#TODO modifier pas sinon gros fichier passe pas et attention derive partielle trop de calcul a faire, faut optimiser

def descenteGradient(x,a,b,sommeX,sommeY,sommeXY,sommeXAuCarre, maxIter):
    pas = 0.00001
    fini = False
    i = 0
    while not fini:

        if (i >= maxIter or (abs(derivePartielleB(x, a, b, sommeX, sommeY)) <= 0.00001 and abs(derivePartielleA(a, b, sommeXAuCarre, sommeX, sommeXY)) <= 0.00001)):
            fini = True

        b -= derivePartielleA(a,b, sommeXAuCarre, sommeX, sommeXY) * pas
        a -= derivePartielleB(x,a,b,sommeX,sommeY) * pas

        i+=1

    return "a = " + str(a) + "\nb = " + str(b)


