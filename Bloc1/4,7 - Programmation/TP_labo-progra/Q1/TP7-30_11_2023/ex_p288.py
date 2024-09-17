def est_sudoku_valide(sudoku):
    # Vérifier les lignes
    for ligne in sudoku:
        if not est_sequence_valide(ligne):
            return "Non"

    # Vérifier les colonnes
    for colonne in range(9):
        if not est_sequence_valide([sudoku[i][colonne] for i in range(9)]):
            return "Non"

    # Vérifier les sous-carrés
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sous_carre = [sudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not est_sequence_valide(sous_carre):
                return "Non"

    return "Oui"

def est_sequence_valide(sequence):
    # Vérifier si la séquence contient tous les chiffres de 0 à 9 une seule fois
    chiffres = set()
    for chiffre in sequence:
        if chiffre < 0 or chiffre > 9 or chiffre in chiffres:
            return False
        chiffres.add(chiffre)
    return True

# Testez votre code avec des données d'exemple
sudoku_valide = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(est_sudoku_valide(sudoku_valide))
