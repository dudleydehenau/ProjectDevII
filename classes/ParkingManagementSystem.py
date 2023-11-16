class ParkingManagementSystem:
    def __init__(self):
        self.ticket_counter = 1
        self.parking_spaces = {
            1: {"available": 50, "reserved": 0},
            2: {"available": 50, "reserved": 0},
            3: {"available": 50, "reserved": 0},
            4: {"available": 50, "reserved": 0}
        }
        self.handicap_spaces = {
            1: {"available": 2, "reserved": 0},
            2: {"available": 2, "reserved": 0},
            3: {"available": 2, "reserved": 0},
            4: {"available": 2, "reserved": 0}
        }

    def generate_ticket(self, floor, is_handicap=False) -> int:
        if self.parking_spaces[floor]["available"] > 0:
            ticket_number = self.ticket_counter
            self.ticket_counter += 1
            self.parking_spaces[floor]["available"] -= 1
            self.parking_spaces[floor]["reserved"] += 1

            if is_handicap:
                self.handicap_spaces[floor]["reserved"] += 1
                self.handicap_spaces[floor]["available"] -= 1

            return ticket_number
        else:
            return None

    def handle_exception(self, floor, exception_type):
        if exception_type == "free":
            # Suite a faire
            pass
        elif exception_type == "other":
            # Suite a faire
            pass
    
    def liberer_place(self, floor, is_handicap=False):
        if is_handicap:
            self.handicap_spaces[floor]["reserved"] -= 1
            self.handicap_spaces[floor]["available"] += 1
        else:
            self.parking_spaces[floor]["available"] += 1
            self.parking_spaces[floor]["reserved"] -= 1

    def show_stat_place(self):
        print("\nStatut des places dans chaque étage:")
        for floor, spaces in self.parking_spaces.items():
            reserved_spaces = spaces["reserved"] 
            available_spaces = spaces["available"]
            print(f"Étage {floor}: {reserved_spaces} places réservées, {available_spaces} places libres")
