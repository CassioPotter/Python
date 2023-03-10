import pygame 
#importa a biblioteca pygame inteira

# Definindo as cores
PRETO = (0, 0, 0) 
#ausencia de todas as cores
BRANCO = (255, 255, 255) 
#todas as cores no maximo
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definindo PI
PI = 3.1416

# Inicializamos os módulos de Pygame
pygame.init() 
#inicia o pygame

# Criamos a janela com título Figuras e texto
janela = pygame.display.set_mode((500, 400)) 
#cria uma janela como uma tupla de 500px por 400px  
pygame.display.set_caption('Figuras e Texto') 
#texto da janela

# Preenchendo o fundo da janela com a cor branca
janela.fill(BRANCO) 
#cobre a superficie da janela de branco

# Trabalhando com texto
fonte = pygame.font.Font(None, 48) 
#nome da fonte seguido pelo seu tamanho
texto = fonte.render('Olá, mundo!', True, BRANCO, AZUL) 
#texto , cor da fonte, cor do fundo
janela.blit(texto, [30, 150]) 
#janela do texto

# Desenhando figuras
pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)),0) 
#onde esta, cor, os 3 vertices"pontos onde se encontra" no caso 3 pois e um triangulo
pygame.draw.circle(janela, AZUL, (300, 50), 20, 0)
pygame.draw.ellipse(janela, VERMELHO, (400, 250, 40, 80), 1)
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, VERMELHO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2, 2)

# mostrando na tela tudo o que foi desenhado
pygame.display.update()
deve_continuar = True

while deve_continuar:

 #Loop para checar eventos
     for event in pygame.event.get():

 #Condicional para sair do loop
        if event.type == pygame.QUIT:
            deve_continuar = False

pygame.quit()