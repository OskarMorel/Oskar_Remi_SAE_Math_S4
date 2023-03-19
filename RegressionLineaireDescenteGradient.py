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
    sommeYAuCarre = 0
    for i in range(len(x)):
        sommeXAuCarre = sommeXAuCarre + (x[i] * x[i])
        sommeYAuCarre = sommeYAuCarre + (y[i] * y[i])
        sommeX = sommeX + x[i]
        sommeXY = sommeXY + (x[i] * y[i])
        sommeY = sommeY + y[i]
    return sommeX,sommeY,sommeXY,sommeXAuCarre, sommeYAuCarre




def derivePartielleA(a,b, sommeXAuCarre, sommeX, sommeXY):
    resultat = 2 * ((a * sommeXAuCarre) + (b * sommeX) - sommeXY)
    return resultat

# Calcule la dérivée partielle de b
# x, y : tableau des valeurs
# a, b : valeurs initiale
# return : le resultat de la derivee de b
def derivePartielleB(x,a,b,sommeX,sommeY):
    resultat = 2 * (a * sommeX + len(x) * b - sommeY)
    return resultat

# Utilise les deux méthodes de calcul des dérivées partielles
# maxIter : le nombre max d'itération avant que la boucle s'arrête (pour pas prendre trop de
# ressource ou finir sur un cas infini
# return : a et b calculés avec la descente de gradient

def descenteGradient(x,y,maxIter):

    a = 1
    b = 1
    fctCoutAvant = 0
    fctCoutApres = 0

    (sommeX,sommeY,sommeXY,sommeXAuCarre, sommeYAuCarre) = lesSommes(x, y)

    pas = 0.0001
    fini = False
    i = 0
    while not fini:

        if (i >= maxIter or (abs(derivePartielleB(x, a, b, sommeX, sommeY)) <= 0.0001 and abs(derivePartielleA(a, b, sommeXAuCarre, sommeX, sommeXY)) <= 0.0001)):
            fini = True

        fctCoutAvant = sommeYAuCarre - 2 * a * sommeXY - 2 * b * sommeY + a * a * sommeXAuCarre + 2 * a * b * sommeX + len(
            x) * b * b

        a -= derivePartielleA(a,b, sommeXAuCarre, sommeX, sommeXY) * pas
        b -= derivePartielleB(x,a,b,sommeX,sommeY) * pas

        fctCoutApres = sommeYAuCarre - 2 * a * sommeXY - 2 * b * sommeY + a * a * sommeXAuCarre + 2 * a * b * sommeX + len(
            x) * b * b

        # On divise le pas par 2 si la fonction cout est plus grande après le calcul du nouveau gradient que avant
        if fctCoutApres > fctCoutAvant:
            pas /= 2

        i+=1
    return "a = " + str(a) + "\nb = " + str(b)


