'''
tests the file DTCPP_functioanlity
'''
import unittest
sys.path.append('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesServer/Source')
from DTCPP_functionality import *
from Classes.PDU import PDU 
from Classes.Message_ids import Message_ids


class DTCPP_functioanlity_should(unittest.TestCase):
    def setUp(self):
        self.validate_good = PDU(Message_ids.INTIALIZE_GAME,1,bytes(56),None)

    def test_validate_request_should_return_true(self):
        validate_good_is_good = validate_request(self.validate_good)
        self.assertTrue(validate_good_is_good)
    
    def test_validate_request_should_return_false(self):
        raise Exception('not built yet')
    
    def test_initialize_game_should_return_RECEIVE_SESSION_ID(self):
        raise Exception('not built yet')
    
    def test_initialize_game_should_return_CANNOT_INITIZE_GAME(self):
        raise Exception('not built yet')
    
    def test_select_level_should_return_RECEIVE_LEVEL(self):
        raise Exception('not built yet')
    
    def test_select_level_should_return_ERROR(self):
        raise Exception('not built yet')
    
    def test_select_level_should_return_ERROR_2(self):
        raise Exception('not built yet')
    
    def test_end_game_should_return_OK(self):
        raise Exception('not built yet')
    
    def test_end_should_return_ERROR(self):
        raise Exception('not built yet')

if __name__ == "__main__":
    unittest.main()