'''
File_system.py
manipulates the file system
for the server
'''
import os
import sys
import io
import json
from pathlib import Path


HOME = str(Path.home())
GAMES_DIRECTORY = '/Games'
LEVELS_DIRECTORY = '/levels'
GAMES_ID = 0
sys.path.append(HOME+GAMES_DIRECTORY)
sys.path.append(HOME+LEVELS_DIRECTORY)
'''
returns a list of levels
'''
def gather_levels():
        temp_list = []
        with open('easy1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('easy2.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('easy3.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('hard1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('medium1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('medium2.json', 'r') as f1:
                temp_list.append(json.load(f1))
        return temp_list

'''
Check if the directory exists
If it does not, then the fuction
will create a new one
'''
def check_games_directory():
    games_directory_there = os.path.exists(HOME+GAMES_DIRECTORY)
    if games_directory_there == False:
        os.mkdir(HOME+GAMES_DIRECTORY)

'''
check if the level directory exist
if does not, it will return false
otherwise true
'''
def check_levels_directory():
        return os.path.exists(HOME+LEVELS_DIRECTORY)

'''
creates a file with the Games ID
then Incrementes
'''
def create_file():
        created = True
        data = None
        try:
                global GAMES_ID
                tempid = GAMES_ID
                t = open(HOME + GAMES_DIRECTORY + "/" + str(GAMES_ID),'w')
                t.close()
                GAMES_ID += 1
        except Exception as err:
                tempid = -1
                created = False
                data = {'Reason' : err}
        return created, tempid, data

'''
deletes a file if the given
file exists, else throws error
'''
def delete_file(index_number):
    file_exists = os.path.exists(HOME + GAMES_DIRECTORY + "/" + index_number)
    if file_exists:
        os.remove(HOME + GAMES_DIRECTORY + "/" + index_number,)
        return True
    raise FileNotFoundError(f'{index_number} does not exists')
    
'''
use to tell if the current file exists
'''
def find_file(index_number):
    return os.path.exists(HOME + GAMES_DIRECTORY + "/" + index_number)