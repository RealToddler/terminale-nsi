class Noeud:
    def __init__(self, valeur, g, d):
        self.val = valeur
        self.gauche = g
        self.droit = d


class ArbreBinaire:
    def __init__(self, noeudRacine):
        self.racine = noeudRacine


    def estVide(self):
        return self.racine is None


    def valRacine(self):
        assert not(self.estVide()), 'Arbre vide '
        return self.racine.val


    def filsG(self):
        assert not(self.estVide()), 'Arbre vide '
        return self.racine.gauche


    def filsD(self):
        assert not(self.estVide()), 'Arbre vide '
        return self.racine.droit


def creeVide():
    return ArbreBinaire(None)


def creeNoeud(valeur, g, d):
    return ArbreBinaire(Noeud(valeur, g, d))

