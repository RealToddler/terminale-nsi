# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-19

# Exercice 1

def multiplication(n1: int, n2: int) -> int:
    toReturn = 0
    for _ in range(abs(n2)):
        if n1 < 0 and n2 < 0:
            toReturn -= n1
        else:
            toReturn += n1
    return toReturn


# print(multiplication(3,5))
# print(multiplication(-4,-8))
# print(multiplication(-2,6))
# print(multiplication(-2,0))

# Exercice 2

def chercher(T, n, i, j):
    if i < 0 or j >= len(T):
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if T[m] < n :
        return chercher(T, n, m+1 , j)
    elif T[m] > n :
        return chercher(T, n, i , m-1 )
    else :
        return m

print(chercher([1,5,6,6,9,12],7,0,10))
print(chercher([1,5,6,6,9,12],7,0,5))
print(chercher([1,5,6,6,9,12],9,0,5))
print(chercher([1,5,6,6,9,12],6,0,5))