# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def recherche(elt, tab):
    return tab.index(elt) if elt in tab else -1

# Exercice 2

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = ( position_alphabet(c) + decalage ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat += c
    return resultat

print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4) )