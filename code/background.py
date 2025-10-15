#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.pos_y = float(self.rect.y)  # guarda posição real em float

    def move(self):
        self.pos_y += 0.1  # velocidade lenta e suave
        self.rect.y = int(self.pos_y)

        # reposiciona quando a imagem sair da tela
        if self.rect.top >= 600:        # ou WIN_HEIGHT
            self.pos_y = -self.rect.height
            self.rect.y = int(self.pos_y)
        pass
