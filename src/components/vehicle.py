class vehicle:
    def __init__(self,vehicle_num,owner):
        self.vehicle_num=vehicle_num
        self.vehicle_owner=owner


class two_wheeler(vehicle):
    def __init__(self,vehicle_num,owner):
        super().__init__(vehicle_num,owner)

class four_wheeler(vehicle):
    def __init__(self,vehicle_num,owner):
        super().__init__(vehicle_num,owner)