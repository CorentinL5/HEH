import re


def check_date_format(date):
    """
    Vérifie si la date est au format AAAA-MM-JJ
    :param date: date à vérifier
    :return: True si la date est au format AAAA-MM-JJ, False sinon
    """
    regex = r'^\d{4}-\d{2}-\d{2}$'  # Format AAAA-MM-JJ
    if re.match(regex, date):
        return True
    else:
        return False


class Vehicle:
    """
    Classe Vehicle, permet de créer des véhicules
    """
    n_vehicles = 0  # Compteur de véhicules instancié à 0

    def __init__(self, make, model, year, daily_rate):
        """
        initialisation de la classe Vehicle avec 4 attributs
        :param make: # Marque de la voiture (str)
        :param model: # Modèle de la voiture (str)
        :param year: # Année de contruction de la voiture (int)
        :param daily_rate: # Prix de location par jour (int)
        """
        if not isinstance(year, int) or year <= 0:
            raise ValueError("L'année doit être un entier positif.")
        if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
            raise ValueError("Le taux journalier doit être un nombre positif.")

        self._id = Vehicle.n_vehicles  # Assigner un identifiant unique
        Vehicle.n_vehicles += 1
        self._make = make
        self._model = model
        self._year = year
        self._daily_rate = daily_rate
        self._km_distance = 0

    def __str__(self):
        """
        :return: id : make model year daily_rate$/jour
        """
        return f"{self._id} : {self._make} {self._model} {self._year} ({self._daily_rate}$/jour)"

    def check_odometer(self):
        """
        :return: "km_distance/km"
        """
        return f"{self._km_distance}/km)"


class Car(Vehicle):
    """
    Sous class Car de Vehicle
    """
    def __init__(self, make, model, year, daily_rate, num_doors, top_speed):
        """
        initialisation de la classe Car avec 6 attributs
        :param make: # Marque de la voiture (str)
        :param model: # Modèle de la voiture (str)
        :param year: # Année de contruction de la voiture (int)
        :param daily_rate: # Prix de location par jour (int)
        :param num_doors: # Nombre de portes (int)
        :param top_speed: # Vitesse max (int)
        """
        super().__init__(make, model, year, daily_rate)
        if not isinstance(num_doors, int) or num_doors <= 0:
            raise ValueError("Le nombre de portes doit être un entier positif.")
        if not isinstance(top_speed, (int, float)) or top_speed <= 0:
            raise ValueError("La vitesse maximale doit être un nombre positif.")

        self._num_doors = num_doors
        self._top_speed = top_speed

    def __str__(self):
        """
        :return: id : make model year daily_rate$/jour \n|-> Portes: num_doors, Vitesse Max: top_speed
        """
        return super().__str__() + f"\n|-> Portes: {self._num_doors}, Vitesse Max: {self._top_speed}"


class Truck(Vehicle):
    def __init__(self, make, model, year, daily_rate, payload_capacity, num_axles):
        """
        initialisation de la classe Truck avec 6 attributs
        :param make: # Marque de la voiture (str)
        :param model: # Modèle de la voiture (str)
        :param year: # Année de contruction de la voiture (int)
        :param daily_rate: # Prix de location par jour (int)
        :param payload_capacity: # capacité de stockage max (int)
        :param num_axles: # nombres d'axes = n° roues/2 (int)
        """
        super().__init__(make, model, year, daily_rate)
        if not isinstance(payload_capacity, int) or payload_capacity <= 0:
            raise ValueError("La capacité maximal du camion doit être un entier positif.")
        if not isinstance(num_axles, int) or num_axles <= 0:
            raise ValueError("Le nombre d'axes doit être un nombre enter positif.")

        self._payload_capacity = payload_capacity
        self._num_axles = num_axles

    def __str__(self):
        """
        :return: id : make model year daily_rate$/jour \n|-> Capactité: payload_capacity, Axes: num_axles
        """
        return super().__str__() + f"\n|-> Capactité: {self._payload_capacity}, Axes: {self._num_axles}"


