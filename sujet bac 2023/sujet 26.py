# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def multiplication(n1: int, n2: int) -> int:
    resultat = 0
    if (n1 > 0 and n2 > 0) or ((n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0)):
        for _ in range(n2):
            resultat += n1

    elif n1 < 0 and n2 < 0:
        for _ in range(-n2):
            resultat += -n1

    return resultat

# Exercice 2

def dichotomie(tab, x):
    """
    tab : tableau dâ€™entiers triÃ© dans lâ€™ordre croissant
    x   : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m-1
    return False


print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27))