# Les monstres

class Monstre:
    def __init__(self, race, classe, nom, age, dangereux):
        self.race = str(race)  # Race du monstre (Dragon, Gobelin, Fantômes, etc.)
        self.classe = str(classe)  # Type de monstre (Humanoïdes, Mort-vivants, Aquatiques, etc.)
        self.nom = str(nom)  # Nom du monstre (str)

        try:
            self.age = int(age)  # Âge du monstre (int)
        except ValueError:
            print("Erreur: L'âge doit être un nombre entier, Âge mis à 0.")
            self.age = 0

        try:
            self.dangereux = bool(dangereux)  # Indique si le monstre est dangereux (bool)
        except ValueError:
            print("Erreur: La valeur de dangerosité doit être un booléen. Réglé à False.")
            self.dangereux = False

    def afficher_info(self):
        print("race : " + self.race,
              "type : " + self.classe,
              "nom : " + self.nom,
              "age : " + str(self.age),
              "dangereux ? : " + str(self.dangereux),
              "",
              sep="\n"
              )

    def vieillir(self, age_en_plus=1):
        self.age += age_en_plus
        print(f"Votre monstre {self.nom} à pris {age_en_plus} d'années.")

    def devenir_dangereux(self):
        if self.dangereux:
            print("Votre monstre est déjà dangeureux")
        else:
            self.dangereux = True
            print("Votre monstre est devenu dangeureux")


monstre1 = Monstre("Dragon", "Humaoïde")
