class Voiture:
    def __init__(self, co, vi, po, ma, de):
        self.couleur = co  # str
        self.vitesse = vi  # int
        self.portes = po  # int
        self.marque = ma  # str
        self.demarree = de  # bool

    def afficher_info(self):
        print("Couleur : " + self.couleur,
              "Vitesse : " + str(self.vitesse),
              "Portes : " + str(self.portes),
              "Marque : " + self.marque,
              "Demarrée ? : " + str(self.demarree),
              "",
              sep="\n"
              )
    def __str__(self):
        return f"""Couleur : {self.couleur}\nVitesse : {self.vitesse}\nPortes : {self.portes}\nMarque : {self.marque}\nDemarrée ? : {self.demarree}"""

    def avancer(self, d):
        print("La", str(self), "avance vers", d)

    def demarrer(self):
        self.Demarree = True

voit1 = Voiture("rouge", 200, 2, "ferrari", False)

voit1.afficher_info()
voit1.demarrer()
voit1.afficher_info()

print(voit1)