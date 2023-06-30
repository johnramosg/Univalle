import pygame, sys,random,time
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode(
    (
        1920,
        1080,
    )
)
pygame.display.set_caption("Titulo de la ventana")
color_fondo = (1, 150, 70)
colorlinea = (255, 0, 0)
clock=pygame.time.Clock()
def rojo():
    posx=random.randrange(0,1920)
    posy=random.randrange(0,1080)
    pygame.draw.line(ventana, (255,0,0),(posx,posy),(posx,posy),40)
def verde():
    posx1=random.randrange(0,1920)
    posy1=random.randrange(0,1080)
    pygame.draw.line(ventana, (0,255,0),(posx1,posy1),(posx1,posy1),40)
def azul():
    posx2=random.randrange(0,1920)
    posy2=random.randrange(0,1080)
    pygame.draw.line(ventana, (0,0,255),(posx2,posy2),(posx2,posy2),40)
pygame.display.update()



while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    rojo()
    verde()
    azul()
    pygame.display.update()
    #clock.tick(1000)