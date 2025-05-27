from src import constant
from src.components.ticket import Ticket



class Parking:
    """Parking class which contains the information about type of vehicles and total space left in parking and revenue."""
    def __init__(self):
        self.total_2W=constant.TWO_WHEELER_SPACE
        self.total_4W=constant.FOUR_WHEELER_SPACE
        self.parked={}
        self.revenue=0


    def available_space(self,vehicle_type:str)->int:
        """Returns available space in the parking"""
        if vehicle_type=='two_wheeler':
            return self.total_2W
        return self.total_4W
    
    def park(self,vehicle_type:str,ticket_id:str,ticket:Ticket)->bool:
        """parks a vehicle based upon type and space left in the parking"""
        if vehicle_type=='two_wheeler' and self.available_space(vehicle_type)>0:
            self.total_2W-=1
            self.parked[ticket_id]=ticket
            return True
            
        elif vehicle_type=='four_wheeler' and self.available_space(vehicle_type)>0:
            self.total_4W-=1
            self.parked[ticket_id]=ticket
            return True
        
        return False

    def remove_vehicle(self,ticket_id:str,vehicle_type:str,fee:float)->None:
        """Checkout the vehicle from the parking based upon its type and adds fees to revenue during checkout"""
        ticket=self.parked.pop(ticket_id,None)
        # print(ticket)
        if ticket:
            self.revenue+=fee
            if vehicle_type=='two_wheeler':
                self.total_2W+=1
            else:
                self.total_4W+=1
                
