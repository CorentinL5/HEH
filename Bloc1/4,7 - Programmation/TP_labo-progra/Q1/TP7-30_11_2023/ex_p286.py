def chiffre_de_vie(date):
    chiffres = [int(chiffre) for chiffre in str(date)]
    somme = sum(chiffres)
    while somme >= 10:
        somme = sum(int(chiffre) for chiffre in str(somme))
    return somme

anniversaire = input("Entrez votre anniversaire (au format AAAAMMJJ, ou AAAAJMM, ou MMJDYYYY) : ")
resultat = chiffre_de_vie(anniversaire)

print("Le chiffre de vie pour la date {} est : {}".format(anniversaire, resultat))
