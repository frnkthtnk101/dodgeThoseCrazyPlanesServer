from enum import Enum

class Message_ids(Enum):
    INTIALIZE_GAME = bytes(0)
    CANNOT_INITIALIZE_GAME = bytes(1)
    RECEIVE_SESSION_ID = bytes(2)
    END_GAME = bytes(3)
    QUIT_GAME = bytes(4)
    OK = bytes(5)
    SEND_SESSION_ID = bytes(6)
    BAD_SESSION_ID = bytes(7)
    GET_LEVEL = bytes(8)
    RECEIVE_LEVEL = bytes(9)
    BAD_LEVEL = bytes(10)
    ERROR = bytes(11)

