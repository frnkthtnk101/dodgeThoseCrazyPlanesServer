'''
DTCPP_functionality.py
all the functions in one convient package
'''

import json
import random
from File_system import create_file, delete_file, find_file
from Classes.PDU import PDU
from Classes.Message_ids import Message_ids


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
    return response

''' 
selects a level on file
returns a respone
'''
def select_level(request, levels):
    valid_session_id = find_file(request["session_id"])
    if valid_session_id:
        worked, data = generate_game(request['data'], levels)
        if worked:
            message = Message_ids.RECEIVE_LEVEL
        else:
            message = Message_ids.ERROR
    else:
        data = {'Reason': 'bad session id.'}
        message = Message_ids.ERROR
    return PDU(message, request["session_id"],request['version'],data)

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

'''
will select a game based on the data
given, else it will return error
'''
def generate_game(request_parameters, levels):
    correct_difficulty =request_parameters['difficutly'] in ['easy', 'medium', 'hard']
    if correct_difficulty:
        while True:
            index = random.randrange(0,len(levels)-1)
            same_level = request_parameters['Difficulty'] == levels[index]['Difficulty']
            request_parameters['PlaneTypes'].sort()
            levels[index]['PlaneTypes'].sort()
            same_dudes = levels[index]['PlaneTypes'] == levels[index]['PlaneTypes']
            if same_level and same_dudes:
                return True, levels[index]
    return False, {"reason" : "invalid difficulty"}