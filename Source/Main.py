'''
Main.py
this is the main loop for
the dodgeThosCrazyPlanesServer
'''

import socket
import json
import logging
from DTCPP_functionality import *
from File_system import check_directory
from Classes.Message_ids import Message_ids
from Classes.PDU import PDU

#set up the logger
logging.basicConfig(
    filename='../Simple.log', filemode='w',
    format = '%(name)s - %(levelname)s - %(message)s',
    level = logging.DEBUG
)
logging.info('log created')
#set up file system
logging.info('checking directory')
check_directory()
#set up the server
server_running = True
try:
    HOST, PORT = '', 80
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #listen
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)
except Exception as error:
    server_running = False
    print(f'{error}')
    logging.error(error)
if server_running:
    print('Dodge those crazy planes server Initialized')
    logging.info('Dodge those crazy planes server Initialized')
    #figure out what to do
    while True:
        client_connection, client_address = listen_socket.accept()
        logging.info(f'and connection from {client_address} received.')
        request = json.load(client_connection.recv(1024))
        request_ok = validate_request(request)
        #at any of them it will session Id
        #at any of them it will return error
        logging.info(f'figuring out what to do with {request['message']}')
        if request_ok:
            #initialize game 
            if bytes(request['message']) == Message_ids.INTIALIZE_GAME:
                #will send a cannot initialize game or
                #Receive session ID/ Send Session ID
                logging.info('intialize game')
                response = initialize_game(request)
            #get level
            elif bytes(request['message']) == Message_ids.GET_LEVEL:
                #send a Receive level
                logging.info('getting a level')
                response = select_level(request)
            #bad level
            elif bytes(request['message']) == Message_ids.BAD_LEVEL:
                logging.warning(f'{client_address} received a bad level')
                document_bad_level(request)
                response = select_level(request)
            #quit game
            elif bytes(request['message']) == Message_ids.END_GAME:
                #will send an OK
                logging.info(f'{client_address} wants to end the game {request['SessionId']}')
                response = end_game(request)
            #end game
            elif bytes(request['message']) == Message_ids.QUIT_GAME:
                #will send an OK
                logging.info(f'{client_address} wants to end the game {request['SessionId']}')
                response = end_game(request)
        logging.info(f'sending a response to {client_address}')
        client_connection.sendall(response)
        client_connection.close() 