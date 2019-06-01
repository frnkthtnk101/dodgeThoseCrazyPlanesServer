'''
File_system.py
manipulates the file system
for the server
'''
import os
import io
import json

GAMES_DIRECTORY = '../Games'
LEVELS_DIRECTORY = '../levels'
GAMES_ID = 0

'''
returns a list of levels
'''
def gather_levels():
        temp_list = []
        with open('../levels/easy1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('../levels/easy2.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('../levels/easy3.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('../levels/hard1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('../levels/medium1.json', 'r') as f1:
                temp_list.append(json.load(f1))
        with open('../levels/medium2.json', 'r') as f1:
                temp_list.append(json.load(f1))
        return temp_list

'''
Check if the directory exists
If it does not, then the fuction
will create a new one
'''
def check_level_directory():
    games_directory_there = os.path.exists(GAMES_DIRECTORY)
    if games_directory_there == False:
        os.mkdir(GAMES_DIRECTORY)

'''
check if the level directory exist
if does not, it will return false
otherwise true
'''
def check_directory():
        return os.path.exists(LEVELS_DIRECTORY)

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
                t = open(GAMES_DIRECTORY + "/" + str(GAMES_ID))
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