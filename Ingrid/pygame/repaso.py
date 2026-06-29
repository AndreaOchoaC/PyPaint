import pygame

pygame.init()

src_alto = 400
src_ancho = 600
screen = pygame.display.set_mode((src_ancho, src_alto))
pygame.display.set_caption("juego1")


fondo_original = pygame.image.load("fondo_omorii.jpg").convert()
fondo = pygame.transform.scale(fondo_original, (src_ancho, src_alto))
font = pygame.font.SysFont("Arial", 24)


running = True


rect_x = 50
rect_y = 50
speed = 0.5

#funciones
show_popup = False
popup_rect = pygame.Rect(200,100,300,140)
close_buttonrect = pygame.Rect(300,100,100,40)

def draw_popup():
    pygame.draw.rect(screen, "red", popup_rect)
    pygame.draw.rect(screen, "blue", popup_rect, 3)
    pygame.draw.rect(screen, "white", close_buttonrect)
    btn_texto = font.render("cerrar", True, "Black")
    btn_textorect = btn_texto.get_rect(center=close_buttonrect.center)
    
    screen.blit(btn_texto, btn_textorect)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fondo, (0,0))
    
    mouse_pos = pygame.mouse.get_pos()
    


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed
    
    if keys[pygame.K_SPACE]:
        show_popup = True
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if show_popup and close_buttonrect.collidepoint(mouse_pos):
                show_popup = False

        
    if rect_x < 0: rect_x = 0
    if rect_y < 0: rect_y = 0
    if rect_x > 700: rect_x = 700
    if rect_y > 500: rect_y = 500






    pygame.draw.circle(screen, ("#001994"), (rect_x, rect_y), 70)
    
    if show_popup:
        draw_popup()





    pygame.display.update()






pygame.quit()