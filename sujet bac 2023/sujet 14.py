# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def recherche(elt, tab):
    return tab.index(elt) if elt in tab else -1

print( recherche(4, [2, 4, 4, 3, 4]))
print(recherche(50, []))

# Exercice 2

def insere(a, tab):
    """ InsÃ¨re l'Ã©lÃ©ment a (int) dans le tableau tab (list)
    triÃ© par ordre croissant Ã  sa place et renvoie le
    nouveau tableau. """
    l = list(tab) #l contient les memes elements que tab
    l.append(a)
    i = len(tab) - 1
    while a < tab[i] and i >= 0:
        l[i+1] = tab[i]
        l[i] = a
        i = i -1
    return l

print( insere(30, [1, 2, 7, 12, 14, 25]))