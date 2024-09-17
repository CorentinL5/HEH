class Voiture:
    nbr = 0
    coloris = ["Noir", "Blanc", "Rouge", "Jaune", "Bleu",]

    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.couleur = None  # couleur --> gestion de la couleur avec coloris
        self.km = 0

        # gestion nombre de voitures
        Voiture.nbr += 1
        self.changer_coloris()

    def __str__(self):
        return f"""La marque est {self.marque}\nLe modele est {self.modele}\nL'année est {self.annee}\nla couleur est {self.couleur}\nLe kilométrage est {self.km} km\n"""

    def changer_coloris(self):
        x = ""
        for index, couleur in enumerate(self.coloris):
            if index == len(self.coloris)- 1:
                x += f"{couleur}. "
            else:
                x += f"{couleur}, "
        print(f"À Vous de choisir votre couleur parmis ceux-ci: {x}")
        choix_c = None
        while choix_c not in self.coloris :
            choix_c = input("Entrez la couleur souhaitée > ").capitalize()
        self.couleur = choix_c
        print(f"Vous avez mis la couleur de votre voiture sur {self.couleur}")


voit1 = Voiture("Ferrari", "F1", 2024)

print(voit1)

print(vars(voit1))
print(vars(Voiture))

print(type(voit1).__name__)