# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-01

# Exercice 1

def recherche(caractere: str, mot:str) -> int:
    return len([i for i in range(len(mot)) if mot[i] == caractere])


# print(recherche('e', "sciences"))
# print(recherche('i',"mississippi"))
# print(recherche('a',"mississippi"))

# Exercice 2

pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution,i)
    else :
        return rendu_glouton(arendre, solution, i+1)


# print(rendu_glouton(68, [], 0))
# print(rendu_glouton(291, [], 0))
