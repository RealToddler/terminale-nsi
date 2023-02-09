 # https://glassus.github.io/terminale_nsi/T6_6_Epreuve_pratique/BNS_2022/#sujet-14

 # Exercice 1

def correspond(mot: str, mot_a_trous: str) -> bool:
    mot = list(mot)
    for i in range(len(mot_a_trous)):
        if mot_a_trous[i] == '*':
            mot[i] = '*'
        
    return "".join(mot) == mot_a_trous

# print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) 
# print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))


# Exercice 2 !

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire plan correspondant
    à un plan d'envoi de messages entre N personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    for _ in range(N-1):
        if plan[personne] == 'A':
            return True
        else:
            personne = plan[personne]
    return False


print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}))