# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    
    else:
        for i in range(len(mot)):
            if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
                return False
    
    return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

# Exercice 2

print('Exercice 2')

def est_cyclique(plan):
    '''
    Prend en paramÃƒÂ¨tre un dictionnaire `plan` correspondant Ãƒ  un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan['A']
    nb_destinaires = 1
    
    while destinataire != 'A':
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)

print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}))
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}))
print(est_cyclique({'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}))
print(est_cyclique({'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}))