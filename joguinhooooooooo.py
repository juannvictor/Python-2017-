# Trabalho de Pygame - Linguagem de Progamação 1
# Professora - Ana Grasieli
# Nome: Juan Victor Dutra Juan
# TIA: 31711081

import random, sys, time, math, pygame
from pygame.locals import *

fps = 30 # Taxa de FPS do jogo
l_tela = 640 # Largura da tela do jogo
h_tela = 480 # Altura da tela do jogo
metade_l = int(l_tela / 2)
metade_h = int(h_tela / 2)

grama_cor = (24, 255, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


mov_camera = 90 # Velocidade do jogador antes de mudar a câmera
vel = 9 # Velocidade do jogador
pulo = 6 # Velocidade do pulo (mais velocidade = mais devagar o pulo)
pulo_h = 30 # Altura máxima do pulo do jogador
tam_inicial = 25 # Tamanho inicial do jogador
tam_vitoria = 300 # Tamanho que o jogador precisa chegar para ganhar o jogo
tempo_inv = 2 # Quanto tempo o jogador fica invunerável em seg após a colisão
tempo_go = 5 # Quanto tempo a tela de game over fica na tela em segundos
vida_max = 4 # Quanta vida o jogador possui no inicio do jogo

num_grama = 80 # Número de objetos da grama na área ativa
num_ini = 30 # Número de inimigos na área ativa
ini_velmin = 3 # Velocidade mínima dos inimigos
ini_velmax = 7 # Velocidade máxima dos inimigos
direcao_mudar = 3 # Porcentagem de chance da direção do objeto mudar p frame
direita = "right"
esquerda = "left"



def main():
    global fps_tempo, tela_jogo

    pygame.init()
    fps_tempo = pygame.time.Clock()
    # pygame.display_set.icon(pygame.image.load('icone do jogo'))
    tela_jogo = pygame.display.set_mode((l_tela, h_tela))
    
    

