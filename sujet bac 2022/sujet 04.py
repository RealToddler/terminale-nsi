# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-04

# Exercice 1

def recherche(tab: list) -> list:
    return [(tab[i], tab[i+1]) for i in range(len(tab)-1) if tab[i+1] - tab[i] == 1]


# print(recherche([1, 4, 3, 5]))
# print(recherche([1, 4, 5, 3]))
# print(recherche([7, 1, 2, 5, 3, 4]))
# print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

# Exercice 2

def propager(M, i, j, val):
    if M[i][j]== 0:
        return None # 

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1): # 
        propager(M, i, j+1, val)


M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
propager(M,2,1,3)
print(M)