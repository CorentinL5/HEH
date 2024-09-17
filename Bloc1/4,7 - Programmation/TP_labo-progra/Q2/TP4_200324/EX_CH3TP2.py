class Robot:
    _nombre_robots = 0  # variable de classe pour suivre le nombre de robots

    def __init__(self, nom, batterie=100):
        self.nom = nom
        Robot._nombre_robots += 1
        self.numero_serie = Robot._nombre_robots
        self.batterie = min(max(0, batterie), 100)  # Assurer que la batterie est entre 0 et 100

    def se_deplacer(self, direction):
        if self.batterie > 0:
            print(f"{self.nom} se déplace vers {direction}.")
            self.batterie -= 1
        else:
            print("Batterie vide, impossible de se déplacer.")

    def se_recharger(self):
        self.batterie = min(100, self.batterie + 10)  # Recharge de 10%, max 100%

    def __str__(self):
        return f"Robot {self.nom} (Numéro de série: {self.numero_serie}, Batterie: {self.batterie}%)"


class Drone(Robot):
    def __init__(self, nom, portee_vol, camera_embarquee=False, batterie=100):
        super().__init__(nom, batterie)
        self.portee_vol = portee_vol
        self.camera_embarquee = camera_embarquee

    def vol_stationnaire(self, altitude):
        if self.batterie > 0:
            print(f"{self.nom} effectue un vol stationnaire à {altitude} mètres d'altitude.")
            self.batterie -= 5  # Le vol stationnaire consomme plus de batterie
        else:
            print("Batterie vide, impossible de voler.")

    def __str__(self):
        return f"Drone {self.nom} (Numéro de série: {self.numero_serie}, Batterie: {self.batterie}%, Portée de vol: {self.portee_vol}m, Caméra embarquée: {self.camera_embarquee})"


class RobotDanseur(Robot):
    def __init__(self, nom, niveau_maitrise, partenaire=None, danses_connu=[], batterie=100):
        super().__init__(nom, batterie)
        self.niveau_maitrise = niveau_maitrise
        self.partenaire = partenaire
        self.danses_connu = danses_connu

    def danser_avec(self, partenaire):
        if self.partenaire == partenaire:
            print(f"{self.nom} danse avec {partenaire.nom}.")
        else:
            print(f"{self.nom} ne peut pas danser avec {partenaire.nom}, ils ne sont pas partenaires.")

    def __str__(self):
        return f"RobotDanseur {self.nom} (Numéro de série: {self.numero_serie}, Batterie: {self.batterie}%, Niveau de maîtrise: {self.niveau_maitrise}, Danses connues: {', '.join(self.danses_connu)})"


# Tests
robot1 = Robot("R1")
print(robot1)

drone1 = Drone("D1", 500, True)
print(drone1)

robot_danseur1 = RobotDanseur("RD1", "Avancé", danses_connu=["Salsa", "Tango"])
robot_danseur2 = RobotDanseur("RD2", "Débutant", danses_connu=["Salsa"])

print(robot_danseur1)
print(robot_danseur2)

robot_danseur1.danser_avec(robot_danseur2)
