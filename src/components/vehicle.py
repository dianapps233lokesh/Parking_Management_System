class Vehicle:
    """This is the base class for the type of vehicle and stores the information about vehicle number and vehicle owner"""
    def __init__(self,vehicle_num:str,owner:str):
        self.vehicle_num=vehicle_num
        self.vehicle_owner=owner


class TwoWheeler(Vehicle):
    """This is the derived class from Vehicle class for two wheelers"""
    def __init__(self,vehicle_num,owner):
        super().__init__(vehicle_num,owner)

class FourWheeler(Vehicle):
    """This is the derived class for the four wheelers"""
    def __init__(self,vehicle_num,owner):
        super().__init__(vehicle_num,owner)