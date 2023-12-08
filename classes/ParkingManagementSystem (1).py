import csv

class ParkingManagementSystem:
    def __init__(self, fileImport):
        self.data_file = fileImport
        self.load_data()

    def load_data(self):
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
        Doc
        """
        with open(self.data_file, 'w', newline='') as file:
            fieldnames = ['Floor', 'SpotNumber', 'Available', 'Reserved', 'Handicap', 'VehicleType']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for spot in self.parking_spots:
                writer.writerow(spot)
    
    def place_libre(self, Floor):
        for spot in self.parking_spots:
            if spot["Floor"] == int(Floor):
                if spot["Available"] == 1:
                    return spot["SpotNumber"]
        
    def generate_ticket(self, Floor, spotNumber, is_handicap=False, vehicle_type=None) -> int:
        for spot in self.parking_spots:
            if spot["Floor"] == int(Floor):
                if spot["SpotNumber"] == spotNumber and spot["Available"] == 1 and is_handicap:
                    spot["Available"] = 0
                    spot["Reserved"] = 1
                    spot["VehicleType"] = vehicle_type
                    self.save_data()
                    return print(f"Le tickets pour la place {spotNumber} a été généré avec succès")
        return None

    def handle_exception(self, floor, exception_type):
        # Traitement des exceptions
        pass

    def liberer_place(self, placeNumber):
        for spot in self.parking_spots:
            if spot["SpotNumber"] == placeNumber and spot["Reserved"] == 1:
                spot["Available"] = "1"
                spot["Reserved"] = "0"
                spot["Handicap"] = "0"
                spot["VehicleType"] = ""
                self.save_data()  # Sauvegarde les données mises à jour dans le fichier CSV
                return True 


    def show_stat_place(self):
        print("\nStatut des places dans chaque étage:")
        for floor in set(spot["Floor"] for spot in self.parking_spots):
            reserved_spots = sum(spot["Reserved"] for spot in self.parking_spots if spot["Floor"] == floor)
            available_spots = sum(spot["Available"] for spot in self.parking_spots if spot["Floor"] == floor)
            print(f"Étage {floor}: {reserved_spots} places réservées, {available_spots} places libres")