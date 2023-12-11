import csv

class ProfitsCalculator:
    def __init__(self):
        self.parking_data = self.load_parking_data()

    def load_parking_data(self):
        csv_file = "datacsv\\parking_bxl.csv"
        parking_data = []
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                parking_data.append({
                    'Floor': int(row['Floor']),
                    'SpotNumber': int(row['SpotNumber']),
                    'Available': int(row['Available']),
                    'Reserved': int(row['Reserved']),
                    'Handicap': int(row['Handicap']),
                    'VehicleType': row['VehicleType']
                })
        return parking_data

    def calculate_daily_profits(self):
        price = 3
        day_profits = 0
        for spot in self.parking_data:
            if spot['Available'] == 0:
                day_profits += price
        return day_profits
