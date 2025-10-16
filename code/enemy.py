#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.const import ENTITY_SPEED  # importa a constante


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.pos_y = float(self.rect.y)
        self.speed = ENTITY_SPEED.get(name, 1)  # busca velocidade pelo nome (padrão = 1)

    def move(self):
        self.pos_y += self.speed * 0.3  # aplica a velocidade
        self.rect.y = int(self.pos_y)
