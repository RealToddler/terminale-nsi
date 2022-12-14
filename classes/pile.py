class Pile():
    def __init__(self):
        self.valeurs = []

    def empiler(self,val):
        self.valeurs.append(val)

    def hauteur(self):
        return len(self.valeurs)

    def estVide(self):
        return self.valeurs==[]

    def depiler(self):
        if not self.estVide():
            return self.valeurs.pop()

    def sommet(self):
        return self.valeurs[-1]