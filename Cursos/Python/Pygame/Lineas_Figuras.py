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
color_fondo = (255,255 ,255)
colorlinea = (255, 0, 0)
clock=pygame.time.Clock()
def rojo():
    posx1=random.randrange(0,1920)
    posy1=random.randrange(0,1080)
    posx=random.randrange(0,1920)
    posy=random.randrange(0,1080)
    tamaño=random.randrange(0,10)
    pygame.draw.line(ventana, (0,0,0),(posx,posy),(posx1,posy1),tamaño)
def verde():
    posx1=random.randrange(0,1920)
    posy1=random.randrange(0,1080)
    posx=random.randrange(0,1920)
    posy=random.randrange(0,1080)
    tamaño=random.randrange(0,10)
    pygame.draw.line(ventana, (255,0,0),(posx,posy),(posx1,posy1),tamaño)
"""
def azul():
    posx2=random.randrange(0,1920)
    posy2=random.randrange(0,1080)
    posx1=random.randrange(0,1920)
    posy1=random.randrange(0,1080)
    pygame.draw.line(ventana, (0,0,255),(posx1,posy1),(posx2,posy2),1)
pygame.display.update()
"""


while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    rojo()
    verde()
    #azul()
    pygame.display.update()
    #clock.tick(10)