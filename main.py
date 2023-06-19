import pygame
import winsound
from tkinter import simpledialog
import sys
pygame.init()

tamanho = (800,600)
tela = pygame.display.set_mode ( tamanho )
pygame.display.set_caption("Space Marker")
rocket = pygame.image.load("rocket.png")
pygame.display.set_icon(rocket)
pygame.mixer.music.load("eletroMusic.mp3")
pygame.mixer.music.play(-1)

janela = pygame.display.set_mode((tamanho))

estrelas = []
nomesEstrelas = []
cordenadasMarcadas = []
name = ""
pos = (0, 0)
white = (255, 255, 255)
fonte = pygame.font.Font(None, 20)
running = True
salvaPontos = "Pressione F10 para SALVAR os pontos marcados"
carregaPontos = "Pressione F11 para CARREGAR os pontos marcados anteriormente"
deletaPontos = "Pressione F12 para DELETAR os pontos"

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            estrelas.append(posicao)

            # Perguntar o nome da estrela 
            nome = simpledialog.askstring("Nome", "Digite um nome para a estrela:")
            nomesEstrelas.append(nome)
            print(nomesEstrelas)

            # Adicionar a coordenada marcada
            cordenadasMarcadas.append(posicao)
            print(cordenadasMarcadas)

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            posicao = pygame.mouse.get_pos()
            estrelas.append(posicao)
            nomesEstrelas.append("desconhecido")
            cordenadasMarcadas.append(posicao)
            

    fundo = pygame.image.load("background.jpg")
    tela.blit(fundo, (0,0))
    
    # Desenhar as estrelas e os nomes
    for posicao, nome in zip(estrelas, nomesEstrelas):
        pygame.draw.circle(janela, white, posicao, 5)
        texto_nome = fonte.render(nome, True, white)
        texto_coordenadas = fonte.render(f"({posicao[0]}, {posicao[1]})", True, white)
        tela.blit(texto_nome, (posicao[0], posicao[1] + 10))
        tela.blit(texto_coordenadas, (posicao[0], posicao[1] + 25))
    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            pygame.draw.line(tela, white, estrelas[i], estrelas[i+1])

    def comandos():
        texto = fonte.render(salvaPontos,True, white )
        tela.blit(texto, (10,10))
        
        texto = fonte.render(carregaPontos,True, white )
        tela.blit(texto, (10,25))
        
        texto = fonte.render(deletaPontos,True, white )
        tela.blit(texto, (10,40))
    
    comandos()
    
    
    pygame.display.update()

pygame.quit()