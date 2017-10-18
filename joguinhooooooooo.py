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
tempo_godMode = 2 # Quanto tempo o jogador fica invunerável em seg após a colisão
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
    global fps_tempo, tela_jogo, fonte_basica, obj_esq, obj_dir, img_grama

    pygame.init()
    fps_tempo = pygame.time.Clock()
    # pygame.display_set.icon(pygame.image.load('icone do jogo'))
    tela_jogo = pygame.display.set_mode((l_tela, h_tela))
    pygame.display.set_caption('Nome do joguinho')
    fonte_basica = pygame.font.Font('freesansbold.ttf',30)

    #Arquivos de imagem
    obj_esq = pygame.image.load('imagem para a esquerda')
    obj_dir = pygame.transform.flip(obj_esq, True, False)
    img_grama = []
    for i in range(1,5):
        img_grama.append(pygame.image.load('imagem da grama' % i))

    while True:
        runGame()

def runGame():
    
    # Variáveis de início do jogo
    godMode = False # Se o jogador estiver invunerável
    godModeStart = 0
    gameOver = False
    gameOverStart = 0 # Perdeu
    win_mode = False # Ganhou

    gameOver_tela = fonte_basica.render('Game Over', True, vermelho)
    gameOver_retangulo = gameOver_tela.get_rect()
    gameOver_retangulo.center = (metade_l, metade_h)

    win_tela = fonte_basica.render('Você atingiu o tamanho máximo!', True, branco)
    win_retangulo = win_tela.get_rect()
    win_retangulo.center = (metade_l, metade_h)

    win_tela2 = fonte_basica.render('(Pressione "r" para recomeçar.)', True, branco)
    win_retangulo2 = win_tela2.get_rect()
    win_retangulo2.center = (metade_l, metade_h + 30)

    # Visão da câmera
    camerax = 0
    cameray = 0

    objetos_grama = [] # Onde todos os objetos no cenário estarão
    objetos_inimigos = [] # Onde todos os inimigos estarão

    # Informações do objeto do jogador

    objeto_jogador = {'surface': pygame.transform.scale(obj_esq, (tam_inicial, tam_inicial)),
                      'rosto': esquerda,
                      'tamanho': tam_inicial,
                      'x': metade_l,
                      'y': metade_h,
                      'pulo': 0,
                      'vida': vida_max}

    moverEsq = False
    moverDir = False
    moverUp = False
    moverDown = False

    # Gramas aleatórias

    for i in range(10):
        objetos_grama.append(criarGrama(camerax, cameray))
        objetos_grama[i]['x'] = random.randint(0, l_tela)
        objetos_grama[i]['y'] = random.randint(0, h_tela)

    while True: # principal loop do game
        # você quer @invulnerabilidade?
        if godMode and time.time() - godModeStart > tempo_godMode:
            godMode = False

        # movendo todos os inimigos
        for inimigos in objetos_inimigos:
            # movendo os inimigos e ajustando o pulo deles
            inimigos['x'] += inimigos['movex']
            inimigos['y'] += inimigos['movey']
            inimigos['pulo'] += 1
            if inimigos['pulo'] > inimigos['taxapulo']:
                inimigos['pulo'] = 0 # ressetando o pulo alheio

            # chance randômica dos inimigos trocarem de lado
            if random.randint(0,99) < direcao_mudar:
                inimigos['movex'] = 
