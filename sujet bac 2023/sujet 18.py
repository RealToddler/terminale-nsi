# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def max_et_indice(tab: int) -> tuple:
    assert(tab != []), "le tableau est vide"

    maxValue = tab[0]

    for i in range(1, len(tab)): 
        maxValue = tab[i] if tab[i] > maxValue else maxValue
    
    return (maxValue, tab.index(maxValue))


print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))


# Exercice 2

def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 Ã   n, False sinon
    '''
    for i in range(1, len(tab)):
        if not i in tab:
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui reprÃ©sente un ordre
    de gÃ¨nes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gÃƒÂ¨nes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < len(ordre)-1:
        if (ordre[i+1] - ordre[i]) not in [-1, 1]: # l'ÃƒÂ©cart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb


print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))