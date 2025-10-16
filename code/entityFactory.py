#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # primeira
                    list_bg.append(Background(f'Level1Bg{i}', (0, -WIN_HEIGHT)))  # segunda logo acima
                return list_bg
            case 'Player1':
                return Player('Player1', ((WIN_WIDTH/2 - 25), 525))
            case 'Player2':
                return Player('Player2', ((WIN_WIDTH / 2 + 25), 525))
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(0, WIN_WIDTH - 40), random.randint(-150, -50)))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(0, WIN_WIDTH - 40), random.randint(-150, -50)))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(0, WIN_WIDTH - 40), random.randint(-150, -50)))