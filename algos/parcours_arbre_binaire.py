from classes.file import * # importation du module file
from classes.arbre_binaire import * # importation du module arbre_binaire
#! classes.module = dossier.fichier avec dossier le dossier dans lequel est stocké le fichier.py
#! qui sert de module (ici classes) et fichier le nom du fichier module (ici file & arbre_binaire)


def creeFeuille(valeur):
    return creeNoeud(valeur, creeVide(), creeVide())


def hauteur(B):
    return -1 if B.estVide() else 1 + max(hauteur(B.filsG()), hauteur(B.filsD()))


def taille(B):
    return 0 if B.estVide() else 1 + taille(B.filsG()) + taille(B.filsD())


def nbFeuilles(B):
    if B.estVide():
        return 0
    elif B.filsG().estVide() and B.filsD().estVide():
        return 1
    else :
        return nbFeuilles(B.filsG()) + nbFeuilles(B.filsD())


def parcoursProfInfixe(a):
    if not a.estVide():
        parcoursProfInfixe(a.filsG())
        print(a.valRacine(), end=" ")
        parcoursProfInfixe(a.filsD())


def parcoursProfPrefixe(a):
    if not a.estVide():
        print(a.valRacine(), end=" ")
        parcoursProfPrefixe(a.filsG())
        parcoursProfPrefixe(a.filsD())


def parcoursProfPostfixe(a):
    if not a.estVide():
        parcoursProfPostfixe(a.filsG())
        parcoursProfPostfixe(a.filsD())
        print(a.valRacine(), end=" ")


def parcoursLargeur(a):
    fileNoeuds = File()
    fileNoeuds.enfiler(a)
    while not fileNoeuds.fileVide():
        noeudATraiter = fileNoeuds.defiler()
        print(noeudATraiter.valRacine(), end=" ")
        if not noeudATraiter.filsG().estVide() :
            fileNoeuds.enfiler(noeudATraiter.filsG())
        if not noeudATraiter.filsD().estVide() :
            fileNoeuds.enfiler(noeudATraiter.filsD())


# il faut créer un arbre...