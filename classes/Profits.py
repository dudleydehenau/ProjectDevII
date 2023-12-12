import csv
from classes.ParkingManagementSystem import ParkingManagementSystem

class ProfitsCalculator:
    def __init__(self):
        pass

    def calculate_daily_profits(self):
        parking_data = ParkingManagementSystem.load_data()
        price = 3
        day_profits = 0
        for spot in parking_data:
            if spot['Available'] == 0:
                day_profits += price
        return print(day_profits)

