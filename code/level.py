import random
import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import COLOR_BRANCO, COLOR_AMARELO, COLOR_BRANCO, WIN_HEIGHT, MENU_OPTION, EVENTY_ENEMY
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

        # adiciona fundo
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # adiciona jogador 1
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        # adiciona jogador 2 somente se modo 2 jogadores
        if game_mode == MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENTY_ENEMY, 2500)

        # dicionário para armazenar scores durante o jogo
        self.last_scores = {"Player1": 0, "Player2": 0}

    def get_scores(self):
        return self.last_scores

    def run(self):
        pygame.mixer_music.load('./asset/menu.wav')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENTY_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Atualiza e desenha todas as entidades
            for ent in list(self.entity_list):
                ent.move()

                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shoot()
                    if shot is not None:
                        self.entity_list.append(shot)

                self.window.blit(source=ent.surf, dest=ent.rect)

                # Atualiza scores
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:{ent.health} | Score:{ent.score}', COLOR_AMARELO, (10, 22))
                    self.last_scores["Player1"] = ent.score
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health:{ent.health} | Score:{ent.score}', COLOR_BRANCO, (10, 36))
                    self.last_scores["Player2"] = ent.score

            # Colisões
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            # Verifica se ainda há jogadores vivos
            alive_players = [p for p in self.entity_list if isinstance(p, Player) and p.health > 0]
            if not alive_players:
                pygame.mixer.music.stop()
                return self.get_scores()  # retorna dicionário com pontos atualizados

            # Atualiza a tela
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
