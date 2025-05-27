from src.components.ticket import Ticket
from src.utils.id_generate import generate_ticket_id
from src import constant
# from src.components.parking import Parking
import time

class park_app:
    def __init__(self,parking):
        # pass
        self.parking=parking

    def allot_parking(self,vehicle,vehicle_type):
        ticket_id=generate_ticket_id()
        entry_time=time.time()
        ticket=Ticket(ticket_id,entry_time,vehicle)
        # parking=Parking()
        if self.parking.park(vehicle_type,ticket_id,ticket):
            return ticket_id
        return None
    
    # def get_remaining_space(self,vehicle_type):
    #     return self.parking.available_space(vehicle_type)   # problem in printing type of vehicle letter
    

    def get_remaining_space(self):
        return {
                'Two wheeler':self.parking.available_space('two_wheeler'),
                'Four wheeler':self.parking.available_space('four_wheeler')

        }


    def checkout(self,vehicle_type,ticket_id):
        ticket=self.parking.parked.get(ticket_id)
        # print(ticket)
        if not ticket:
            return None
        exit_time=time.time()
        fee=self.calculate_fee(ticket.entry_time,exit_time,vehicle_type)
        ticket.checkout(exit_time,fee)
        self.parking.remove_vehicle(ticket_id,vehicle_type,fee)

        return fee
    
    def calculate_fee(self,entry_time,exit_time,vehicle_type):
        total_hrs=(exit_time-entry_time)/3600
        if vehicle_type=='two_wheeler':
            rate=constant.TWO_WHEELER_FEE
        else:
            rate=constant.FOUR_WHEELER_FEE
        if total_hrs<1:
            return rate
        return rate*total_hrs
    
    def parked_vehicles(self):
        return [(val.vehicle.vehicle_owner,val.vehicle.vehicle_num) for val in self.parking.parked.values()]
    

    def parked_vehicles_dict(self):
        return self.parking.parked
    
    def total_revenue(self):
        return self.parking.revenue