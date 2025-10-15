#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH
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
                return Player('Player1', (WIN_WIDTH/2, 525))
