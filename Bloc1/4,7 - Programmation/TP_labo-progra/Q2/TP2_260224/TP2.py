from datetime import datetime

current_year = datetime.now().year


class Humain:
    """
    Classe représentant un être humain.

    Attributes:
        nom (str): Le nom de l'humain.
        prenom (str): Le prénom de l'humain.
        annee_de_naissance (int): L'année de naissance de l'humain.
        enfants (list): La liste des enfants de l'humain.
    """
    def __init__(self, nom, prenom, annee_de_naissance, enfants=None):
        """
        Constructeur lors d'une instance de la classe Humain.

        Args:
            nom (str): Le nom de l'humain.
            prenom (str): Le prénom de l'humain.
            annee_de_naissance (int): L'année de naissance de l'humain.
            enfants (list): La liste des enfants de l'humain.

        Raises:
            ValueError: Si l'année de naissance n'est pas un nombre entier.
        """
        if enfants is None:
            enfants = []
        self.nom = str(nom)  # str
        self.prenom = str(prenom)  # str

        try:
            self.annee_de_naissance = int(annee_de_naissance)  # int
        except ValueError:
            print(f"Erreur: l'année de naissance doit être un nombre entier. Annee_de_naissance mis à {current_year}.")
            self.annee_de_naissance = current_year

        self.enfants = []
        for i in enfants:
            if isinstance(i, Humain):
                self.enfants.append(i)  # Ajout à la liste
            else:
                print(f"{i} n'est pas une instance de la classe Humain.")

    def calculer_age(self):
        """
        Calcule l'âge de l'humain en fonction de l'année en cours.

        Returns:
            int: L'âge de l'humain.
        """
        return current_year - self.annee_de_naissance

    def se_presenter(self):
        """
        Retourne une chaîne de caractères représentant la présentation de l'humain.

        Returns:
            str: La présentation de l'humain.
        """
        return f"Nom : {self.nom}\nPrénom : {self.prenom}\nAnnée de naissance : {self.annee_de_naissance}"

    def reconnaissance_parentale(self, humain):
        """
        Ajoute un enfant à la liste des enfants de l'humain.

        Args:
            humain (Humain): L'instance de la classe Humain à ajouter comme enfant.
        """
        self.enfants.append(humain)

    def voire_reconnaissance_parentale(self):
        """
         Affiche les informations sur les enfants de l'humain.
         """
        for i in self.enfants:
            print(i.nom, i.prenom, i.annee_de_naissance)


humain1 = Humain("Smith", "Jean", 1970, [])
humain2 = Humain("Smith", "Pol", 1999, [humain1])

humain2.voire_reconnaissance_parentale()
print("--------------")
humain1.reconnaissance_parentale(humain2)
humain1.voire_reconnaissance_parentale()
