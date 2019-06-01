import unittest
import Classes.Message_ids
import Classes.PDU

class File_systems_should (unittest.TestCase):
    def should_find_file(self):
        return True
    def should_not_find_file(self):
        return False
    def should_delete_file(self):
        return True
    def should_error_on_delete_file(self):
        return True
    def should_create_file_true(self):
        return True
    def should_createfile_false(self):
        return True
    def should_check_directory_true(self):
        return True
    def should_check_directory_false(self):
