import pygame
pygame.init()
pygame.display.set_caption("Figuras en Pygame")
ventana = pygame.display.set_mode((400,300))
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
orange= (255, 69, 0)
white = (255, 255, 255)
ventana.fill(white)
pygame.draw.rect(ventana, blue, [30, 200, 80, 80])
pygame.draw.rect(ventana, red, [200, 100, 10, 10])
pygame.draw.rect(ventana, green, [370, 0, 30, 30])
pygame.draw.circle(ventana, orange, [200,280], 20)
pygame.display.update()

continuar=True
while (continuar==True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                continuar = False
