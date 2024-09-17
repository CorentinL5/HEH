def sont_anagrammes(chaine1, chaine2):
    liste1 = list(chaine1.lower().replace(" ", ""))
    liste2 = list(chaine2.lower().replace(" ", ""))

    liste1.sort()
    liste2.sort()

    return liste1 == liste2


texte1 = input("Entrez le premier texte : ")
texte2 = input("Entrez le deuxième texte : ")

if sont_anagrammes(texte1, texte2):
    print("Anagrammes")
else:
    print("Pas d'anagrammes")
