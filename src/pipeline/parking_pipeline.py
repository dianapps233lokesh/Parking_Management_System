from src.components.ticket import Ticket
from src.utils.id_generate import generate_ticket_id
from src import constant
from src.components.parking import Parking
from src.components.vehicle import Vehicle
from typing import Optional,List,Tuple
import time
from math import ceil

class ParkService:
    """This is more like a pipeline which will use components created inside directory and makes them functional. This class is responsible for 
       alloting parking to vehicle, checkout the vehicle from parking, checking space available, accessing data about parked vehicles, fee calculation for 
       parking based upon hours parked in the parking"""
    def __init__(self,parking:Parking):
        # pass
        self.parking=parking

    def allot_parking(self,vehicle:Vehicle,vehicle_type:str)->Optional[str]:
        """This method accesses park method from parking class and parks car in parking based uppon some specified conditions"""
        ticket_id=generate_ticket_id()
        entry_time=time.time()
        ticket=Ticket(ticket_id,entry_time,vehicle)
        # parking=Parking()
        if self.parking.park(vehicle_type,ticket_id,ticket):
            return ticket_id
        return None
    
    # def get_remaining_space(self,vehicle_type):
    #     return self.parking.available_space(vehicle_type)   # problem in printing type of vehicle letter
    

    def get_remaining_space(self)->dict:
        """This method returns the space available in parking for both two wheelers and four wheelers in parking."""
        return {
                'Two wheeler':self.parking.available_space('two_wheeler'),
                'Four wheeler':self.parking.available_space('four_wheeler')
        }


    def checkout(self,vehicle_type:str,ticket_id:str)->Optional[float]:
        """This method is reponsible for deboarding the car from parking and returning the fee based upon total hours parked in parking."""
        ticket=self.parking.parked.get(ticket_id)
        # print(ticket)
        if not ticket:
            return None
        exit_time=time.time()
        fee=self.calculate_fee(ticket.entry_time,exit_time,vehicle_type)
        ticket.checkout(exit_time,fee)
        self.parking.remove_vehicle(ticket_id,vehicle_type,fee)

        return fee
    
    def calculate_fee(self,entry_time:float,exit_time:float,vehicle_type:str)->float:
        """This method calculates the total fee based upon the total hours car parked in parking"""
        total_hrs=ceil((exit_time-entry_time)/3600)
        if vehicle_type=='two_wheeler':
            rate=constant.TWO_WHEELER_FEE
        else:
            rate=constant.FOUR_WHEELER_FEE
        if total_hrs<1:
            return rate
        return rate*total_hrs
    
    def parked_vehicles(self)->List[Tuple[str,str]]:
        """This method returns the details about parked vehicles"""
        return [(val.vehicle.vehicle_owner,val.vehicle.vehicle_num) for val in self.parking.parked.values()]
    

    # def parked_vehicles_dict(self):
    #     return self.parking.parked
    
    def total_revenue(self)->float:
        """This method returns the total revenue of parking mall"""
        return self.parking.revenue