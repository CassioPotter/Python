import pygame

pygame.init()

janela= pygame.display.set_mode((400,300))
pygame.display.set_caption('OLA MUNDO')
pygame.display.set_caption('OLA MUNDO', icontitle=None)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

pygame.quit()