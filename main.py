from src.components.parking import Parking
from src.pipeline.parking_pipeline import ParkService
from src.components.vehicle import TwoWheeler,FourWheeler
# import time

def get_vehicle_type() -> str:
    print("\n\nSelect vehicle type:")
    print("1. Two Wheeler")
    print("2. Four Wheeler")
    choice = input("Enter choice (1 or 2): ").strip()
    if choice == "1":
        return "two_wheeler"
    elif choice == "2":
        return "four_wheeler"
    else:
        return None


def main():
    parking=Parking()
    park_service=ParkService(parking)

    print("...Welcome to the Parking System...")

    while True:
        print("\nOptions:")
        print("1. Allot Parking")
        print("2. Checkout")
        print("3. View Parked Vehicles")
        print("4. View Available Space")
        print("5. View Total Revenue")
        print("6. Exit")


        choice=input("Enter your choice: ").strip()

        if choice=='1':
            vtype=get_vehicle_type()
            if not vtype:
                print("Invalid choice.")
                continue
            vnum=input('Enter vehicle number: ').strip()
            owner=input('Enter vehicle owner name: ').strip()

            if vtype=='two_wheeler':
                vehicle=TwoWheeler(vnum,owner)
            elif vtype=='four_wheeler':
                vehicle=FourWheeler(vnum,owner)
            else:
                print("Invalid vehicle type..")
                continue


            ticket_id=park_service.allot_parking(vehicle,vtype)
            if ticket_id:
                print(f"Parking alloted. Ticket_id: {ticket_id}")
            else:
                print("Parking full or failed")
        
        elif choice=='2':
            vtype=get_vehicle_type()
            if not vtype:
                print("Invalid choice.")
                continue
            ticket_id=input('Enter ticket id: ').strip()
            fee=park_service.checkout(vtype,ticket_id)
            print(f"Parking fee: {fee}")
        
        elif choice=='3':
            print("Parked Vehicles:")
            for owner, vnum in park_service.parked_vehicles():
                print(f"  - {owner} ({vnum})")

        elif choice=='4':
            print("Available space:",park_service.get_remaining_space())
        
        elif choice == "5":
            print("Total revenue collected:", park_service.total_revenue())

        elif choice == "6":
            print("Exiting the parking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()