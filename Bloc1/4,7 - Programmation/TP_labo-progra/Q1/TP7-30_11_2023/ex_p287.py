def recherche_chaine(chaine1, chaine2):
    index = -1
    for char in chaine1:
        index = chaine2.find(char, index + 1)
        if index == -1:
            return "Non"
    return "Oui"

# Exemples d'utilisation
resultat1 = recherche_chaine("dons", "Nabuchodonosor")
print(resultat1)

resultat2 = recherche_chaine("donneur", "Nabuchodonosor")
print(resultat2)
