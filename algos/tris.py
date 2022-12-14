def selection(tab):
    for i in range(len(tab)):
        indMin = i
        for j in range(i+1, len(tab)):
            indMin = j if tab[j] < tab[indMin] else indMin
        valTemp = tab[i]
        tab[i] = tab[indMin]
        tab[indMin] = valTemp
    return tab


def insertion(tab):
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j]:
            tab[j+1] = tab[j]
            j -=1
        tab[j+1] = k
    
    return tab


def rapide(tab):
    if len(tab) == 0:
        return tab

    pivot = tab[0]
    t1, t2 = [], []

    for elem in tab[1:]:
        t1.append(elem) if elem < pivot else t2.append(elem)
    
    return rapide(t1) + [pivot] + rapide(t2)


def fusion(gauche, droite):
    if not len(gauche) or not len(droite):
        return gauche or droite

    i = j = 0
    result = []

    while len(result) < len(gauche) + len(droite):
        if gauche[i] < droite[j]:
            result.append(gauche[i])
            i += 1
        else:
            result.append(droite[j])
            j += 1

        if i == len(gauche) or j == len(droite):
            result.extend(gauche[i:] or droite[j:])
            break
    
    return result


def tri_fusion(tab):

    if len(tab) < 2:
        return tab
    
    milieu = int(len(tab)/2)
    gauche = tri_fusion(tab[:milieu])
    droite = tri_fusion(tab[milieu:])

    return fusion(gauche, droite)
