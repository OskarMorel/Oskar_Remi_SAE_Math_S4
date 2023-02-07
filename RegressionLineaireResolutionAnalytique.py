# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Algorithme N°1 pour l'estimation du prix d'un appartement  par rapport à ça surface  Régression linéaire par resolution analytique

with open("values.txt", "r") as f:
    x = list()
    y = list()
    for line in f:
        data = line.split()
        x.append(data[0])
        y.append(data[1])
print(x)
print(y)