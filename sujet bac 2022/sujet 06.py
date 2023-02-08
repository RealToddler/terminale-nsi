# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-06

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

# Exercice 2 !

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n-g+1 and trouve == False :
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve

print(recherche("AATC", "GTACAAATCTTGCC"))
print(recherche("AGTC", "GTACAAATCTTGCC"))