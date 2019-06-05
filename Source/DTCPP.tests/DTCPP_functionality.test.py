'''
tests the file DTCPP_functioanlity
'''
import unittest
import os
import shutil
import sys
#this needs to be hardcoded because the test needs to know where the other files are at
sys.path.append('C:\\Users\\Franco\dodgeThoseCrazyPlanesServer\Source')
from DTCPP_functionality import *
from Classes.PDU import PDU 
from Classes.Message_ids import Message_ids
from File_system import *


class DTCPP_functioanlity_should(unittest.TestCase):
    def setUp(self):
        self.validate_good = {'Message' : Message_ids.INTIALIZE_GAME.value, 'SessionId': 1, 'Version' : (56).to_bytes(1, byteorder='big'),'Data' : None}
        self.validate_bad = {'bad' : 'This is will produce a false'}
        self.initialize_game = {'Message' : Message_ids.INTIALIZE_GAME.value, 'SessionId': 1, 'Version' : (56).to_bytes(1, byteorder='big'), 'Data' : None}
        self.request_level = {'Message' : Message_ids.GET_LEVEL.value,
        'SessionId' : '-1',
        'Version' : bytes(89), 
        'Data' : 
            {
                'Difficulty' : 'easy',
                'PlaneTypes' : ['downers']
            }
        }
        self.end_game = {'Message' : Message_ids.END_GAME.value, 'SessionId' : -1, 'Version' : (56).to_bytes(1, byteorder='big'), 'Data' : None}
    
    def test_validate_request_should_return_true(self):
        validate_good_is_good = validate_request(self.validate_good)
        self.assertTrue(validate_good_is_good)
    
    def test_validate_request_should_return_false(self):
        validate_request_is_false = validate_request(self.validate_bad)
        self.assertFalse(validate_request_is_false)
    
    def test_initialize_game_should_return_RECEIVE_SESSION_ID(self):
        initialize_game_response = initialize_game(self.initialize_game)
        is_the_response_RECEIVED = initialize_game_response.Message == Message_ids.RECEIVE_SESSION_ID.value
        self.assertTrue(is_the_response_RECEIVED)

    def test_initialize_game_should_return_CANNOT_INITIZE_GAME(self):
        game_directory_there = os.path.exists(HOME + GAMES_DIRECTORY)
        if game_directory_there:
            shutil.rmtree(HOME + GAMES_DIRECTORY)
        initialize_game_response = initialize_game(self.initialize_game)
        check_games_directory()
        game_could_not_be_initialized = initialize_game_response.Message == Message_ids.CANNOT_INITIALIZE_GAME.value
        self.assertTrue(game_could_not_be_initialized)
    
    def test_select_level_should_return_RECEIVE_LEVEL(self):
        levels = gather_levels()
        request_initialization = initialize_game(self.validate_good)
        self.request_level['SessionId'] = request_initialization.SessionId
        self.request_level['Version'] = request_initialization.Version, 
        response = select_level(self.request_level, levels)
        same_level = self.request_level['Data']['Difficulty'] == response.Data['Difficulty']
        same_planes = self.request_level['Data']['PlaneTypes'] == response.Data['PlaneTypes']
        self.assertTrue(same_level)
        self.assertTrue(same_planes)

    
    def test_select_level_should_return_ERROR(self):
        levels = gather_levels()
        request_level = {'Message' : Message_ids.GET_LEVEL.value,
        'SessionId' : 55,
        'Version' : (56).to_bytes(1, byteorder='big'), 
        'Data' : 
            {
                'Difficulty' : 'easy',
                'PlaneTypes' : ['downers']
            }
        }
        response = select_level(request_level, levels)
        gave_error = response.Message == Message_ids.ERROR.value
        self.assertTrue(gave_error)
    
    def test_select_level_should_return_ERROR_2(self):
        levels = gather_levels()
        request_initialization = initialize_game(self.validate_good)
        self.request_level['SessionId'] = request_initialization.SessionId
        self.request_level['Version'] = request_initialization.Version
        self.request_level['Data']['Difficulty'] = 'beta'
        response = select_level(self.request_level, levels)
        gave_error = response.Message == Message_ids.ERROR.value
        self.assertTrue(gave_error)
    
    def test_end_game_should_return_OK(self):
        request_initialization = initialize_game(self.validate_good)
        self.end_game['SessionId'] = request_initialization.SessionId
        response = end_game(self.end_game)
        did_it_end_game = response.Message == Message_ids.OK.value
        self.assertTrue(did_it_end_game)
    
    def test_end_should_return_ERROR(self):
        self.end_game['SessionId'] = -1
        response = end_game(self.end_game)
        did_it_error_out = response.Message == Message_ids.ERROR.value
        self.assertTrue(did_it_error_out)

if __name__ == "__main__":
    unittest.main()