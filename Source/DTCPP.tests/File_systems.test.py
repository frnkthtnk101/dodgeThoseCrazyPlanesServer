import unittest
import os
import sys
import shutil
sys.path.append('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesServer/Source')
import Classes.Message_ids
import Classes.PDU
from File_system import *

class File_systems_should (unittest.TestCase):
    
    '''
    creates a file to find
    then try to asserts if
    it can find it or not
    '''
    def test_should_find_file(self):
        t = open(HOME + GAMES_DIRECTORY + '/findme','w')
        t.close()
        self.assertTrue(find_file('findme'))
    
    '''
    trys to find the file
    findme, but should
    fail
    '''
    def should_not_find_file(self):
        file_exist = os.path.exists(HOME + GAMES_DIRECTORY + '/findme')
        if file_exist:
            os.remove(HOME + GAMES_DIRECTORY + '/findme')
        self.assertFalse(find_file('findme'))
    
    '''
    creates a file called
    findme then deletes it
    '''
    def test_should_delete_file(self):
        t = open(HOME + GAMES_DIRECTORY + '/findme')
        t.close()
        self.assertTrue('findme')

    '''
    checks to see if delete file
    raises error as it should
    '''
    def test_should_error_on_delete_file(self):
        file_exist = os.path.exists(HOME + GAMES_DIRECTORY + '/findme')
        if file_exist:
            os.remove(HOME+GAMES_DIRECTORY + '/findme')
        self.assertRaises(FileNotFoundError,delete_file('findme'))
    
    '''
    just creates a file
    checks the pdu
    '''
    def test_should_create_file_true(self):
        created, tempid, data = create_file()
        tempid_is_not_zero = tempid != 0 
        data_is_not_none = data is not None
        if tempid_is_not_zero or data_is_not_none:
            self.fail('the tempid was not 0 or data was not None')
        else:
            self.assertTrue(created)
    
    '''
    trys to create a file
    but fails
    '''
    def test_should_createfile_false(self):
        game_directory_there = os.path.exists(HOME+GAMES_DIRECTORY)
        if game_directory_there:
            shutil.rmtree(HOME+GAMES_DIRECTORY)
        created, tempid, data = createfile()
        tempid_is_not_neg_one = tempid != -1
        data_is_none = data is None
        if tempid_is_not_neg_one or data_is_none:
            self.fail('the tempid was not -1 or the data was null')
        self.assertFalse(created)
    
    '''
    checks if the games directory
    exist. it should
    '''
    def test_should_check_directory_true(self):
        check_games_directory()
        game_directory_there = os.path.exists(HOME+GAMES_DIRECTORY)
        if game_directory_there:
            self.assertTrue(True)
        else:
            self.fail('the games directory is not there')
        
    
    '''
    checks if the games directory
    ex
    '''
    def test_should_check_directory_false(self):
        game_directory_there = os.path.exists(HOME + GAMES_DIRECTORY)
        if game_directory_there:
            shutil.rmtree(HOME + GAMES_DIRECTORY)
        check_games_directory()
        game_directory_there = os.path.exists(HOME + GAMES_DIRECTORY)
        if game_directory_there:
            self.assertTrue(True)
        else:
            self.fail('the games directory is not there')

if __name__ == "__main__":
    unittest.main()