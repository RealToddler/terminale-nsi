# https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-23

# Exercice 1

def max_dico(dico: dict) -> tuple:
    return [(name, max(dico.values())) for name in dico.keys() if dico[name] == max(dico.values())][0]

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))

# Exercice 2

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()


print(eval_expression([2, 3, '+', 5, '*']))