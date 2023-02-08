# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-11

# Exercice 1 !

def recherche(tab: list, n:int) -> int:
    debut = 0
    fin = len(tab) -1

    while debut <= fin:
        milieu = (fin+debut) // 2
        if tab[milieu] == n:
            return milieu
        
        elif tab[milieu] > n:
            fin = milieu-1
        
        elif tab[milieu] < n:
            debut = milieu + 1
            
    return -1


# print(recherche([2, 3, 4, 5, 6], 5))
# print(recherche([2, 3, 4, 6, 7], 5))

# Exercice 2

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message:
        if lettre in ALPHABET:
            indice = (position_alphabet(lettre) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + lettre
    return resultat
    
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !',4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !',-5))
