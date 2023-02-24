# https://pixees.fr/informatiquelycee/term/ep/index.html

# Exercice 1

def moyenne(tab):
    return sum(tab)/len(tab)

print(moyenne([1.0, 2.0, 4.0]))

# Exercice 2

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(83))