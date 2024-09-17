class Serpent:
    def __init__(self, longueur, couleur, vitesse, veimeux):
        self.longueur = longueur
        self.couleur = couleur
        self.vitesse = vitesse
        self.veimeux = veimeux

    def afficher_info(self):
        print("Longueur : " + str(self.longueur),
              "Couleur : " + self.couleur,
              "Vitesse : " + self.vitesse,
              "Venimeux : " + self.veimeux,
              sep="\n"
              )

    @staticmethod
    def se_deplacer(d):
        print("Le serpent se déplace vers : " + d)

    @staticmethod
    def manger():
        print("Le serpent à mangé")


s1 = Serpent(10, "vert", "très lent", "oui")
s2 = Serpent(100, "rouge", "rapide", "non")

s1.afficher_info()
