'''
File_system.py
manipulates the file system
for the server
'''
import os
import io

GAMES_DIRECTORY = '../Games'
GAMES_ID = 0

def check_directory():
    games_directory_there = os.path.exists(GAMES_DIRECTORY)
    if games_directory_there == False:
        os.mkdir(GAMES_DIRECTORY)

def create_file():
    global GAMES_ID
    open(GAMES_DIRECTORY + "/" + str(GAMES_ID))
    GAMES_ID += 1

def delete_file():
    raise Exception('NotImplementedException')

def find_file():
    raise Exception('NotImplementedException')