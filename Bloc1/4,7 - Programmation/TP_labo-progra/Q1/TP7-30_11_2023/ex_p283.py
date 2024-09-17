def chiffrement_cesar(texte, decalage):
    texte_chiffre = ""
    for caractere in texte:
        if caractere.isalpha():
            minuscule = caractere.islower()
            caractere = (
                chr(
                    (ord(caractere) - ord('a' if minuscule else 'A') + decalage) % 26
                    + ord('a' if minuscule else 'A')
                )
            )
        texte_chiffre += caractere
    return texte_chiffre


def demander_decalage():
    while True:
        try:
            decalage = int(input("Veuillez entrer un nombre de décalage de 1 à 25 : "))
            if 1 <= decalage <= 25:
                return decalage
            else:
                print("La valeur de décalage doit être entre 1 et 25.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def main():
    texte_original = input("Veuillez entrer une ligne de texte à chiffrer : ")
    decalage = demander_decalage()

    texte_chiffre = chiffrement_cesar(texte_original, decalage)

    print("Texte chiffré :", texte_chiffre)


main()
