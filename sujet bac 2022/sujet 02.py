# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-02

# Exercice 1

def moyenne(couples:list) -> float: 
    return (sum([couple[0] * couple[1] for couple in couples]) / sum(couple[1] for couple in couples))


# print(moyenne([(15,2),(9,1),(12,3)]))

# Exercice 2 !

def pascal(n):
    C= [[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C


# print(pascal(4))