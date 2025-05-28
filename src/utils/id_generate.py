import random
import string

def generate_ticket_id(length=8)->str:
    """This method generates the ticket id randomly"""
    characters = string.ascii_uppercase + string.digits  # A-Z, 0-9
    ticket_id = ''.join(random.choices(characters, k=length))
    return ticket_id

# print(generate_ticket_id())