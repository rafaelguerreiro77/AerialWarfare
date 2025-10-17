#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import COLOR_BRANCO, WIN_HEIGHT, MENU_OPTION, EVENTY_ENEMY, COLOR_GREEN, COLOR_CYAN, COLOR_AMARELO
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENTY_ENEMY, 2500)

    def run(self):
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:{ent.health} | Score:{ent.score}', COLOR_AMARELO, (10, 22))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health:{ent.health} | Score:{ent.score}', COLOR_BRANCO, (10, 36))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTY_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False


            # printed text
            # self.level_text(14, f'{self.name}', COLOR_BRANCO, (10,5))
            # self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_BRANCO, (10, WIN_HEIGHT - 35))
            # self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_BRANCO, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

