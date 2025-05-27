from src.components.parking import Parking
from src.pipeline.park_app import park_app
from src.components.vehicle import two_wheeler,four_wheeler
import time

def main():
    parking=Parking()
    park_service=park_app(parking)
    
    veh1=two_wheeler('RJ14BW5273',"Lokesh")
    veh2=four_wheeler('RJ14BW5279',"Rahul")
    veh3=four_wheeler('RJ14BS5279',"Rahuls")

    ticket_id1=park_service.allot_parking(veh1,'two_wheeler')
    ticket_id2=park_service.allot_parking(veh2,'four_wheeler')
    ticket_id3=park_service.allot_parking(veh3,'four_wheeler')
    print("Available space: ",park_service.get_remaining_space())
    time.sleep(2)

    fee1=park_service.checkout('two_wheeler',ticket_id1)
    fee1=park_service.checkout('four_wheeler',ticket_id3)

    
    print("Available space: ",park_service.get_remaining_space())

    print("fee1: ",fee1)

    print(park_service.parked_vehicles())

    print('total revenue: ',park_service.total_revenue())

main()