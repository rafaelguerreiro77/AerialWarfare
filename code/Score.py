import pygame
import sys
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_RED, COLOR_VERDE, COLOR_GREEN, COLOR_BLACK


class Score:
    def __init__(self, window):
        self.window = window
        self.last_scores = {"Player1": 0, "Player2": 0}
        self.game_mode = None  # define no Game.run antes de chamar show_score()

    def show_score(self):
        pygame.mixer_music.load('./asset/gameover.wav')
        pygame.mixer_music.play()

        """Mostra a tela final de scores"""
        background = pygame.image.load('./asset/score.png').convert()
        background = pygame.transform.scale(background, (480, 600))  # ajusta ao tamanho da janela
        self.window.blit(background, (0, 0))

        # título
        text_font = pygame.font.SysFont("Arial Black", 42)
        title = text_font.render("GAME OVER", True, (255, 255, 0))
        title_rect = title.get_rect(center=(WIN_WIDTH // 2, 120))
        self.window.blit(title, title_rect)

        # Player1
        text_font_small = pygame.font.SysFont("Arial Black", 22)
        p1_score = text_font_small.render(f"Player 1: {self.last_scores['Player1']} pontos", True, COLOR_VERDE)
        p1_rect = p1_score.get_rect(center=(WIN_WIDTH // 2, 240))
        self.window.blit(p1_score, p1_rect)

        # Player2 (só mostra se for modo 2 jogadores)
        if self.game_mode == MENU_OPTION[1]:
            p2_score = text_font_small.render(f"Player 2: {self.last_scores['Player2']} pontos", True, COLOR_GREEN)
            p2_rect = p2_score.get_rect(center=(WIN_WIDTH // 2, 280))
            self.window.blit(p2_score, p2_rect)

        # instrução para continuar
        text_continue = text_font_small.render("Pressione ENTER para voltar ao menu", True, COLOR_BLACK)
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
