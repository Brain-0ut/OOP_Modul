"""Models module"""
from random import randint
from exceptions import GameOver, EnemyDown
from settings import ALLOWED_ATTACKS, PLAYER_LIVES


class Enemy:
    """class Enemy"""
    level = 0

    def __init__(self):
        Enemy.level += 1
        self.level = Enemy.level
        self.lives = Enemy.level

    @staticmethod
    def select_attack():
        """select_attack for Enemy"""
        return randint(1, 3)

    def decrease_lives(self):
        """decrease_lives for Enemy"""
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    """class Player"""

    def __init__(self, name, allowed_attacks=ALLOWED_ATTACKS, lives=PLAYER_LIVES, score=0):
        self.name = name
        self.allowed_attacks = allowed_attacks
        self.lives = lives
        self.score = score
        self.result = {'Attack was successful': 0,
                       'Attack was down': 0,
                       'Attack was draw': 0,
                       'Defense was successful': 0}

    @staticmethod
    def fight(attack, defense):
        """fight for the game"""
        if (attack == 1 and defense == 2) or (attack == 2 and defense == 3) \
                or (attack == 3 and defense == 1):
            result = 1
        elif attack == defense:
            result = 0
        else:
            result = -1
        return result

    def decrease_lives(self):
        """decrease_lives for Player"""
        self.lives -= 1
        if not self.lives:
            raise GameOver

    def attack(self, enemy_obj):
        """attack for Player"""
        attack = self.character_choice('attack')
        enemy_attack = enemy_obj.select_attack()
        result = self.fight(attack=attack, defense=enemy_attack)
        self.print_round_text(attack, enemy_attack)
        if result == 0:
            print('It\'s a DRAW!')
            self.result['Attack was draw'] += 1
        elif result == 1:
            print('You attack was successful!')
            self.result['Attack was successful'] += 1
            self.score += 1
            enemy_obj.decrease_lives()
        else:
            print('You attack was down!')
            self.result['Attack was down'] += 1

    def defense(self, enemy_obj):
        """defence for Player"""
        defense = self.character_choice('defense')
        enemy_attack = enemy_obj.select_attack()
        result = self.fight(attack=enemy_attack, defense=defense)
        self.print_round_text(attack=defense, enemy_attack=enemy_attack)
        if result != 1:
            print('You defense was successful!')
            self.result['Defense was successful'] += 1
        else:
            print('You defense was down!')
            self.decrease_lives()

    def character_choice(self, call_from):
        """character_choice"""
        all_attack = [x.value for x in self.allowed_attacks]
        choice = None
        while choice not in all_attack:
            try:
                print('{}, choose yor character for {}:'.format(self.name, call_from))
                for all_att in self.allowed_attacks:
                    print(all_att.name + " - " + str(all_att.value))
                choice = int(input())
                if choice not in all_attack:
                    raise ValueError
            except ValueError:
                print('Type from 1 to 3, please!')
        return choice

    def print_round_text(self, attack, enemy_attack):
        """print_round_text"""
        player_char = [all_att.name for all_att in self.allowed_attacks
                       if all_att.value == attack][0]
        pc_char = [all_att.name for all_att in self.allowed_attacks
                   if all_att.value == enemy_attack][0]
        print('In this round you choose {} and PC choose {}'.format(player_char, pc_char))


class Score:
    """class Score"""

    def __init__(self, fp):
        self.fp = fp

    def save_score(self, player):
        """save_score"""
        score_list = [[player.name + ':', str(player.score)]]
        for line in self.read_score():
            score_list.append(line.split(' '))
        score_list = sorted(score_list, key=lambda x: x[::-1], reverse=True)
        if len(score_list) > 10:
            score_list.pop()
        self.save_to_file(score_list)

    def print_score(self):
        """print_score"""
        for line in self.read_score():
            print(line)

    def read_score(self):
        """read_score"""
        res = []
        with open(self.fp, 'r') as score_file:
            for line in score_file:
                res.append(line.strip())
        score_file.close()
        return res

    def save_to_file(self, score_list):
        """save_to_file"""
        with open(self.fp, 'w') as score_file:
            for line in score_list:
                line_to_file = line[0] + ' ' + line[1] + '\n'
                score_file.write(line_to_file)
        score_file.close()
