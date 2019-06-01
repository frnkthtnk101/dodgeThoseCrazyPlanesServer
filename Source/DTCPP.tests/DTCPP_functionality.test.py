'''
tests the file DTCPP_functioanlity
'''
import unittest
import os
import shutil
sys.path.append('/Users/francopettigrosso/ws/dodgeThoseCrazyPlanesServer/Source')
from DTCPP_functionality import *
from Classes.PDU import PDU 
from Classes.Message_ids import Message_ids
from File_system import *


class DTCPP_functioanlity_should(unittest.TestCase):
    def setUp(self):
        self.validate_good = {'Message' : Message_ids.INTIALIZE_GAME, 'SessionId': 1, 'Version' : bytes(56),'Data' : None}
        self.validate_bad = {'bad' : 'This is will produce a false'}
        self.initialize_game = {'Message' : Message_ids.INTIALIZE_GAME, 'SessionId': 1, 'Version' : bytes(56), 'Data' : None}
    
    def test_validate_request_should_return_true(self):
        validate_good_is_good = validate_request(self.validate_good)
        self.assertTrue(validate_good_is_good)
    
    def test_validate_request_should_return_false(self):
        validate_request_is_false = validate_request(self.validate_bad)
        self.assertFalse(validate_request_is_false)
    
    def test_initialize_game_should_return_RECEIVE_SESSION_ID(self):
        initialize_game_response = initialize_game(self.initialize_game)
        is_the_response_RECEIVED = initialize_game_response.message == Message_ids.RECEIVE_SESSION_ID
        self.assertTrue(is_the_response_RECEIVED)

    def test_initialize_game_should_return_CANNOT_INITIZE_GAME(self):
        game_directory_there = os.path.exists(HOME + GAMES_DIRECTORY)
        if game_directory_there:
            shutil.rmtree(HOME + GAMES_DIRECTORY)
        initialize_game_response = initialize_game(self.initialize_game)
        check_games_directory()
        game_could_not_be_initialized = initialize_game_response.message == Message_ids.CANNOT_INITIALIZE_GAME
        self.assertTrue(game_could_not_be_initialized)
    
    def test_select_level_should_return_RECEIVE_LEVEL(self):
        levels = gather_levels()
        request_initialization = initialize_game(self.validate_good)
        request_level = {'Message' : Message_ids.GET_LEVEL,
        'SessionID' : request_initialization.session_id,
        'Version' : request_initialization.version, 
        'Data' : 
            {
                'Difficulty' : 'easy',
                'PlaneTypes' : ['downers']
            }
        }
        response = select_level(request_level, levels)
        same_level = request_level['Data']['Difficulty'] == response.data['Difficulty']
        same_planes = request_level['Data']['PlaneTypes'] == response.data['PlaneTypes']
        self.assertTrue(same_level)
        self.assertTrue(same_planes)

    
    def test_select_level_should_return_ERROR(self):
        levels = gather_levels()
        request_level = {'Message' : Message_ids.GET_LEVEL,
        'SessionID' : 55,
        'Version' : bytes(56), 
        'Data' : 
            {
                'Difficulty' : 'easy',
                'PlaneTypes' : ['downers']
            }
        }
        response = select_level(request_level, levels)
        gave_error = response.message == Message_ids.ERROR
        self.assertTrue(gave_error)
    
    def test_select_level_should_return_ERROR_2(self):
        raise Exception('not built yet')
    
    def test_end_game_should_return_OK(self):
        raise Exception('not built yet')
    
    def test_end_should_return_ERROR(self):
        raise Exception('not built yet')

if __name__ == "__main__":
    unittest.main()