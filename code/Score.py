import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Score:
    def __init__(self, window):
        self.window = window
        self.last_scores = {"Player1": 0, "Player2": 0}
        self.game_mode = None  # define no Game.run antes de chamar show_score()

    def show_score(self):
        """Mostra a tela final de scores"""
        self.window.fill((0, 0, 0))  # fundo preto

        # título
        text_font = pygame.font.SysFont("Arial Black", 36)
        title = text_font.render("FIM DE JOGO", True, (255, 255, 0))
        title_rect = title.get_rect(center=(WIN_WIDTH // 2, 120))
        self.window.blit(title, title_rect)

        # Player1
        text_font_small = pygame.font.SysFont("Arial", 24)
        p1_score = text_font_small.render(f"Player 1: {self.last_scores['Player1']} pontos", True, (255, 255, 255))
        p1_rect = p1_score.get_rect(center=(WIN_WIDTH // 2, 240))
        self.window.blit(p1_score, p1_rect)

        # Player2 (só mostra se for modo 2 jogadores)
        if self.game_mode == MENU_OPTION[1]:
            p2_score = text_font_small.render(f"Player 2: {self.last_scores['Player2']} pontos", True, (200, 200, 200))
            p2_rect = p2_score.get_rect(center=(WIN_WIDTH // 2, 280))
            self.window.blit(p2_score, p2_rect)

        # instrução para continuar
        text_continue = text_font_small.render("Pressione ENTER para voltar ao menu", True, (255, 255, 0))
        cont_rect = text_continue.get_rect(center=(WIN_WIDTH // 2, 500))
        self.window.blit(text_continue, cont_rect)

        pygame.display.flip()

        # espera até o jogador pressionar Enter ou fechar
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    waiting = False
