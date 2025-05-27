class Ticket:
    def __init__(self,ticket_id,entry_time,vehicle):
        self.ticket_id=ticket_id
        self.entry_time=entry_time
        self.exit_time=None
        self.fee=0
        self.vehicle=vehicle

    
    def checkout(self,exit_time,fee):
        self.exit_time=exit_time
        self.fee=fee