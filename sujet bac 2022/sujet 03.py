# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-03

# Exercice 1

def delta(tab:list) -> int:
    if tab == []:
        return "le tableau est vide"

    return [tab[0]] + [tab[i+1] - tab[i] for i in range(len(tab)-1)]


# print(delta([1000, 800, 802, 1000, 1003]))
# print(delta([42])

# Exercice 2 !

class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire disposant de 3
    attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit.
    '''
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ""
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    return s # 

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),
'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',
Noeud(None, 1, None)))

print(expression_infixe(e))
