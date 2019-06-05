'''
Message_ids.py
used to keep track of
what message is being sent
'''
from enum import Enum

'''
to prevent anything shady
or any accidents made an enum
helps prevent fuzzing.
'''
class Message_ids(Enum):
    INTIALIZE_GAME = 0
    CANNOT_INITIALIZE_GAME = 1
    RECEIVE_SESSION_ID = 2
    END_GAME = 3
    QUIT_GAME = 4
    OK = 5
    SEND_SESSION_ID = 6
    BAD_SESSION_ID = 7
    GET_LEVEL = 8
    RECEIVE_LEVEL = 9
    BAD_LEVEL = 10
    ERROR = 11

