# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def enumere(L):
    dic = {key: [] for key in set(L)}
    for i in range(len(L)):
        dic[L[i]].append(i)
    return dic

print(enumere([1, 1, 2, 3, 2, 1]))


# Exercice 2

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implÃ©mente
        un arbre binaire de recherche.
    """
    if arbre != None:
        if not arbre.fg:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if not arbre.fd:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)