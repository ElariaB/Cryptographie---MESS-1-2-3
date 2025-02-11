with open('message1.txt', 'r', encoding ="utf-8") as file:
    message = file.read()
    #%%

def lire_message(fichier):
    with open(fichier, 'r', encoding="utf-8") as file:
        return file.read()

def creer_grille(message, longueur_cle):
    colonnes = longueur_cle
    lignes = len(message) // colonnes
    if len(message) % colonnes != 0:
        lignes += 1

    grille = [[''] * colonnes for _ in range(lignes)]
    index = 0
    for row in range(lignes):
        for col in range(colonnes):
            if index < len(message):
                grille[row][col] = message[index]
                index += 1
    return grille

def transposer_grille(grille):
    lignes = len(grille)
    colonnes = len(grille[0])
    grille_transposee = [[''] * lignes for _ in range(colonnes)]
    for row in range(lignes):
        for col in range(colonnes):
            grille_transposee[col][row] = grille[row][col]
    return grille_transposee

def lire_grille_transposee(grille_transposee):
    message_dechiffre = ''.join([''.join(row) for row in grille_transposee])
    return message_dechiffre

# Lire le message chiffré depuis le fichier
message_chiffre = lire_message('message1.txt')

# Définir la longueur de la clé (à ajuster selon votre cas)
longueur_cle = 334

# Créer la grille
grille = creer_grille(message_chiffre, longueur_cle)

# Transposer la grille
grille_transposee = transposer_grille(grille)

# Lire la grille transposée pour obtenir le message déchiffré
message_dechiffre = lire_grille_transposee(grille_transposee)

print(message_dechiffre)
