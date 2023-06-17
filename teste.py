import pygame
import sys
from pygame import *
from tkinter import simpledialog, Tk

# Inicializa o Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)

# Configurações da janela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bolinha e Nome')

# Variáveis para armazenar a posição e o nome
pos = (0, 0)
name = ""

# Loop principal do jogo
while True:
    # Verifica eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Exibe uma janela de diálogo para inserir o nome
            root = Tk()
            root.withdraw()
            name = simpledialog.askstring("Nome", "Digite seu nome:")
            pygame.display.set_caption('Bolinha e Nome - ' + name)
            root.destroy()

            # Obtém a posição do clique do mouse
            pos = pygame.mouse.get_pos()

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha a bolinha branca
    pygame.draw.circle(screen, WHITE, pos, 20)

    # Renderiza o nome abaixo da bolinha
    font = pygame.font.SysFont(None, 24)
    text = font.render(name, True, WHITE)
    text_rect = text.get_rect(center=(pos[0], pos[1] + 30))
    screen.blit(text, text_rect)

    # Atualiza a tela
    pygame.display.update()