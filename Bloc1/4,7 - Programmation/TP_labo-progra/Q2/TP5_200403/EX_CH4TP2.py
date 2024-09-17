import random


class Vaisseau:
    def __init__(self, nom, modele, longueur, largeur, hauteur, vitesse):
        self.nom = nom
        self.modele = modele
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse = vitesse
        self.integrite = 100

    def __str__(self):
        return f"Nom: {self.nom}, Modèle: {self.modele}, Longueur: {self.longueur}m, Largeur: {self.largeur}m, Hauteur: {self.hauteur}m, Vitesse: {self.vitesse} km/h"

    def accelerer(self, vitesse_supplementaire):
        self.vitesse += vitesse_supplementaire


class Chasseur(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, hauteur, vitesse, armes):
        super().__init__(nom, modele, longueur, largeur, hauteur, vitesse)
        self.armes = armes
        self.furtif = False

    def afficher_armes(self):
        print("Armes du chasseur:")
        for arme in self.armes:
            print(arme)

    def activer_furtivite(self):
        self.furtif = True

    def attaquer(self, vaisseau, arme):
        degats = random.randint(10, 30)  # Simuler des dégâts aléatoires
        vaisseau.integrite -= degats


class VaisseauDeCombat(Vaisseau):
    def __init__(self, nom, modele, longueur, largeur, hauteur, vitesse, armure):
        super().__init__(nom, modele, longueur, largeur, hauteur, vitesse)
        self.armure = armure

    def afficher_armure(self):
        print(f"Niveau d'armure du vaisseau de combat {self.nom}: {self.armure}")

    def activer_bouclier(self):
        self.armure += 100


class FlotteSpatiale:
    def __init__(self, nom):
        self.nom = nom
        self.vaisseaux = []

    def ajouter_vaisseau(self, vaisseau):
        self.vaisseaux.append(vaisseau)

    def supprimer_vaisseau(self, vaisseau):
        self.vaisseaux.remove(vaisseau)

    def afficher_vaisseaux(self):
        print(f"Vaisseaux de la flotte {self.nom}:")
        for vaisseau in self.vaisseaux:
            print(vaisseau)

    def attaquer_flotte(self, flotte_cible):
        print(f"La flotte {self.nom} attaque la flotte {flotte_cible.nom} !")
        for vaisseau in self.vaisseaux:
            cible = random.choice(flotte_cible.vaisseaux)
            print(f"{vaisseau.nom} attaque {cible.nom} !")
            vaisseau.attaquer(cible, vaisseau.armes[0])  # Pour simplifier, nous prenons la première arme


# Création de quelques vaisseaux et armes pour les tests
v1 = Vaisseau("Vaisseau 1", "Modèle 1", 50, 30, 20, 500)
v2 = Vaisseau("Vaisseau 2", "Modèle 2", 60, 40, 25, 600)

chasseur1 = Chasseur("Chasseur 1", "Modèle A", 20, 10, 10, 800, ["Laser", "Missile"])
chasseur2 = Chasseur("Chasseur 2", "Modèle B", 25, 15, 12, 900, ["Canon plasma"])

vaisseau_combat1 = VaisseauDeCombat("Vaisseau Combat 1", "Modèle X", 70, 50, 30, 400, 200)
vaisseau_combat2 = VaisseauDeCombat("Vaisseau Combat 2", "Modèle Y", 80, 60, 35, 450, 250)

# Création d'une flotte spatiale et ajout des vaisseaux
flotte1 = FlotteSpatiale("Flotte 1")
flotte1.ajouter_vaisseau(v1)
flotte1.ajouter_vaisseau(v2)
flotte1.ajouter_vaisseau(chasseur1)
flotte1.ajouter_vaisseau(chasseur2)
flotte1.ajouter_vaisseau(vaisseau_combat1)
flotte1.ajouter_vaisseau(vaisseau_combat2)

# Affichage des vaisseaux de la flotte
flotte1.afficher_vaisseaux()

# Test d'accélération d'un vaisseau
print("\nAccélération de Chasseur 1...")
chasseur1.accelerer(100)
print(f"La nouvelle vitesse de Chasseur 1 est de {chasseur1.vitesse} km/h")

# Test d'attaque d'un chasseur
print("\nAttaque de Chasseur 1 contre Vaisseau 1...")
chasseur1.attaquer(v1, chasseur1.armes[0])
print(f"L'intégrité de Vaisseau 1 après l'attaque est de {v1.integrite}%")

# Test d'activation de la furtivité d'un chasseur
print("\nActivation de la furtivité de Chasseur 2...")
chasseur2.activer_furtivite()
print(f"Chasseur 2 est en mode furtif: {chasseur2.furtif}")

# Test d'activation du bouclier d'un vaisseau de combat
print("\nActivation du bouclier de Vaisseau Combat 1...")
vaisseau_combat1.activer_bouclier()
print(f"Niveau d'armure de Vaisseau Combat 1 après activation du bouclier: {vaisseau_combat1.armure}")

# Création d'une deuxième flotte spatiale pour le test d'attaque
flotte2 = FlotteSpatiale("Flotte 2")
flotte2.ajouter_vaisseau(Vaisseau("Vaisseau ennemi 1", "Modèle Z", 70, 50, 30, 400))
flotte2.ajouter_vaisseau(Vaisseau("Vaisseau ennemi 2", "Modèle W", 80, 60, 35, 450))

# Test d'attaque d'une flotte vers une autre flotte
print("\nLa Flotte 1 attaque la Flotte 2 !")
flotte1.attaquer_flotte(flotte2)
