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
    response = PDU(message,session_id,request['Version'],data)
    return response

''' 
selects a level on file
returns a respone
'''
def select_level(request, levels):
    valid_session_id = find_file(request['SessionId'])
    if valid_session_id:
        worked, data = generate_game(request['Data'], levels)
        if worked:
            message = Message_ids.RECEIVE_LEVEL
        else:
            message = Message_ids.ERROR
    else:
        data = {'Reason': 'bad session id.'}
        message = Message_ids.ERROR
    return PDU(message, request['SessionId'],request['Version'],data)

'''
ends the current game
'''
def end_game(request):
    valid_session_id = find_file(request['SessionId'])
    if valid_session_id:
        delete_file(request['SessionId'])
        message = Message_ids.OK
        data = None
    else:
        data = {'Reason': 'bad session id.'}
        message = Message_ids.ERROR
    tempPDU = PDU(message, request['SessionId'], request['Version'], data)
    return tempPDU

'''
will select a game based on the data
given, else it will return error
'''
def generate_game(request_parameters, levels):
    correct_difficulty =request_parameters['Difficulty'] in ['easy', 'medium', 'hard']
    if correct_difficulty:
        while True:
            index = random.randrange(0,len(levels)-1)
            same_level = request_parameters['Difficulty'] == levels[index]['Difficulty']
            request_parameters['PlaneTypes'].sort()
            #levels[index]['PlaneTypes']
            same_dudes = levels[index]['PlaneTypes'] == levels[index]['PlaneTypes']
            if same_level and same_dudes:
                return True, levels[index]
    return False, {"reason" : "invalid difficulty"}