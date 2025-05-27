from src.components.vehicle import Vehicle

class Ticket:
    """Contains the information which will be printed on ticket while parking the car."""
    def __init__(self,ticket_id:str,entry_time:float,vehicle:Vehicle):
        
        self.ticket_id=ticket_id
        self.entry_time=entry_time
        self.exit_time=None
        self.fee=0
        self.vehicle=vehicle

    
    def checkout(self,exit_time:float,fee:float)->None:
        """Contains the exit time and fee deposited during checkout"""
        self.exit_time=exit_time
        self.fee=fee