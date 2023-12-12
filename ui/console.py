from classes import ParkingManagementSystem, sleep
from classes.Profits import ProfitsCalculator
import os

def console_interface():
    """
    DOC
    """
    parking_system = ParkingManagementSystem()
    profits_calculator = ProfitsCalculator()
    while True:
        print("\nMenu:")
        print("1. Générer un ticket")
        print("2. Gérer les exceptions")
        print("3. Afficher les places disponibles")
        print("4. Libérer une place")
        print("5. Afficher les bénéfices de la journée")
        print("99. Quitter")
        choice = input("Choisissez une option: ")

        if choice == "1":
            floor = int(input("Entrez l'étage (1-4) : "))
            is_handicap = input("La place est-elle réservée aux personnes handicapées? (Oui/Non): ").lower() == "oui"
            ticket_number = parking_system.generate_ticket(floor, is_handicap)
            if ticket_number:
                print(f"Ticket généré avec succès. Numéro de ticket : {ticket_number}")
            else:
                print("Désolé, toutes les places sont occupées.")
        elif choice == "2":
            floor = int(input("Entrez l'étage (1-4) : "))
            exception_type = input("Type d'exception (gratuite/autre): ").lower()
            parking_system.handle_exception(floor, exception_type)
            print(f"Exception gérée avec succès à l'étage {floor}.")
        elif choice == "3":
            parking_system.show_stat_place()
        elif choice == "4":
            floor = int(input("Entrez l'étage (1-4) : "))
            is_handicap = input("La place était-elle réservée aux personnes handicapées? (Oui/Non): ").lower() == "oui"
            parking_system.liberer_place(floor, is_handicap)
            print(f"La place de l'étage {floor} a été libérée avec succès.")
        elif choice == "5":
            profits = profits_calculator.calculate_daily_profits()
            print(f"\nLes bénéfices de la journée sont de : {profits} €.")
        elif choice == "99":
            sleep(2.5)
            break
        else:
            print("Option invalide. Veuillez réessayer.")
