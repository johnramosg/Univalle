import pygame
import random

pygame.init()
pygame.display.set_caption("Movimientos")
ventana = pygame.display.set_mode((600,400))
  
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

x1 = random.randrange(0,600)
y1 = random.randrange(0,400)
pygame.draw.rect(ventana, green, [x1,y1,10,10])
pygame.display.update()
                  
desplazamiento_X=0
desplazamiento_Y=0

while (continuar==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                desplazamiento_X = -10
                desplazamiento_Y = 0
            elif event.key == pygame.K_RIGHT:
                desplazamiento_X = 10
                desplazamiento_Y = 0
            elif event.key == pygame.K_UP:
                desplazamiento_X = 0
                desplazamiento_Y = -10
            elif event.key == pygame.K_DOWN:
                desplazamiento_X = 0
                desplazamiento_Y = 10

            x1 += desplazamiento_X
            y1 += desplazamiento_Y
            print(x1,y1)
            pygame.draw.rect(ventana, green, [x1,y1,10,10])
            pygame.display.update()
           
