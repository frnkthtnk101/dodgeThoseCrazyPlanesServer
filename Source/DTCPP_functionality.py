'''
DTCPP_functionality.py
all the functions in one convient package
'''

import json
from File_system import create_file, delete_file

pdu = ['Message','SessionId','Version','Data']

'''
validates that the Json meets the PDU
Standard.
return a bool statement
'''
def validate_request(response):
    keys = response.keys()
    request_ok = True
    for index in pdu:
        if index in keys:
            continue
        request_ok = False
        break
    return request_ok

'''
initializes the game
returns a response
'''
def initialize_game(response):
    

'''
selects a level on file
returns a respone
'''
def select_level(response):
    raise Exception("Not Implemented")

'''
ends the current game
'''
def end_game(response):
    raise Exception("Not Implemented")
