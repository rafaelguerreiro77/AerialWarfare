#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_WIDTH, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 2:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.left < (WIN_WIDTH - 44):
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        pressed_key = pygame.key.get_pressed()
        shoot_key = PLAYER_KEY_SHOOT[self.name]

        # Se a tecla não estiver pressionada, resetamos o delay
        if not pressed_key[shoot_key]:
            self.shot_delay = 0
            return None

        # Se o delay for 0, pode atirar
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]  # inicia o tempo de recarga
            return PlayerShot(
                name=f'{self.name}Shot',
                position=(self.rect.centerx, self.rect.centery)
            )

        # Caso contrário, apenas decrementa o tempo
        else:
            self.shot_delay -= 1
            return None

