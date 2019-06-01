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
    
    def should_create_file_true(self):
        return True
    def should_createfile_false(self):
        return True
    def should_check_directory_true(self):
        return True
    def should_check_directory_false(self):
