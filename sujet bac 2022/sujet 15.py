# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-15

# Exercice 1

def nb_repetitions(elt: any, tab:list) -> int:
    return tab.count(elt)


# print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
# print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
# print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))

# Exercice 2

def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a != 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a


print(binaire(0))
print(binaire(77))