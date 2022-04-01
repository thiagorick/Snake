from cgitb import text
import imp
from operator import le
from random import randint
from tkinter import font
from turtle import pos
import pygame
from pygame.locals import *

pygame.init()

CIMA = K_UP
BAIXO = K_DOWN
DIREITA = K_RIGHT
ESQUERDA = K_LEFT

passo = 10
pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

# TELA
tamanho_tela = (600, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Snake')

# SNAKE
snake_pos = [(300, 300)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 255, 0))
snake_direção = ESQUERDA

# APPLE
def pos_aleatoria():
    x = randint(0, tamanho_tela[0])
    y = randint(0, tamanho_tela[1])
    x = x // passo * passo
    y = y // passo * passo
    return x, y
apple_pos = pos_aleatoria()
apple_skin = pygame.Surface((passo, passo))
apple_skin.fill((255, 0, 0))


# função de colisão com a apple
def colisao(pos1, pos2):
    return pos1 == pos2


# função de colisão com a parede
def colisao_parede(snake_pos):
    if 0 <= snake_pos[0] < tamanho_tela[0] and 0 <= snake_pos[1] < tamanho_tela[1]:
        return False
    else:
        return True

# função para reiniciar o jogo
def restart():
    global snake_pos
    global apple_pos
    global snake_direção
    snake_pos = [(300, 300)]
    snake_direção = ESQUERDA
    apple_pos = pos_aleatoria()


while True:

    # limitar a velocidade da snake
    pygame.time.Clock().tick(15)

    # limpar a tela
    tela.fill((0, 0, 0))

    # pontuação
    mesagem = f'Pontos: {pontos}'
    texto = fonte.render(mesagem, True,(255, 255, 255))
    
    # verificar eventos
    for event in pygame.event.get():

        # se clicar em fechar, fechar
        if event.type == QUIT:
            pygame.quit()
            quit()

        # verificar o botão para movimentar
        if event.type == KEYDOWN:
            if event.key in [CIMA, BAIXO, ESQUERDA, DIREITA]:
                    snake_direção = event.key

    # verifica colisão com parede
    if colisao_parede(snake_pos[0]):
        restart()
        pontos = 0
            
    # desenhando snake
    for position in snake_pos:
        tela.blit(snake_skin, position)

    # desenhando a apple
    tela.blit(apple_skin, apple_pos)
    tam_snake = len(snake_pos) -1

    # fazer o corpo acompanhar a snake
    for i in range(tam_snake, 0, -1):
        snake_pos[i] = snake_pos[i-1]

    # pegar a apple
    if colisao(snake_pos[0], apple_pos):
        snake_pos.append(snake_pos[tam_snake])
        apple_pos = pos_aleatoria()
        pontos += 1

    # movimentação da snake
    if snake_direção == CIMA:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] - passo
    if snake_direção == BAIXO:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] + passo
    if snake_direção == ESQUERDA:
        snake_pos[0] = snake_pos[0][0] - passo, snake_pos[0][1]
    if snake_direção == DIREITA:
        snake_pos[0] = snake_pos[0][0] + passo, snake_pos[0][1]
    
    tela.blit(texto, (370, 0))

    pygame.display.update()
