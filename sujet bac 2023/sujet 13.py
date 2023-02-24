# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def recherche(a, tab):
    return tab.count(a)


# Exercice 2

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):

    rendu = []
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i -= 1
    return rendu


print(rendu_monnaie(102, 500))