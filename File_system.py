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

def delete_file(index_number):
    file_exists = os.path.exists(GAMES_DIRECTORY + "/" + index_number)
    if file_exists:
        os.remove(GAMES_DIRECTORY + "/" + index_number,)
        return True
    raise FileNotFoundError(f'{index_number} does not exists')
    

def find_file(index_number):
    return os.path.exists(GAMES_DIRECTORY + "/" + index_number)