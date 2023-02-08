# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-08

# Exercice 1

def recherche(elt: int, tab:list) -> int:
    return [i for i in range(len(tab)) if tab[i] == elt][0] if elt in tab else -1


# print(recherche(1, [2, 3, 4]))
# print(recherche(1, [10, 12, 1, 56]))
# print(recherche(50, [1, 50, 1]))
# print(recherche(15, [8, 9, 10, 15]))

# Exercice 2 !

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i -= 1
    return l

print(insere(3,[1,2,4,5]))
print(insere(10,[1,2,7,12,14,25]))
print(insere(1,[2,3,4]))