import pygame

def dibujarCirculo():
    pos=pygame.mouse.get_pos()
    pygame.draw.circle(ventana, blue, pos, 20)
    pygame.display.update()
    
pygame.init()
pygame.display.set_caption("Usando el mouse")
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
        if event.type == pygame.MOUSEBUTTONUP:
            dibujarCirculo()
            
