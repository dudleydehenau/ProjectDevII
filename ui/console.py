from classes.ParkingManagementSystem import ParkingManagementSystem
from time import sleep
import os

def console_interface():
    """
    DOC
    """
    script_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(script_dir)
    data_file = os.path.join(project_dir, 'datacsv', 'parking_bxl.csv')
    parking_system = ParkingManagementSystem(data_file)
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
            placeNumber_input = input("Entrez, si vous le souhaitez, un numéro de place. (vide = aléatoire) :")
            if placeNumber_input.strip():
                placeNumber = int(placeNumber_input)
            else:
                for spot in parking_system.parking_spots:
                    if spot["Floor"] == floor and spot["Available"] == 1:
                        placeNumber = spot["SpotNumber"]
                        break
                else:
                    print(f"Aucune place disponible à l'étage {floor}.")
                    placeNumber = None
            is_handicap = input("La place est-elle réservée aux personnes handicapées? (Oui/Non): ").lower() == "oui"
            vehicule_type = input("Entrez le type de véhicule garé. (vide pour ignorer) :") 
            ticket_number = parking_system.generate_ticket(floor, placeNumber, is_handicap, vehicule_type)
            if ticket_number:
                print(f"Ticket généré avec succès. Numéro de ticket : {ticket_number}")
            else:
                print("Erreur, veuillez réessayer")
        elif choice == "2":
            floor = int(input("Entrez l'étage (1-4) : "))
            exception_type = input("Type d'exception (gratuite/autre): ").lower()
            parking_system.handle_exception(floor, exception_type)
            print(f"Exception gérée avec succès à l'étage {floor}.")
        elif choice == "3":
            parking_system.show_stat_place()
        elif choice == "4":
            placeNumber = int(input("Entrez le numéro de la place : "))
            #parking_system.liberer_place(placeNumber)
            if (parking_system.liberer_place(placeNumber)) :
                print(f"La place numero {placeNumber} a été libérée avec succès.")
            else :
                print(f"Il semblerais qu'il y ai une erreur. Veuillez vérifier si vous avez bien entrez le bon numéro de tickets")
        elif choice == "5":
            profits = parking_system.calculate_daily_profits()
            print(f"\nLes bénéfices de la journée sont de : {profits} €.")
        
        elif choice == "99":
            sleep(2.5)
            break
        else:
            print("Option invalide. Veuillez réessayer.")
