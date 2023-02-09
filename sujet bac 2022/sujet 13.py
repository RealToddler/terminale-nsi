# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-13

# Exercice 1

def rendu(somme_a_rendre: int) -> list:
    return [somme_a_rendre//5, (somme_a_rendre%5)//2, ((somme_a_rendre%5)%2)//1]


# print(rendu(13))
# print(rendu(64))
# print(rendu(89))


# Exercice 2 !

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None


class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None


F = File()
print("File vide", F.est_vide())
F.enfile(2)
F.affiche()
print("File vide", F.est_vide())
F.enfile(5)
F.enfile(7)
print("Affiche")
F.affiche()
print("Defile")
print(F.defile())
print("Defile")
print(F.defile())
print("Affiche")
F.affiche()
