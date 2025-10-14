#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print('Setup start')
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))
        print('Setup end')

        while True:
            # check por todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
