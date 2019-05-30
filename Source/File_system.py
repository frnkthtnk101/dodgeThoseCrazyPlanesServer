'''
File_system.py
manipulates the file system
for the server
'''
import os
import io

GAMES_DIRECTORY = '../Games'
GAMES_ID = 0

'''
Check if the directory exists
If it does not, then the fuction
will create a new one
'''
def check_directory():
    games_directory_there = os.path.exists(GAMES_DIRECTORY)
    if games_directory_there == False:
        os.mkdir(GAMES_DIRECTORY)

'''
creates a file with the Games ID
then Incrementes
'''
def create_file():
    global GAMES_ID
    tempid = GAMES_ID
    open(GAMES_DIRECTORY + "/" + str(GAMES_ID))
    GAMES_ID += 1
    return tempid

'''
deletes a file if the given
file exists, else throws error
'''
def delete_file(index_number):
    file_exists = os.path.exists(GAMES_DIRECTORY + "/" + index_number)
    if file_exists:
        os.remove(GAMES_DIRECTORY + "/" + index_number,)
        return True
    raise FileNotFoundError(f'{index_number} does not exists')
    
'''
use to tell if the current file exists
'''
def find_file(index_number):
    return os.path.exists(GAMES_DIRECTORY + "/" + index_number)