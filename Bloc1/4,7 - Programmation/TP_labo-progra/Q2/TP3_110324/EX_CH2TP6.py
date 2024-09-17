class Joueur:
    # Attribut de classe
    nombre_joueurs = 0

    def __init__(self, nom, age, score, niveau):
        # Attributs d'instance
        self.nom = nom
        self.age = age
        self.score = score
        self.niveau = niveau
        # Incrémenter le nombre total de joueurs à chaque nouvelle instance
        Joueur.nombre_joueurs += 1

    def afficher_informations(self):
        print(f"Nom: {self.nom}, Âge: {self.age}, Score: {self.score}, Niveau: {self.niveau}")

    def augmenter_score(self, points):
        self.score += points


class JoueurExpert(Joueur):
    def __init__(self, nom, age, score, niveau, bonus):
        # Appeler le constructeur de la classe parente avec super()
        super().__init__(nom, age, score, niveau)
        # Nouvel attribut d'instance pour la sous-classe
        self.bonus = bonus

    def afficher_bonus(self):
        print(f"Bonus du joueur expert {self.nom}: {self.bonus}")


# Création d'une instance de la classe Joueur
joueur1 = Joueur("John Doe", 25, 100, "Intermédiaire")

# Création d'une instance de la classe JoueurExpert
joueur_expert1 = JoueurExpert("Jane Doe", 30, 150, "Avancé", 50)

# Affichage des informations des joueurs
joueur1.afficher_informations()
joueur_expert1.afficher_informations()

# Augmentation du score du joueur1
joueur1.augmenter_score(20)

# Affichage du bonus du joueur_expert1
joueur_expert1.afficher_bonus()

# Utilisation de __dict__ pour afficher les attributs d'instance
print("Attributs d'instance de joueur1:", joueur1.__dict__)
print("Attributs d'instance de joueur_expert1:", joueur_expert1.__dict__)

# Utilisation de __bases__ pour comprendre la hiérarchie des classes
print("Bases de la classe Joueur:", Joueur.__bases__)
print("Bases de la classe JoueurExpert:", JoueurExpert.__bases__)
