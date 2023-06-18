import pygame
import winsound
from tkinter import simpledialog
import sys
pygame.init()

tamanho = (800,600)
tela = pygame.display.set_mode ( tamanho )
pygame.display.set_caption("Space Marker")


# Criação da janela
janela = pygame.display.set_mode((tamanho))

# Lista para armazenar as posições das estrelas
estrelas = []
nomesEstrelas = []
cordenadasMarcadas = []
name = ""
pos = (0, 0)
white = (255, 255, 255)

# Fonte da escrita
fonte = pygame.font.Font(None, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            estrelas.append(posicao)

            # Abrir um diálogo para obter o nome 
            nome = simpledialog.askstring("Nome", "Digite um nome para a estrela:")
            nomesEstrelas.append(nome)
            print(nomesEstrelas)

            # Adicionar a coordenada marcada
            cordenadasMarcadas.append(posicao)
            print(cordenadasMarcadas)

    # Preencher a janela com a cor de fundo
    fundo = pygame.image.load("background.jpg")
    tela.blit(fundo, (0,0))
    
    # Desenhar as estrelas e os nomes
    for posicao, nome in zip(estrelas, nomesEstrelas):
        pygame.draw.circle(janela, white, posicao, 5)
        texto = fonte.render(nome, True, white)
        tela.blit(texto, (posicao[0], posicao[1] + 10))

    # Atualizar a tela
    pygame.display.update()

pygame.quit()