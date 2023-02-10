# | Auteurs : Remi Jauzion - Oskar Morel |
# |-------------------------------------|
# Outils mathématiques statistiques pour aider aux différents calculs du projet

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
