# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-22


# Exercice 1

def renverse(mot:str) -> str:
    return mot[::-1]


print(renverse("informatique"))

# Exercice 2

def crible(N):
    """
    Renvoie un tableau contenant tous les nombres premiers plus petits que N
    """
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

