'''
DTCPP_functionality.py
all the functions in one convient package
'''

import json
from File_system import create_file, delete_file
from Classes.PDU import PDU
from Classes.Message_ids import Message_ids
from File_system import *

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
can send a Receive session id and
Cannot initialize game
'''
def initialize_game(request):
    created, session_id, data = create_file()
    if created:
        message = Message_ids.RECEIVE_SESSION_ID
    else:
        message = Message_ids.CANNOT_INITIALIZE_GAME
    response = PDU(message,session_id,request['version'],data)
    return json.loads(response)

''' 
selects a level on file
returns a respone
'''
def select_level(request):
    valid_session_id = find_file(request["session_id"])
    if valid_session_id:
        data = generate_game()
        message = Message_ids.RECEIVE_LEVEL
    else:
        data = {'Reason': 'bad session id.'}
        message = Message_ids.ERROR
    return PDU(message, response["session_id"],
        response['version'],data)


'''
ends the current game
'''
def end_game(response):
    valid_session_id = find_file(response["session_id"])
    if valid_session_id:
        delete_file(response["session_id"])
        message = Message_ids.OK
        data = None
    else:
        data = {'Reason': 'bad session id.'}
        message = Message_ids.ERROR
    return PDU(message,response["session_id"],
    response['version'], data)
