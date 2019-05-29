'''
Main.py
this is the main loop for
the dodgeThosCrazyPlanesServer
'''

import socket
 #set up the server
HOST, PORT = '', 80
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 #listen
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Dodge those crazy planes server Initialized')



 #figure out what to do

 #close