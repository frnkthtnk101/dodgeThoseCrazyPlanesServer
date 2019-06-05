'''
Main.py
this is the main loop for
the dodgeThosCrazyPlanesServer
'''

import socket
import json
import logging
from DTCPP_functionality import *
from File_system import *
from Classes.Message_ids import Message_ids
from Classes.PDU import PDU

#set up the logger
logging.basicConfig(
    filename='Simple.log', filemode='w',
    format = '%(name)s - %(levelname)s - %(message)s',
    level = logging.DEBUG
)
logging.info('log created')
#set up file system
logging.info('checking directory')
check_games_directory()
if check_levels_directory():
    levels = gather_levels()
    #set up the server
    server_running = True
    try:
        HOST, PORT = '', 28960
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
            information = client_connection.recv(4096)
            information_decoded = information.decode()
            request = json.loads(information_decoded)
            request_ok = validate_request(request)
            #at any of them it will session Id
            #at any of them it will return error
            message = int(request['Message'])
            session_id = request['SessionId']
            logging.info(f'figuring out what to do with {message}')
            if request_ok:
                #initialize game 
                if message == Message_ids.INTIALIZE_GAME.value:
                    #will send a cannot initialize game or
                    #Receive session ID/ Send Session ID
                    logging.info('intialize game')
                    response = initialize_game(request)
                #get level
                elif message == Message_ids.GET_LEVEL.value:
                    #send a Receive level
                    logging.info('getting a level')
                    response = select_level(request, levels)
                #bad level
                elif message == Message_ids.BAD_LEVEL.value:
                    logging.warning(f'{client_address} received a bad level')
                    reason = request['Data']['Reason']
                    logging.info(f'reasons why the level was bad {reason}')
                    response = select_level(request,levels)
                #quit game
                elif message == Message_ids.END_GAME.value:
                    #will send an OK
                    logging.info(f'{client_address} wants to end the game {session_id}')
                    response = end_game(request)
                #end game
                elif message == Message_ids.QUIT_GAME.value:
                    #will send an OK
                    logging.info(f'{client_address} wants to end the game {session_id}')
                    response = end_game(request)
                else:
                    response = PDU(Message_ids.ERROR, request['SessionId'], request['Version'], {'Reason' : 'Invalid Request'} )
            logging.info(f'sending a response to {client_address}')
            response_json = json.dumps(response.__dict__)
            response_json_encode = str.encode(response_json)
            client_connection.sendall(response_json_encode)
            client_connection.close()
else:
    print('the games directory not here')