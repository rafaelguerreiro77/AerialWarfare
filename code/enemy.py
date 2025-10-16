#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.entity import Entity
from code.const import ENTITY_SPEED, ENTITY_SHOT_DELAY  # importa a constante


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.pos_y = float(self.rect.y)
        self.speed = ENTITY_SPEED.get(name, 1)  # busca velocidade pelo nome (padrão = 1)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.pos_y += self.speed * 0.3  # aplica a velocidade
        self.rect.y = int(self.pos_y)

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
