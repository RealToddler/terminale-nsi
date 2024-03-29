# # https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def  ecriture_binaire_entier_positif(n):
    return [int(i) for i in list(bin(n)[2::])]

print(ecriture_binaire_entier_positif(2))

# Exercice 2

def tri_bulles(T):
    '''
	Renvoie le tableau T triÃƒÂ© par ordre croissant
	'''
    n = len(T)
    for i in range(n-1, 0,-1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T

print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))