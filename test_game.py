import unittest
from unittest.mock import patch
from game import Room, Game


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.x = 5
        self.y = 4
        self.name = "Room to test your unit"
        self.description = "You see units standing, ready for test."
        self.exits = ['north', 'south']
        self.room = Room(self.x, self.y, self.name,
                         self.description, self.exits)

    def test_str(self):
        expected = f'{self.name}\n{self.description}'
        result = self.room.__str__()
        self.assertEqual(expected, result)

    def test_check_exit_positive(self):
        result = self.room._check_exit('north')
        self.assertTrue(result)

    def test_check_exit_negative(self):
        directions = ['west', 'North', 'vostok']
        for direction in directions:
            with self.subTest(direction):
                result = self.room._check_exit(direction)
                self.assertFalse(result)


class TestGame(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(0, 0, "Main room", "", ["north"])
        self.room2 = Room(0, -1, "Second room", "", ["south", "east"])
        self.room3 = Room(1, -1, 'Third room', '', ['west', 'north'])
        self.map = {(self.room1.x, self.room1.y): self.room1,
                    (self.room2.x, self.room2.y): self.room2,
                    (self.room3.x, self.room3.y): self.room3
                    }
        self.game = Game(self.map)

    def test_get_room_positive(self):
        """
        In this test, in a variable coords, the key is the coordinates to move
        to another room. The value is the name of the room where the player
        should go after the transition, if the method worked correctly
        """
        coords = {(0, -1): 'Second room', (1, 0): 'Third room',
                  (-1, 0): 'Second room', (0, 1): 'Main room'}
        for coord, name in coords.items():
            with self.subTest(coord):
                x, y = coord
                result = self.game._get_room(x, y)
                self.game.player_x += x
                self.game.player_y += y
                self.assertIsInstance(result, Room)
                self.assertEqual(result.name, name)

    def test_get_room_negative(self):
        """
        In this test, the coordinates for exiting the main room
        (south, east, west) are passed. She has only one exit
        to the north. Therefore, the method should not return the room.
        """
        coords = [(0, 1), (1, 0), (-1, 0)]
        for coord in coords:
            with self.subTest(coord):
                result = self.game._get_room(*coord)
                self.assertIsNone(result)

    @patch('game.Room._check_exit', return_value=True)
    @patch('game.Game._move')
    def test_parse_positive(self, _move, _check_exit):
        in_data = {'Go north': (0, -1), 'go East': (1, 0),
                   'Go South': (0, 1), 'go west': (-1, 0)}
        for in_str, coord in in_data.items():
            with self.subTest(in_str):
                self.game._parse(in_str)
                _check_exit.assert_called()
                _move.assert_called()
                _move.assert_called_with(*coord)
                _move.reset_mock()
                _check_exit.reset_mock()

    @patch('game.Room._check_exit')
    def test_parse_negative(self, _check_exit):
        in_data = ['move north', 'go_north']
        for in_str in in_data:
            with self.subTest(in_str):
                self.game._parse(in_str)
                _check_exit.assert_not_called()

    @patch('game.Game._look_at')
    def test_move_positive(self, _look_at):
        coords_north = (0, -1)
        self.game._move(*coords_north)
        self.assertIs(self.game.current_room, self.room2)
        self.assertEqual(self.game.player_x, 0)
        self.assertEqual(self.game.player_y, -1)
        _look_at.assert_called()

    @patch('builtins.print')
    @patch('game.Game._get_room', return_value=None)
    def test_move_negative(self, _get_room, mock_print):
        coord = (1, 0)
        self.game._move(*coord)
        _get_room.assert_called()
        mock_print.assert_called_with('Error: missing room')


if __name__ == '__main__':
    unittest.main(buffer=True)
