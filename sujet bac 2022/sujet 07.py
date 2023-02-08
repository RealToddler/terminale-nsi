# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-07

# Exercice 1

def conv_bin(n: int) -> tuple:
    return (list(bin(n))[2:], len(list(bin(n))[2:]))


# print(conv_bin(9))

# Exercice 2 !

def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

print(tri_bulles([1, 4, 5, 2, 6]))