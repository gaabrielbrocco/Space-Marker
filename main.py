import pygame
import winsound
from tkinter import simpledialog
import sys
import os
import math
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

def calcular_distancia(estrela1, estrela2):
    x1, y1 = estrela1
    x2, y2 = estrela2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia


try:
    while running:
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
                cordenadasMarcadas.append(posicao)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    #Salvar 
                    with open("estrelas_salvas.txt", "w") as arquivo:
                        for estrela, nome in zip(estrelas, nomesEstrelas):
                            arquivo.write(f"{estrela[0]},{estrela[1]},{nome}\n")
                    print("Estrelas marcadas salvas com sucesso!")
                    
                elif event.key == pygame.K_F11:
                    #Carregar
                    if os.path.isfile("estrelas_salvas.txt"):
                        estrelas.clear()
                        nomesEstrelas.clear()
                        with open("estrelas_salvas.txt", "r") as arquivo:
                            linhas = arquivo.readlines()
                            for linha in linhas:
                                x, y, nome = linha.strip().split(",")
                                estrelas.append((int(x), int(y)))
                                nomesEstrelas.append(nome)
                        print("Estrelas marcadas carregadas com sucesso!")
                    else:
                        print("Nenhum arquivo de estrelas salvas encontrado.")
                        
                elif event.key == pygame.K_F12:
                    #Deletar
                    if os.path.isfile("estrelas_salvas.txt"):
                        os.remove("estrelas_salvas.txt")
                        estrelas.clear()
                        nomesEstrelas.clear()
                        print("Estrelas marcadas deletadas com sucesso!")
                    else:
                        print("Nenhum arquivo de estrelas salvas encontrado.")
            #Fechar janela
            elif event.type == pygame.QUIT: 
                running = False
                print("--------------------" "\n" "The game was closed!" "\n" "--------------------")     

        fundo = pygame.image.load("background.jpg")
        tela.blit(fundo, (0,0))
        
        #Mostrar estrelas e nomes
        for posicao, nome in zip(estrelas, nomesEstrelas):
            pygame.draw.circle(janela, white, posicao, 5)
            texto_nome = fonte.render(nome, True, white)
            texto_coordenadas = fonte.render(f"({posicao[0]}, {posicao[1]})", True, white)
            tela.blit(texto_nome, (posicao[0], posicao[1] + 10))
            tela.blit(texto_coordenadas, (posicao[0], posicao[1] + 25))
        if len(estrelas) >= 2:
            for i in range(len(estrelas) - 1):
                pygame.draw.line(tela, white, estrelas[i], estrelas[i+1])
        if len(estrelas) >= 2:
            for i in range(len(estrelas) - 1):
                estrela1 = estrelas[i]
                estrela2 = estrelas[i + 1]
                distancia = calcular_distancia(estrela1, estrela2)

                ponto_medio = ((estrela1[0] + estrela2[0]) // 2, (estrela1[1] + estrela2[1]) // 2)

                texto_distancia = fonte.render(f"Distância: {distancia:.2f}", True, white)
                tela.blit(texto_distancia, (ponto_medio[0], ponto_medio[1] - 10))

                pygame.draw.line(tela, white, estrela1, estrela2)

            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            posicao = pygame.mouse.get_pos()
            estrelas.append(posicao)
            nomesEstrelas.append("desconhecido")
            cordenadasMarcadas.append(posicao)
        
        for posicao, nome in zip(estrelas, nomesEstrelas):
            pygame.draw.circle(janela, white, posicao, 5)
            texto_nome = fonte.render(nome, True, white)
            texto_coordenadas = fonte.render(f"({posicao[0]}, {posicao[1]})", True, white)
            tela.blit(texto_nome, (posicao[0], posicao[1] + 10))
            tela.blit(texto_coordenadas, (posicao[0], posicao[1] + 25))
        

        def comandos():
            texto = fonte.render(salvaPontos,True, white )
            tela.blit(texto, (10,10))
            
            texto = fonte.render(carregaPontos,True, white )
            tela.blit(texto, (10,25))
            
            texto = fonte.render(deletaPontos,True, white )
            tela.blit(texto, (10,40))
        
        comandos()
        
        
        pygame.display.update()

except Exception as e:
    print("Ocorreu um erro!", str(e))

finally:
    pygame.quit()