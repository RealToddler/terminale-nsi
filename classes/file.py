class File():
    def __init__(self):
        self.valeurs = []


    def enfiler(self,x):
        self.valeurs.append(x)


    def longueur(self):
        return len(self.valeurs)


    def fileVide(self):
        return self.valeurs==[]


    def defiler(self):
        if not self.fileVide():
            return self.valeurs.pop(0)
    
    
    def premierFile(self):
        return self.valeurs[0]


        