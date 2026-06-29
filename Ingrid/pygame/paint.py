import pygame
import sys

pygame.init()

src_alto = 400
src_ancho = 425
screen = pygame.display.set_mode((src_ancho, src_alto))
pygame.display.set_caption("alien.paint")

fondo_original = pygame.image.load("paint_png.jpg").convert_alpha()
fondo = pygame.transform.scale(fondo_original, (src_ancho, src_alto))


drawing = False
color = (0,0,0)
radius = 5
background_color = (255, 255, 255)
screen.fill(background_color)
font = pygame.font.SysFont('Calibri', 18)




x1 = 20
y1 = 20
x2 = 40
y2 = 40
x3 = 60
y3 = 60


screen.blit(fondo, (0,0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False



    

    if drawing:
        pos = pygame.mouse.get_pos()
        #pygame.draw.circle(screen, color, pos, radius)
        pygame.draw.polygon(screen, 'blue', [(x1, y1), (x2, y2), (x3, y3)], 5)


        x1 += 20
        y1 += 20
        x2 += 40
        y2 += 40
        x3 += 60
        y3 += 60

        











    pygame.display.update()