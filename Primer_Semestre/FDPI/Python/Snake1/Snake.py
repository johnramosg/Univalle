#Importar librerías.
import pygame
import sys
import random
import time

#Definición de las funciones de Puntajes y Juego terminado.
def Snake1Score(Puntuacion1):
    texto=fuente.render("Snake: "+str(Puntuacion1),True,red)
    ventana.blit(texto, [20,0])
    
def velocidadS(velocidad):
    texto=fuente.render(f"Velocidad: {str(velocidad)}m/s",True,black)
    ventana.blit(texto, [280,0])
    
def juegoTerminado():
    if (Puntuacion1==30):
        texto = fuente.render("Snake CAMPEÓN", True, red)
        ventana.blit(texto, [280, alto/2])
        
        
#Dimensiones de la ventana y elementos.
ancho=800
alto=600
radio=15

#Configuración de la ventana.
pygame.init()
ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption('Snake🐍-Two Players')
fuente=pygame.font.SysFont('Consolas',30)
#Imágenes y contenido.
fondo = pygame.image.load("imagenes/back-ground.jpg")
serpiente_01 = pygame.image.load("imagenes/serpent-head-02.png")
serpiente_02 = pygame.image.load("imagenes/serpent-head-01.png")
egg = pygame.image.load("imagenes/ball.png")
icono = pygame.image.load("imagenes/serpent-icon.png")
ventana.blit(fondo,(0,0))
pygame.display.set_icon(icono)

#Sonidos
obtener=pygame.mixer.Sound("sonidos/obtener.mp3")
Victoria=pygame.mixer.Sound("sonidos/sonido3.mp3")
pygame.mixer.music.load("sonidos/sonido2.mp3")
pygame.mixer.music.play()


#Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (8, 168, 13)

#Velocidad Snake
clock = pygame.time.Clock()

#Snake 1
Snake1_x=random.randrange(0,ancho,20)
Snake1_y=random.randrange(0,alto,20)
ventana.blit(serpiente_01, [Snake1_x,Snake1_y,20,20])
movimiento_x1=0
movimiento_y1=0


#Comida Snake
Comida_x=random.randrange(0,ancho,20)
Comida_y=random.randrange(0,alto,20)
ventana.blit(egg,[Comida_x,Comida_y,20,20])
Puntuacion1=0
velocidad=10
#Actualizar la ventana

velocidadS(velocidad)
Snake1Score(Puntuacion1)
juegoTerminado()
pygame.display.update()

jugando=True
en_pausa=False

#Bucle principal
while jugando:
    #Recorre todos los eventos  
    for evento in pygame.event.get():
        #Cerrar la ventana
        if evento.type==pygame.QUIT:
            sys.exit()   
        #Movimientos Snake 1
        if evento.type==pygame.KEYDOWN and evento.key!=pygame.K_DOWN and evento.key!=pygame.K_UP and evento.key!=pygame.K_LEFT and evento.key!=pygame.K_RIGHT:
            if evento.key==pygame.K_a and movimiento_x1!=20:
                movimiento_x1=-20
                movimiento_y1=0
            elif evento.key==pygame.K_d and movimiento_x1!=-20:
                movimiento_x1=20
                movimiento_y1=0
            elif evento.key==pygame.K_w and movimiento_y1!=20:
                movimiento_x1=0
                movimiento_y1=-20
            elif evento.key==pygame.K_s and movimiento_y1!=-20:
                movimiento_x1=0
                movimiento_y1=20
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    en_pausa = not en_pausa  # Cambiar entre pausa y juego

    if not en_pausa:
        Snake1_x+=movimiento_x1
        Snake1_y+=movimiento_y1
        ventana.blit(fondo,(0,0))
        velocidadS(velocidad)
        Snake1Score(Puntuacion1)
        juegoTerminado()
        ventana.blit(egg,[Comida_x,Comida_y,20,20])
        ventana.blit(serpiente_01, [Snake1_x,Snake1_y,20,20])
        pygame.display.update()
        
        if(Puntuacion1==30):
            ventana.blit(fondo,(0,0))
            pygame.mixer.music.stop()
            Victoria.play()
            juegoTerminado()
            time.sleep(20)
            sys.exit() 
            
        if(Snake1_x==Comida_x and Snake1_y==Comida_y):
            Puntuacion1+=1
            velocidad+=5
            obtener.play()
            print('Encontraste la comida snake 1')
            ventana.blit(serpiente_01, [Snake1_x,Snake1_y,20,20])
            Snake1Score(Puntuacion1)
            velocidadS(velocidad)
            Comida_x=random.randrange(0,ancho,20)
            Comida_y=random.randrange(0,alto,20)
            ventana.blit(egg,[Comida_x,Comida_y,20,20])
        #Aparecer en el lado opuesto
        if Snake1_x<=0:
                Snake1_x=ancho
        elif Snake1_x>=ancho:
                Snake1_x=0
        if Snake1_y<=0:
                Snake1_y=alto
        elif Snake1_y>=alto:
                Snake1_y=0

        ventana.blit(fondo,(0,0))
    # Lógica para pausa
    while en_pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                en_pausa = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    en_pausa = not en_pausa  # Cambiar entre pausa y juego

    velocidadS(velocidad)
    
                
    clock.tick(velocidad)