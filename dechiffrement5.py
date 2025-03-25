from math import gcd


def lire_message(nom_fichier):
    with open(nom_fichier, mode="r", encoding="utf8") as lecteur:
        lignes = lecteur.readlines()
    message = "".join(lignes)
    return message


def trouver_repétitions(liste, min_i=0, min_j=1, d=1):
    for i in range(min_i, len(liste)):
        if i == min_i:
            init = min_j + 1
        else:
            init = i + 1
        for j in range(init, len(liste)):
            if liste[i:i + d] == liste[j:j + d]:
                return i, j


def caractère_fréquent(texte):
    dictionnaire = freq(texte)
    max_fréquence = 0
    caractère_fréquent = ''
    for caractère in dictionnaire:
        if dictionnaire[caractère] > max_fréquence:
            caractère_fréquent = caractère
            max_fréquence = dictionnaire[caractère]
    return ord(' ') - ord(caractère_fréquent)


def freq(texte):
    dictionnaire = {}
    for caractère in texte:
        if caractère not in dictionnaire:
            dictionnaire[caractère] = 1
        else:
            dictionnaire[caractère] += 1
    return dictionnaire


def recherche_répétitions(message, longueur):
    tranches_message = [tuple(message[i:i + longueur]) for i in range(len(message) - longueur)]
    i, j = trouver_repétitions(tranches_message)
    k, l = trouver_repétitions(tranches_message, i, j)
    première_occurrence = (i, j, message[i:i + longueur], message[j:j + longueur])
    deuxième_occurrence = (k, l, message[k:k + longueur], message[l:l + longueur])
    return première_occurrence, deuxième_occurrence


def vigenere(message):
    longueur = 5
    tranches_message = [tuple(message[i:i + longueur]) for i in range(len(message) - longueur)]
    i, j = trouver_repétitions(tranches_message)
    k, l = trouver_repétitions(tranches_message, i, j)
    nb_clé = gcd(j - i, l - k)
    print(nb_clé)

    liste = [[message[i] for i in range(k, len(message), nb_clé)] for k in range(nb_clé)]

    valeurs_clé = []
    for sous_liste in liste:
        valeurs_clé.append(caractère_fréquent(sous_liste))
    print(valeurs_clé)

    liste = [[ord(liste[i][j]) + valeurs_clé[i] for j in range(len(liste[i]))] for i in range(len(liste))]

    for ligne in liste:
        for i in range(len(ligne)):
            ligne[i] = chr(ligne[i])

    liste_finale = []
    for i in range(len(liste[0])):
        for colonne in range(len(liste)):
            if i < len(liste[colonne]):
                liste_finale.append(liste[colonne][i])
    return "".join(liste_finale)

with open("message5.txt", "r", encoding="utf8") as fichier:
    message = fichier.read()
message_décrypté = vigenere(message)
print(message_décrypté)

