# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def recherche_min(tab):
    return tab.index(min(tab))


print(recherche_min([5]))
print(recherche_min([5, 3, 2, 2, 4]) )

# Exercice 2

def separe(tab):

    gauche = 0
    droite = len(tab)-1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche += 1
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche]
            droite = droite -1
    return tab

print(separe([1, 0, 1, 0, 1, 0, 1, 0]))