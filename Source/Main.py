'''
Main.py
this is the main loop for
the dodgeThosCrazyPlanesServer
'''

import socket
import json
from DTCPP_functionality import *

#set up file system
#set up the server
HOST, PORT = '', 80
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#listen
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Dodge those crazy planes server Initialized')

#figure out what to do
while True:
    client_connection, client_address = listen_socket.accept()
    request = json.load(client_connection.recv(1024))
    request_ok = validate_request(request)
    #at any of them it will session Id
    #at any of them it will return error
    if request_ok:
        #initialize game 
        if int(request['message']) == 0:
            #will send a cannot initialize game or
            #Receive session ID/ Send Session ID
            response = initialize_game(request)
        #get level
        elif int(request['message']) == 9:
            #send a Receive level
            response = select_level(request)
        #bad level
        elif int(request['message']) == 10:
            document_bad_level(request)
            response = select_level(request)
        #quit game
        elif int(request['message']) == 8:
            #will send an OK
            response = end_game(request)
        #end game
        elif int(request['message']) == 3:
            #will send an OK
            response = end_game(request)
    client_connection.sendall(response)
    client_connection.close() 

    print(request)
    
#close