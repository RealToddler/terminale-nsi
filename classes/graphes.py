class GrapheNonOriente:
    def __init__(self, n):
        self.n = n
        self.adj = [[0]*n for _ in range(n)]
        print(self.adj)


    def get_adj(self) :
        return self.adj


    def ajouter_arete(self, s1, s2):
        self.adj[s1][s2] = 1 
        self.adj[s2][s1] = 1


    def arete(self, s1, s2):
        return self.adj[s1][s2]==1


    def voisins(self, s):
        return [self.adj[s][i] for i in range(self.n) if self.adj[s][i] == 1]


    def degre(self, s):
        return len(self.voisins(s))


    def degreMax(self):
        return max([self.degre(s) for s in range(self.n)])


class GrapheOriente:
    def __init__(self, n):
        self.n = n
        self.adj = [[0]*n for _ in range(n)]


    def get_adj(self) :
        return self.adj


    def ajouter_arc(self, s1, s2):
        self.adj[s1][s2]=1


    def arc(self, s1, s2):
        return self.adj[s1][s2]==1


    def successeurs(self, s):
        return [self.adj[s][i] for i in range(self.n) if self.adj[s][i] == 1]


class GrapheOrienteDict :
    def __init__(self):
        self.adj = {}


    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s]= set()


    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)


    def arc(self, s1, s2):
        return s2 in self.adj[s1]


    def sommets(self):
        return list(self.adj.keys())


    def successeurs(self, s):
        return self.adj[s]