class RentalAgreement:
    def __init__(self, vehicle, start_date, end_date, daily_rate):
        """
        initialisation de la classe RentalAgreement avec 4 attributs
        :param vehicle: # Vehicule du contrat
        :param start_date: # date de début de contrat
        :param end_date: # date de fin de contrat
        :param daily_rate: # Prix de location par jour (int)
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Le véhicule doit être une instance de la classe Vehicle.")
        if not check_date_format(start_date):
            raise ValueError("La date de début n'est pas au format AAAA-MM-JJ.")
        if not check_date_format(end_date):
            raise ValueError("La date de fin n'est pas au format AAAA-MM-JJ.")
        if not isinstance(daily_rate, (int, float)) or daily_rate <= 0:
            raise ValueError("Le taux journalier doit être un nombre positif.")

        self._vehicle = vehicle
        self._start_date = start_date
        self._end_date = end_date
        self._daily_rate = daily_rate

    def total_cost(self):
        """
        Cout total de la location
        :return: rent$ for total_days days
        """
        start_d = self._start_date.split("-")
        end_d = self._end_date.split("-")
        years = int(end_d[0]) - int(start_d[0])
        months = int(end_d[1]) - int(start_d[1])
        days = int(end_d[2]) - int(start_d[2])
        total_days = years * 356 + months * 30 + days
        rent = self._daily_rate * total_days
        return f"{rent}$ for {total_days} days"


class RentalSystem:
    """
    Class RentalSystem, permet de crée un système de location avec des voitures et des contrats
    """
    def __init__(self, vehicles, agreements):
        """
        initialisation de la classe RentalSystem avec 2 attributs
        :param vehicles: Véhicules dans ce système (list)
        :param agreements: contrats du système (list)
        """
        if not isinstance(vehicles, list):
            raise ValueError("Les véhicules doivent être ajoutés en liste.")
        else:
            for vehicle in vehicles:
                if not isinstance(vehicle, Vehicle):
                    raise ValueError("Le véhicule doit être une instance de la classe Vehicle.")
        if not isinstance(agreements, list):
            raise ValueError("Les contrats doivent être ajoutés en liste.")

        self._vehicles = vehicles
        self._agreements = agreements

    def add_vehicle(self, vehicle):
        """
        ajouter un véhicule au sytème
        :param vehicle: véhicule à ajouter au système
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Le véhicule doit être une instance de la classe Vehicle.")
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        """
        retirer un véhicule du système
        :param vehicle: véhicule à retirer du système
        """
        if not isinstance(vehicle, Vehicle):
            raise ValueError("Le véhicule doit être une instance de la classe Vehicle.")
        if vehicle in self._vehicles:
            self._vehicles.remove(vehicle)
        else:
            print("Le véhicule n'est pas dans ce système")

    def list_vehicles(self):
        """
        lister les véhicules
        return: listed_vehicle
        """
        listed_vehicle = []
        for vehicle in self._vehicles:
            listed_vehicle.append("\n|-> " + str(vehicle)+"\n")
        return "\n------------------------------\nVéhicules dans le système : \n" + "".join(listed_vehicle)

    def create_agreement(self, vehicle, start_date, end_date, daily_rate):
        """
        Créer un contrat de location
        :param vehicle: véhicule à louer
        :param start_date: date de début de location
        :param end_date: date de fin de location
        :param daily_rate: taux journalier de location
        """
        for v in self._vehicles:
            if v == vehicle:
                agreement = RentalAgreement(vehicle, start_date, end_date, daily_rate)
                self._agreements.append(agreement)
                print(f"Contrat de location créé pour le véhicule suivant :\n|-> {vehicle}.")
                return
        print(f"Le véhicule {vehicle} n'est pas disponible dans le système de location.")

    def list_agreements(self):
        """
        lister les contrats de location
        return: listed_agreements
        """
        listed_agreements = []
        for agreement in self._agreements:
            listed_agreements.append(str(agreement))
        return "Contrats de location dans le système : " + ", ".join(listed_agreements)

    def return_vehicle(self, vehicle):
        """
        Marquer un véhicule comme retourné
        :param vehicle: véhicule à marquer comme retourné
        """
        for agreement in self._agreements:
            if agreement.vehicle == vehicle:
                self._agreements.remove(agreement)
                print(f"Le véhicule {vehicle} a été marqué comme retourné.")
                return
        print(f"Le véhicule {vehicle} n'a pas de contrat de location en cours.")


# Créer des instances de véhicules (voitures et camions)
car1 = Car("Toyota", "Corolla", 2018, 50, 4, 180)
car2 = Car("Honda", "Civic", 2020, 60, 4, 200)
truck1 = Truck("Ford", "F150", 2019, 80, 2000, 4)
truck2 = Truck("Chevrolet", "Silverado", 2021, 90, 2500, 6)

# Instancier le système de location
c_vehicles = [car1, car2, truck1, truck2]
c_agreements = []
rental_system = RentalSystem(c_vehicles, c_agreements)


# Créer des contrats de location pour différents véhicules et différentes durées
rental_system.create_agreement(car1, "2024-04-03", "2024-04-10", 50)
rental_system.create_agreement(car2, "2024-04-05", "2024-04-12", 60)
rental_system.create_agreement(truck1, "2024-04-04", "2024-04-11", 80)
rental_system.create_agreement(truck2, "2024-04-06", "2024-04-13", 90)

# Afficher les informations des véhicules
print(rental_system.list_vehicles())
