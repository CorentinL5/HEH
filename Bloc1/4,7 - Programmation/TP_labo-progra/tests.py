from datetime import datetime, timedelta


def generate_dates(start_date, days):
    # Initialiser la liste pour stocker les dates
    dates = []

    # Convertir la date de départ en objet datetime
    current_date = datetime.strptime(start_date, '%d-%m-%Y')

    # Boucle pour générer les dates sur "days" jours
    for i in range(days):
        # Ajouter les heures spécifiques pour chaque jour
        dates.append(current_date.replace(hour=13, minute=0, second=0))
        dates.append(current_date.replace(hour=16, minute=0, second=0))
        dates.append(current_date.replace(hour=20, minute=0, second=0))

        # Passer au jour suivant
        current_date += timedelta(days=1)

    # Afficher les dates au format souhaité
    for date in dates:
        print(date.strftime('%d-%m-%Y  %H:%M:%S'))


# Exemple d'utilisation
start_date = "09-09-2024"
days = 7

generate_dates(start_date, days)
