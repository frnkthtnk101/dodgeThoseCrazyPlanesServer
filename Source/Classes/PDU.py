'''
PDU.py
class that every response will
give back
'''
'''
the class for the PDU
every response will be created with this
to preven FUZZING
'''
class PDU:
    def __init__(self, message, session_id, version, data):
        self.Message = message.value
        self.SessionId = session_id
        self.Version = version
        self.Data = data