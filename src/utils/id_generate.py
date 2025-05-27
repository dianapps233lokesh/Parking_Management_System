import random
import string

def generate_ticket_id(length=8):
    characters = string.ascii_uppercase + string.digits  # A-Z, 0-9
    ticket_id = ''.join(random.choices(characters, k=length))
    return ticket_id

# print(generate_ticket_id())