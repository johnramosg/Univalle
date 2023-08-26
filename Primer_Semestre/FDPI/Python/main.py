from pygame.locals import *
import pygame,sys

def posicion():
    print(pygame.mouse.get_pos())



pygame.init()
win=pygame.display.set_mode((300,300))
pygame.display.set_caption("Hola")
fuente=pygame.font.SysFont("italic",70)
texto=fuente.render("Salo",True,(255,0,0))


pygame.draw.circle(win,(255,0,0),(110,100),50)
pygame.draw.circle(win,(255,0,0),(190,100),50)
pygame.draw.circle(win,(0,0,0),(110,100),45)
pygame.draw.circle(win,(0,0,0),(190,100),45)
pygame.draw.line(win,(255,0,0),(68,125),(145,250),5)
pygame.draw.line(win,(255,0,0),(230,125),(145,250),5)
pygame.draw.line(win,(0,0,0),(205, 137),(95, 140),37)
pygame.draw.line(win,(0,0,0),(216, 129),(196, 157),16)
pygame.draw.line(win,(0,0,0),(79, 125),(103, 168),14)
win.blit(texto, [100, 110])

while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        if evento.type==MOUSEBUTTONUP:
            posicion()
    pygame.display.update()