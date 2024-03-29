# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def delta(liste):
    return [liste[0]] + [liste[i] - liste[i-1] for i in range(1, len(liste))]

print(delta([1000, 800, 802, 1000, 1003]) )
    

# Exercice 2

class Noeud:
    '''
    classe implÃƒÂ©mentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possÃ©de 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'Ã©tiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la reprÃ©sentation du noeud en chaine de caractÃ¨res
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None


e = Noeud(Noeud(Noeud(None, 3, None),
    '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))),
    '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))


def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    return s

print(expression_infixe(e))