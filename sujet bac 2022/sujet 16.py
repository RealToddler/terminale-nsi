# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-16

# Exercice 1

def maxi(tab: list) -> tuple:
    max_val = tab[0]
    max_index = 0

    for i in range(1, len(tab)):
        if tab[i] > max_val:
            max_val = tab[i]
            max_index = i
    
    return (max_val, max_index)


# print(maxi([1,5,6,9,1,2,3,7,9,8]))

# Exercice 2

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

# print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
