"""Setting module"""
from enum import Enum

PLAYER_LIVES = 5
ALLOWED_ATTACKS = Enum('allowed_attacks', 'WIZARD, WARRIOR, ROGUE')
ALLOWED_COMMANDS = ('start', 'help', 'score', 'exit')
