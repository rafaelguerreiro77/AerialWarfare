# C
import pygame

COLOR_AMARELO = (255, 255, 62)
COLOR_VERDE = (105, 252, 108)
COLOR_BRANCO = (255, 255, 255)
COLOR_RED = (255, 0, 0)

# E
EVENTY_ENEMY = pygame.USEREVENT + 1


ENTITY_SPEED = {
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': -2,
    'Player2Shot': -2,
    'Enemy1': 1,
    'Enemy2': 2,
    'Enemy3': 3,
    'Enemy1Shot': -2,
    'Enemy2Shot': -3,
    'Enemy3Shot': -4
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 90,
    'Enemy2': 60,
    'Enemy3': 30,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1
}

ENTITY_SHOT_DELAY = {
    'Player1': 35,
    'Player2': 35,
    'Enemy1': 150,
    'Enemy2': 150,
    'Enemy3': 150
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEM GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_LCTRL}

#W
WIN_WIDTH = 480
WIN_HEIGHT = 600
