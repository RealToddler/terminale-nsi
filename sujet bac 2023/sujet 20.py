# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def ajoute_dictionnaires(d1, d2):
    for key in d1:
        if key in d2.keys():
            d2[key] += d1[key]
        else:
            d2[key] = d1[key]
    
    return d2


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

# Exercice 2

from random import randint
def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if not case_en_cours in cases_vues:
            cases_vues.append(case_en_cours)
        n += 1
    return n