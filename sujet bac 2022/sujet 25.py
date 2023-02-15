# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-25

# Exercice 1

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
            {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
            {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
            {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
            {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]

def selection_enclos(table_animaux: list, num_enclos: int) -> list:
    return [item for item in table_animaux if item["enclos"] == num_enclos]


print(selection_enclos(animaux, 5))
print(selection_enclos(animaux, 2))
print(selection_enclos(animaux, 7))

# Exercice 2

def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans la liste tab où 
    tab vérifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice + 1] == tab[indice]:
            return trouver_intrus(tab, indice + 3, d)
        else:
            return trouver_intrus(tab, g, indice)


print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2, 2, 2, 4, 4, 4, 8, 8,
8, 5, 5, 5], 0, 21))
