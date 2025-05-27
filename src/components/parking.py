from src import constant
class Parking:
    def __init__(self):
        self.total_2W=constant.TWO_WHEELER_SPACE
        self.total_4W=constant.FOUR_WHEELER_SPACE
        self.parked={}
        self.revenue=0


    def available_space(self,vehicle_type):
        if vehicle_type=='two_wheeler':
            return self.total_2W
        return self.total_4W
    
    def park(self,vehicle_type,ticket_id,ticket):
        if vehicle_type=='two_wheeler' and self.available_space(vehicle_type)>0:
            self.total_2W-=1
            self.parked[ticket_id]=ticket
            return True
            
        elif vehicle_type=='four_wheeler' and self.available_space(vehicle_type)>0:
            self.total_4W-=1
            self.parked[ticket_id]=ticket
            return True
        
        return False

    def remove_vehicle(self,ticket_id,vehicle_type,fee):
        ticket=self.parked.pop(ticket_id,None)
        # print(ticket)
        if ticket:
            self.revenue+=fee
            if vehicle_type=='two_wheeler':
                self.total_2W+=1
            else:
                self.total_4W+=1
                
