# # https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

def rangements_valeurs(tab):
    return [tab.count(i) for i in range(11)]


def notes_triees(tab):
    toReturn = []
    for i in range(len(tab)):
        for _ in range(tab[i]):
            toReturn.append(i)

    return toReturn


effectifs_notes = rangements_valeurs(notes_eval)
print(effectifs_notes)
print(notes_triees(effectifs_notes))

# Exercice 2

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == '1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
    

print(bin_to_dec('11001'))

