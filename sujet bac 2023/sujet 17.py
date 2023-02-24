# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def moyenne(liste_notes):
    return sum([item[0] * item[1] for item in liste_notes]) / sum([item[1] for item in liste_notes])

print(moyenne([(15, 2), (9, 1), (12, 3)]))

# Exercice 2

def pascal(n):
    triangle= [[1]]
    for k in range(1, n+1):
        ligne_k = [1]
        for i in range(1, k):
            ligne_k.append(triangle[k-1][i-1] + triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle


print(pascal(4))
