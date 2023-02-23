# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def convertir(tab: list) -> int:
    return int(''.join([str(i) for i in tab]), 2    )


print(convertir([1, 0, 1, 0, 0, 1, 1]))


# Exercice 2

liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j  -= 1
        tab[j] = valeur_insertion

tri_insertion(liste) 

print(liste)