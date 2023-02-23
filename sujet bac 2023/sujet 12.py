# # https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

class ABR:
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self is None:
            return ''
        else:
            return '(' + (self.gauche).__repr__() + ',' + str(self.cle) + ',' +(self.droit).__repr__() + ')'

n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)


def ajoute(cle, a):
    if a is None:
        return ABR(None, cle, None)
    elif cle == a.cle:
        return a
    elif cle < a.cle:
        return ABR(ajoute(cle, a.gauche), a.cle, a.droit)
    else:
        return ABR(a.gauche, a.cle, ajoute(cle, a.droit))


def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses:
        i=0
        while i <= nb_boites and boites[i] + masse > c:
                i = i + 1
        if i == nb_boites + 1:
                nb_boites += 1
        boites[i] = boites[i] + masse
    return nb_boites + 1


print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))