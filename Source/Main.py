'''
Main.py
this is the main loop for
the dodgeThosCrazyPlanesServer
'''

import socket
import json
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
    if request_ok:
        if int(request['message']) == 0:
            respone = initialize_game(request)
    client_connection.sendall(respone)
    client_connection.close() 

    print(request)
    
 #close