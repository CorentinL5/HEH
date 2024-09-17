chiffres_ascii = [
    [
        "  ###  ",
        " #   # ",
        "#     #",
        "#     #",
        "#     #",
        " #   # ",
        "  ###  "
    ],  # 0
    [
        "   #   ",
        "  ##   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        " ##### "
    ],  # 1
    [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "#      ",
        "#      ",
        "#######"
    ],  # 2
    [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "      #",
        "#     #",
        " ##### "
    ],  # 3
    [
        "#      ",
        "#    # ",
        "#    # ",
        "#######",
        "     # ",
        "     # ",
        "     # "
    ],  # 4
    [
        "#######",
        "#      ",
        "#      ",
        " ##### ",
        "      #",
        "#     #",
        " ##### "
    ],  # 5
    [
        " ##### ",
        "#      ",
        "#      ",
        " ##### ",
        "#     #",
        "#     #",
        " ##### "
    ],  # 6
    [
        "#######",
        "     # ",
        "    #  ",
        "   #   ",
        "  #    ",
        " #     ",
        "#      "
    ],  # 7
    [
        " ##### ",
        "#     #",
        "#     #",
        " ##### ",
        "#     #",
        "#     #",
        " ##### "
    ],  # 8
    [
        " ##### ",
        "#     #",
        "#     #",
        " ######",
        "      #",
        "#     #",
        " ##### "
    ]  # 9
]


def afficher_nombre_sept_segments_ascii(nombreaafficher):
    list_chiffres = [int(ch) for ch in str(nombreaafficher)]
    for ligne in range(7):
        ligne_affichage = ""
        for chiffre in list_chiffres:
            ligne_affichage += chiffres_ascii[chiffre][ligne] + "  "
        print(ligne_affichage)


nombre = 0
while nombre == 0:
    try:
        nombre = int(input("Entrez un nombre non négatif : "))
    except ValueError:
        print("Ce n'est pas un entier. Veuillez entrer un nombre entier.")


afficher_nombre_sept_segments_ascii(nombre)
