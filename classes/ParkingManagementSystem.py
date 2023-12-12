import csv

class ParkingManagementSystem:
    def __init__(self, fileImport):
        """
        Constructeur de la classe ParkingManagementSystem.

        PRE: fileImport est une chaîne de caractères non vide représentant le chemin du fichier CSV.
        RAISE: ValueError si fileImport n'est pas une chaîne de caractères non vide.
        """
        if not isinstance(fileImport, str) or not fileImport:
            raise ValueError("Le chemin du fichier doit être une chaîne de caractères non vide.")
        self.data_file = fileImport
        self.load_data()

    def load_data(self):
        """
        Charge les données à partir du fichier CSV spécifié dans le constructeur.

        POST: Les données du fichier CSV sont chargées dans self.parking_spots.
        RAISE: ValueError si le contenu du fichier n'est pas conforme aux attentes.
        """
        self.parking_spots = []
        with open(self.data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                spot = {
                    "Floor": int(row['Floor']),
                    "SpotNumber": int(row['SpotNumber']),
                    "Available": int(row['Available']),
                    "Reserved": int(row['Reserved']),
                    "Handicap": int(row['Handicap']),
                    "VehicleType": row['VehicleType']
                }
                self.parking_spots.append(spot)

    def save_data(self):
        """
        Enregistre les données dans le fichier CSV spécifié dans le constructeur.
        """
        with open(self.data_file, 'w', newline='') as file:
            fieldnames = ['Floor', 'SpotNumber', 'Available', 'Reserved', 'Handicap', 'VehicleType']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for spot in self.parking_spots:
                writer.writerow(spot)
    
    def place_libre(self, Floor):
        """
        Trouve une place libre dans l'étage spécifié.

        PRE: Floor est un entier positif.
        POST: Retourne le numéro de la place libre dans l'étage spécifié ou None si aucune place n'est disponible.
        """
        for spot in self.parking_spots:
            if spot["Floor"] == int(Floor):
                if spot["Available"] == 1:
                    return spot["SpotNumber"]
        return None
        
    def generate_ticket(self, floor, spotNumber, is_handicap=False, vehicle_type=None):
        """
        Génère un ticket pour réserver une place.

        PRE: floor et spotNumber sont des entiers positifs.
             is_handicap est un booléen.
             vehicle_type est une chaîne de caractères ou None.
        POST: Retourne le numéro de la place réservée si la réservation est réussie, sinon retourne None.
        RAISE: ValueError si floor ou spotNumber ne sont pas des entiers positifs.
        """
        if not all(isinstance(arg, int) and arg > 0 for arg in (floor, spotNumber)):
            raise ValueError("floor et spotNumber doivent être des entiers positifs.")
        
        for spot in self.parking_spots:
            if spot["Floor"] == floor and spot["SpotNumber"] == spotNumber and spot["Available"] == 1:
                spot["Available"] = 0
                spot["Reserved"] = 1
                spot["Handicap"] = int(is_handicap)
                spot["VehicleType"] = vehicle_type
                self.save_data()
                return spotNumber
        return None

    def liberer_place(self, placeNumber):
        """
        Libère une place spécifiée.

        PRE: placeNumber est un entier positif et la disponibilité (Available) doit valoir 1.
        POST: Retourne True si la place a été libérée avec succès, sinon retourne False.
        RAISE: ValueError si placeNumber n'est pas un entier positif ou si la disponibilité (Available) n'est pas égale à 1.
        """
        if not isinstance(placeNumber, int) or placeNumber <= 0:
            raise ValueError("placeNumber doit être un entier positif.")

        found_spot = False
        for spot in self.parking_spots:
            if spot["SpotNumber"] == placeNumber and spot["Reserved"] == 1 and spot["Available"] == 1:
                spot["Available"] = 1
                spot["Reserved"] = 0
                spot["Handicap"] = 0
                spot["VehicleType"] = ""
                self.save_data()
                found_spot = True
                break

        if not found_spot:
            raise ValueError("La place spécifiée n'est pas réservée ou n'est pas disponible.")
        
        return True


    def show_stat_place(self):
        """
        Affiche le statut des places dans chaque étage.
        """
        print("\nStatut des places dans chaque étage:")
        for floor in set(spot["Floor"] for spot in self.parking_spots):
            reserved_spots = sum(spot["Reserved"] for spot in self.parking_spots if spot["Floor"] == floor)
            available_spots = sum(spot["Available"] for spot in self.parking_spots if spot["Floor"] == floor)
            print(f"Étage {floor}: {reserved_spots} places réservées, {available_spots} places libres")

    def calculate_daily_profits(self):
        """
        Calcule les profits quotidiens en fonction des places occupées.

        PRE: parking_spots doit contenir toutes les informations sur les places de parking.
        POST: Retourne le montant total des profits.
        RAISE: ValueError si parking_spots n'est pas une liste valide.
        """
        if not isinstance(self.parking_spots, list):
            raise ValueError("parking_spots doit être une liste valide contenant les informations sur les places de parking.")

        price = 3.0
        day_profits = 0
        for spot in self.parking_spots:
            if spot['Available'] == 0:
                day_profits += price
        return day_profits

