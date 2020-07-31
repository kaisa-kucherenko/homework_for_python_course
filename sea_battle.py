import random
import os
from time import sleep


class SeaBattleGame:
    Rules = """
Hello, players!
Now you will play 'Sea Battle'.
The game is designed for 2 players. Each player has 8 single-deck ships.
The first to destroy the opponent's ships will win.
Legend:
You will have 2 fields. On the left is an active field with your ships.
On the right is a field with the history of your shots at enemy ships.
'~' - empty cell
'o' - active ship
'x' - destroyed ship
'*' - miss shot
Enter the x and y coordinates for the shot, separated by commas. 
x and y can be integers from 1 to 10.
            """

    def __init__(self, ships_count=8):
        self.ships_count = ships_count
        self.player_1 = {'name': None,
                         'ships': self.ships_count,
                         'active_field': self._set_ships(),
                         'shots_field': self._generate_field()}
        self.player_2 = {'name': None,
                         'ships': self.ships_count,
                         'active_field': self._set_ships(),
                         'shots_field': self._generate_field()}
        self.shot = None

    @staticmethod
    def _generate_field():
        field = [['~'] * 10 for i in range(10)]
        return field

    def _set_ships(self):
        field = self._generate_field()
        ships_number = self.ships_count
        while ships_number > 0:
            rand_x = random.randint(0, 9)
            field[rand_x][0] = 'o'
            random.shuffle(field[rand_x])
            ships_number -= 1
        return field

    @staticmethod
    def _show_fields(player):
        print('Active field'.center(28), 'Shots field'.center(43))
        for x in range(10):
            print(f"{'  '.join(player['active_field'][x])} \t\t "
                  f"{'  '.join(player['shots_field'][x])}", end='')
            print()

    def _parse_shot(self, shot):
        try:
            shot = shot.split(',')
            x = int(shot[0])
            y = int(shot[1])
            if 0 < x <= 10 and 0 < y <= 10:
                self.shot = (x-1, y-1)
            else:
                print('x and y must be from 1 to 10')
        except Exception:
            print('Enter x comma y \nx and y must be from 1 to 10')

    def _switch_turn(self, player_turn, player_wait):
        print(f"Your move, {player_turn['name']}")
        self._show_fields(player_turn)
        while self.shot is None:
            shot = input(f"Please enter x,y coordinates "
                         f"for shot, {player_turn['name']}: ")
            self._parse_shot(shot)
        x, y = self.shot
        if player_wait['active_field'][x][y] == 'o':
            player_wait['active_field'][x][y] = 'x'
            player_turn['shots_field'][x][y] = 'x'
            player_wait['ships'] -= 1
            if player_wait['ships'] == 0:
                print(f"Congrats, {player_turn['name']}, you hit last ship. "
                      f"And win this game!!!")
            else:
                print(f"Congrats, {player_turn['name']}, you hit the ship")
                sleep(4)
                os.system('cls||clear')

        else:
            player_turn['shots_field'][x][y] = '*'
            print(f"Auch, {player_turn['name']} you were close. "
                  f"Maybe next time you hit the target")
            sleep(4)
            os.system('cls||clear')
        self.shot = None

    def run(self):
        print(self.Rules)
        self.player_1['name'] = input('Pleas enter your name, player №1: ')
        self.player_2['name'] = input('Pleas enter your name, player №2: ')
        while True:
            if self.player_1['ships']:
                self._switch_turn(self.player_1, self.player_2)
            else:
                break
            if self.player_2['ships']:
                self._switch_turn(self.player_2, self.player_1)
            else:
                break


if __name__ == '__main__':
    game = SeaBattleGame()
    game.run()
