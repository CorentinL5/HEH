def est_palindrome(texte):
    texte = texte.replace(" ", "").lower()

    # Vérifier si le texte est égal à son inverse
    if texte == texte[::-1]:
        return "C'est un palindrome"
    else:
        return "Ce n'est pas un palindrome"


texte_utilisateur = input("Entrez du texte : ")

resultat = est_palindrome(texte_utilisateur)
print(resultat)
