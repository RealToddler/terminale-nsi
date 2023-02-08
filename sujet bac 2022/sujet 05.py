# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-05

# Exercice 1

def rechercheMinMax(tab:list) -> dict:
    dic = {"max": None, "min": None}
    dic["max"], dic["min"] = tab[0], tab[0]
    for item in tab:
        dic["max"] = item if item >  dic["max"] else dic["max"]
        dic["min"] = item if item < dic["min"] else dic["min"]
    
    return dic


tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
resultat = rechercheMinMax(tableau)
# print(resultat)

# Exercice 2

class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range( 1, 14)]

    """Renvoie la Carte qui se trouve a  la position donnee"""
    def getCarteAt(self, pos):
        if 0 <= pos < len(self.contenu) :
            return self.contenu[pos]

unPaquet = PaquetDeCarte()
unPaquet.remplir()
uneCarte = unPaquet.getCarteAt(20)
print(uneCarte.getNom() + " de " + uneCarte.getCouleur())