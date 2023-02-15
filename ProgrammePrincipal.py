# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Programme principal qui appelle les méthodes des différentes classes du projet
import os

from RegressionLineaireResolutionAnalytique import *
from RegressionLineaireDescenteGradient import *
from Outils import *
import time

print("┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓\n"
      + "┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃\n"
      + "┃┗━┛┣━━┳━━┳━┳━━┳━━┳━━┳┳━━┳━┓╋┃┃┏┳━┓┏━━┳━━┳┳━┳━━┓\n"
      + "┃┏┓┏┫┃━┫┏┓┃┏┫┃━┫━━┫━━╋┫┏┓┃┏┓┓┃┃┣┫┏┓┫┃━┫┏┓┣┫┏┫┃━┫\n"
      + "┃┃┃┗┫┃━┫┗┛┃┃┃┃━╋━━┣━━┃┃┗┛┃┃┃┃┃┗┫┃┃┃┃┃━┫┏┓┃┃┃┃┃━┫\n"
      + "┗┛┗━┻━━┻━┓┣┛┗━━┻━━┻━━┻┻━━┻┛┗┛┗━┻┻┛┗┻━━┻┛┗┻┻┛┗━━┛\n"
      + "╋╋╋╋╋╋╋┏━┛┃\n"
      + "╋╋╋╋╋╋╋┗━━┛\n")

url = None

while True:
    if url == None:
        quitter = False
        while not quitter:
            url = input("Veuillez entrer le chemin de votre fichier contenant les valeur : ")
            if os.path.exists(url):
                x, y = ouvertureFichier(url)
                print("Importation du fichier réussie")
                break
            else:
                print("Le chemin du fichier est erroné")

                choixQuitter = input("Voulez vous quitter l'importation du fichier ? O / N : ")
                if choixQuitter == "O":
                    quitter = True
                else:
                    url = None
    print("\n***********************")
    print("Choisissez une option")
    print("***********************\n")
    print("1 - Ouvrir un autre fichier contenant les valeurs")
    print("2 - Calculer le prix d'un appartement")
    print("3 - Régression linéaire par resolution analytique")
    print("4 - Régression linéaire par descente de gradient")
    print("5 - Indicateurs statistiques")
    print("6 - Afficher le graphique")
    print("7 - Aide format des données")
    print("8 - Quitter")

    choix = input("\nEntrez votre choix : ")
    print("\n")

    if choix == "1":
        quitter = False
        while not quitter:
            url = input("Veuillez entrer le chemin de votre fichier contenant les valeur : ")
            if os.path.exists(url):
                x, y = ouvertureFichier(url)
                print("Importation du fichier réussie")
                break
            else:
                print("Le chemin du fichier est erroné")

                choixQuitter = input("Voulez vous quitter l'importation du fichier ? O / N : ")
                if choixQuitter == "O":
                    quitter = True
                else:
                    url = None
    elif choix == "2":
        surface = input("Veuillez entrer la surface d'un appartement (en m²) : ")
        try:
            prixAppart = 2.64 * float(surface) + 3.53
            prixAppart *= 1000
            print("Pour un appartement de " + str(surface)+ " m². Le prix sera de " + str("{:.2f}".format(prixAppart)) + " €")
        except ValueError:
            print("\nErreur, vous n'avez pas rentré un nombre")
    elif choix == "3":
        print("Regression linéaire par résolution analytique\n" + str(regressionLineaire(x, y)))
    elif choix == "4":
        print("Regression linéaire par descente de gradient\n" + descenteGradient(x, y, 1, 1, 1000))
    elif choix == "5":
        print("*****************")
        print("Indicateurs sur X")
        print("*****************")
        print("Moyenne X : " + str(moyenne(x)))
        print("Mediane X : " + str(mediane(x)))
        print("Etendue X : " + str(etendue(x)))
        print("Variance X : " + str(variance(x)))
        print("\n*****************")
        print("Indicateurs sur Y")
        print("*****************")
        print("Moyenne Y : " + str(moyenne(y)))
        print("Mediane Y : " + str(mediane(y)))
        print("Etendue Y : " + str(etendue(y)))
        print("Variance Y : " + str(variance(y)))
        print("\n*****************")
        print("Indicateurs sur X et Y")
        print("*****************")
        print("Covariance X et Y : " + str(covariance(x,y)))
        print("Coefficient de corrélation linéaire X et Y : " + str(coefCorrelationLineaire(x,y)))
        coef = coefCorrelationLineaire(x,y)
        if coef == 0:
            print("La corrélation des données est nulle")
        elif coef > 0 and coef < 0.5:
            print("La corrélation des données est positivement faible")
        elif coef >= 0.5 and coef < 1:
            print("La corrélation des données est postivement forte")
        elif coef >= 1:
            print("La corrélation des données est positivement très forte")
        elif coef < 0 and coef > -0.5:
            print("La corrélation des données est négativement faible")
        elif coef <= -0.5 and coef > -1:
            print("La corrélation des données est négativement forte")
        elif coef <= -1:
            print("La corrélation des données est négativement très forte")
    elif choix == "6":
        graphique(x, y)
    elif choix == "7":
        print("Quand vous voulez remplir votre propre fichier avec vos propres données. Il faut respecter le\n"
              + "format attendu. Sur chaque ligne il faut 'x' votre valeur x. Ensuite tabulation et enfin\n"
              + "'y' votre valeur y.\n"
              + "Ex : 62   94.3")
    elif choix == "8":
        print("Merci, au revoir")
        time.sleep(5)
        break
    else:
        print("Choix invalide, réessayer")
