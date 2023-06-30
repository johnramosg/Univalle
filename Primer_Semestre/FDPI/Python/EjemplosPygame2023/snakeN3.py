import pygame
import random

def dibujarCuadros():
    for i in range(1,101,1):
        x=random.randrange(0,400)
        y=random.randrange(0,300)       
        pygame.draw.rect(ventana, fucsia, [x,y,10,10])
        pygame.display.update()
    
pygame.init()
pygame.display.set_caption("Cuadros aleatorios")
ventana = pygame.display.set_mode((400,300))
  
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange= (255, 69, 0)
lightskyblue= (135, 206, 250)
fucsia= (255, 0, 255)

ventana.fill(black)
pygame.display.update()

continuar=True
dibujarCuadros()

while (continuar==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuar = False
