import pygame
import sys
from code.Score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()  # retorna opção escolhida

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:  # Modo 1 ou 2 jogadores
                level = Level(self.window, 'Level1', menu_return)
                level_scores = level.run()  # retorna dicionário com os scores

                # configura o Score para exibir
                score.last_scores = level_scores
                score.game_mode = menu_return
                score.show_score()  # sem passar argumento
            elif menu_return == MENU_OPTION[-1]:  # sair
                pygame.quit()
                sys.exit()
