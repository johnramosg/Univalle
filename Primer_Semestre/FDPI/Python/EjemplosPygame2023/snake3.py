import pygame
import random

def dibujarCuadrado():
    x1 = random.randrange(0,400)
    y1 = random.randrange(0,300)
    pygame.draw.rect(ventana, green, [x1,y1,10,10])
    pygame.display.update()

pygame.init()
pygame.display.set_caption("Usando el teclado")
ventana = pygame.display.set_mode((400,300))
  
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange= (255, 69, 0)
lightskyblue= (135, 206, 250)

ventana.fill(black)
pygame.display.update()

continuar=True
while (continuar==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dibujarCuadrado()
            
