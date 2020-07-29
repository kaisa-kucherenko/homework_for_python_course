import unittest
from sea_battle import SeaBattleGame


class TestSeaBattleGame(unittest.TestCase):
    def setUp(self):
        self.ships_count = 1
        self.game = SeaBattleGame(self.ships_count)

    def test_generate_field(self):
        expected = [['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'],
                    ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']]
        self.assertListEqual(self.game._generate_field(), expected)

    def test_set_ships_positive(self):
        expected = self.ships_count
        result = 0
        field1 = self.game._set_ships()
        for y in field1:
            result += y.count('o')
        self.assertEqual(result, expected)
        field2 = self.game._set_ships()
        self.assertNotEqual(field1, field2, 'The ships are in the same places.'
                                            ' Must be at random every time')

    def test_set_ships_negative(self):
        expected = self.ships_count + 1
        result = 0
        field1 = self.game._set_ships()
        for y in field1:
            result += y.count('o')
        self.assertNotEqual(result, expected)

    def test_parse_shot_positive(self):
        shot = '1,9'
        self.game._parse_shot(shot)
        self.assertIsNotNone(self.game.shot)
        self.assertEqual(self.game.shot, (0, 8))

    def test_parse_shot_negative(self):
        shots = ['three and fife', '1.4', '0,9', '5,11']
        for shot_to_parse in shots:
            with self.subTest(shot_to_parse=shot_to_parse):
                self.game._parse_shot(shot_to_parse)
                self.assertIsNone(self.game.shot)

    def test_switch_turn_hit_ship(self):
        ship_index = None
        active_field_p2 = self.game.player_2['active_field'].copy()
        for s in active_field_p2:
            if 'o' in s:
                ship_index = active_field_p2.index(s), s.index('o')
        self.game.shot = ship_index
        x, y = ship_index
        self.game._switch_turn(self.game.player_1, self.game.player_2)
        self.assertEqual(self.game.player_2['active_field'][x][y], 'x')
        self.assertEqual(self.game.player_1['shots_field'][x][y], 'x')
        self.assertEqual(self.game.player_2['ships'], self.ships_count-1)
        self.assertIsNone(self.game.shot)

    def test_switch_turn_missed(self):
        ship_index = None
        active_field_p2 = self.game.player_2['active_field'].copy()
        for s in active_field_p2:
            if '~' in s:
                ship_index = active_field_p2.index(s), s.index('~')
        self.game.shot = ship_index
        x, y = ship_index
        self.game._switch_turn(self.game.player_1, self.game.player_2)
        self.assertEqual(self.game.player_1['shots_field'][x][y], '*')
        self.assertEqual(self.game.player_2['ships'], self.ships_count)
        self.assertIsNone(self.game.shot)


if __name__ == '__main__':
    unittest.main(buffer=True)
