import unittest
import os
import Classes.Message_ids
import Classes.PDU
import File_system

class File_systems_should (unittest.TestCase):
    
    '''
    creates a file to find
    then try to asserts if
    it can find it or not
    '''
    def should_find_file(self):
        t = open('../Games/findme')
        t.close()
        self.assertTrue(File_system.find_file('findme'))
    
    '''
    trys to find the file
    findme, but should
    fail
    '''
    def should_not_find_file(self):
        file_exist = os.path.exists('../Games/findme')
        if file_exist:
            os.remove('../Games/findme')
        self.assertFalse(File_system.find_file('findme'))
    
    '''
    creates a file called
    findme then deletes it
    '''
    def should_delete_file(self):
        t = open('../Games/findme')
        t.close()
        self.assertTrue('findme')

    '''
    checks to see if delete file
    raises error as it should
    '''
    def should_error_on_delete_file(self):
        file_exist = os.path.exists('../Games/findme')
        if file_exist:
            os.remove('../Games/findme')
        self.assertRaises(FileNotFoundError,File_system.delete_file('findme'))
    
    '''
    just creates a file
    checks the pdu
    '''
    def should_create_file_true(self):
        created, tempid, data = create_file()
        tempid_is_not_zero = tempid != 0 
        data_is_not_none = data is not None
        if tempid_is_not_zero or data_is_not_none:
            self.fail('the tempid was not 0 or data was not None')
        self.assertTrue(created)
    
    '''
    trys to create a file
    but fails
    '''
    def should_createfile_false(self):
        os.rename('../Games','../Games1')
        created, tempid, data = createfile()
        os.rename('../Games1','../Games')
        tempid_is_not_neg_one = tempid != -1
        data_is_none = data is None
        if tempid_is_not_neg_one or data_is_none:
            self.fail('the tempid was not -1 or the data was null')
        self.assertFalse(created)
    
    '''
    checks if the games directory
    exist. it should
    ''''
    def should_check_directory_true(self):
        File_system.check_directory()
        game_directory_there = os.path.exists('../Games')
        if game_directory_there:
            self.assertTrue(True)
        self.fail('the games directory is not there')
        
    
    '''
    checks if the games directory
    ex
    '''
    def should_check_directory_false(self):
        game_directory_there = os.path.exists('../Games')
        if game_directory_there:
            os.remove('../Games')
        File_system.check_directory()
        game_directory_there = os.path.exists('../Games')
        if game_directory_there:
            self.assertTrue(True)
        self.fail('the games directory is not there')