# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°2 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par descente de gradient

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

    return "a = " + str(a) + "\nb = " + str(b)

