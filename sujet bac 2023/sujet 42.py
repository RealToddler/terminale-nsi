# # https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def tri_selection(tab):
    for i in range(len(tab)-1):
        indMin = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indMin]:
                indMin = j

        valTemp = tab[i]
        tab[i] = tab[indMin]
        tab[indMin] = valTemp
    return tab

print(tri_selection([1, 52, 6, -9, 12]))

# Exercice 2

from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)
