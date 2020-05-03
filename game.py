"""Main module"""
# coding: utf-8
from exceptions import EnemyDown, GameOver
from models import Enemy, Player, Score
from settings import ALLOWED_COMMANDS


def _help():
    """Print the 'HELP' info"""
    print('This is my AWESOME INTERACTIVE GAME!!!\n'
          'Allowed commands in my game:')
    for all_comm in ALLOWED_COMMANDS:
        print(all_comm)
    input('Press any key')


def start(player, enemy):
    """Start fight"""
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
            print('-'*50)
            print('{}, you have {} lives and you score is {}'
                  .format(player.name, player.lives, player.score))
            print('Start the NEXT ROUND! FIGHT!!!')
            print('-' * 50)
        except EnemyDown:
            player.score += 5
            enemy = Enemy()
            print('!'*50)
            print('CONGRATULATIONS! {}, you WON this fight!'.format(player.name))
            print('{}, you score - {}'.format(player.name, player.score))
            print('!' * 50)
            print('Welcome to LEVEL {}! Let`s START to fight!'.format(enemy.level))
        except GameOver:
            print('#' * 50)
            print('ACHTUNG!!! {}, you DIED in this GAME!!!'.format(player.name))
            print('{}, you final score - {}'.format(player.name, player.score))
            for key, item in player.result.items():
                print('{}: {}'.format(key, item))
            print('#' * 50)
            score = Score('scores.txt')
            score.save_score(player)
            choice = input('{}, did you want to START another GAME (Y/N)? '
                           .format(player.name)).lower()
            if choice != 'y':
                raise KeyboardInterrupt
            player = Player(player.name)


def play():
    """Main function"""
    print('Hello in my AWESOME GAME!!!')
    name = input('Tell me yor NAME, my brave player: ')
    player = Player(name)
    enemy = Enemy()
    score = Score('scores.txt')
    while True:
        print('_'*50)
        print('{}, make your choice!'.format(player.name))
        print('For start the GAME type "START"')
        print('For help about GAME type "HELP"')
        print('For view the scores of game type "SCORE"')
        print('For exit from GAME type "EXIT"')
        choice = input('>>>  ').lower()
        while choice not in ALLOWED_COMMANDS:
            choice = input('You are funny one))))\n'
                           'Try one more time: ')
        if choice == 'start':
            start(player, enemy)
        elif choice == 'help':
            _help()
        elif choice == 'score':
            score.print_score()
        else:
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('I hope you enjoyed the game')
    finally:
        print('Good bye!')
