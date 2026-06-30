# Versión 1 25/Jun/26

import pygame
import sys
from tools_paint import *

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi PyPaint") # el texto que sale en la ventana del juego

icono = pygame.image.load("MEDIA/paint_icon.png")
pygame.display.set_icon(icono)

fondo_original = pygame.image.load("MEDIA/Interfaz1_600x600.png").convert()
fondo = pygame.transform.scale(fondo_original, (WIDTH, HEIGHT)) # escalar a la pantalla
screen.blit(fondo, (0,0)) # llenar pantalla con la imagen

# Confg inicial del pincel
drawing = False
color = (0, 0, 0)
radius = 5
background_color = (255, 255, 255)
#screen.fill(background_color)
font = pygame.font.SysFont('Calibri', 18)

# EXTRA: Cambiar el cursor
custom_cursor = pygame.image.load("MEDIA/cursor1.png").convert_alpha()
custom_cursor = pygame.transform.scale(custom_cursor, (40, 40))
#pygame.mouse.set_visible(False)

# cursor personalizado DEBE IR DENTRO DEL CICLO
# pero ahorita entra en conflicto con nuestro fondo
'''pos = pygame.mouse.get_pos()
screen.blit(custom_cursor, pos)'''
# opción "propia" de pygame
#pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

# ---------- ELEMENTOS DE LA INTERFAZ ----------

# PALETA DE COLORES
colores = {
    "negro": "#000000",
    "gris": "#808080",
    "blanco": "#FFFFFF",
    "rojo": "#FF0000",
    "marrón": "#800000",
    "amarillo": "#FFFF00",
    "verde": "#008000",
    "verde_claro": "#00FF00",
    "verde_azulado": "#008080",
    "cian": "#00FFFF",
    "azul": "#0000FF",
    "azul_claro": "#00CCFF",
    "violeta": "#800080",
    "magenta": "#FF00FF",
    "rosa": "#FF99CC",
    "naranja": "#FF8000"
}

# Convertirlos a RGB (o bien crear el diccionario con RGBs desde el principio)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

colores_rgb = {nombre: hex_to_rgb(hex) for nombre, hex in colores.items()}

# Diccionario con RGBs
colores_dic_rgb = {
    "negro": (0, 0, 0),
    "gris": (128, 128, 128),
    "blanco": (255, 255, 255),
    "rojo": (255, 0, 0),
    "marrón": (128, 0, 0),
    "amarillo": (255, 255, 0),
    "verde": (0, 128, 0),
    "verde_claro": (0, 255, 0),
    "verde_azulado": (0, 128, 128),
    "cian": (0, 255, 255),
    "azul": (0, 0, 255),
    "azul_claro": (0, 204, 255),
    "violeta": (128, 0, 128),
    "magenta": (255, 0, 255),
    "rosa": (255, 153, 204),
    "naranja": (255, 128, 0)
}


# Dibujar paleta de colores (recuadro por recuadro)
cuadros = []
size_cuadro = 40
y_base = HEIGHT - size_cuadro - 40  # margen inferior

# creamos un Rect(x, y, ancho, alto) para cada recuadro de la paleta

for i, (nombre, rgb) in enumerate(colores_rgb.items()):
    rect = pygame.Rect(25 + i*(size_cuadro+5), y_base, size_cuadro, size_cuadro)
    cuadros.append((rect, nombre, rgb))

# BARRA DE HERRAMIENTAS

# crear una clase para el objeto "herramienta"
class Herramienta:
    def __init__(self, nombre, icono_path, x, y, tamaño=40):
        self.nombre = nombre
        self.icono = pygame.image.load(icono_path)
        self.icono = pygame.transform.scale(self.icono, (tamaño, tamaño))
        self.rect = pygame.Rect(x, y, tamaño, tamaño)
        self.seleccionada = False

    def dibujar(self, screen):
        screen.blit(self.icono, self.rect)
        if self.seleccionada == True:
            color_borde = (0,0, 255)
            grosor_borde = 4
        else:
            color_borde = (0,0,0)
            grosor_borde = 2

        pygame.draw.rect(screen, color_borde, self.rect, grosor_borde)

    def clic(self, pos):
        return self.rect.collidepoint(pos)

# crear todas las herramientas que necesitemos

nombresH = ["free_form", "select_rect", "borrar", "fill",
            "cuentagotas", "lupa", "pencil", "paintbrush",
            "airbrush", "texto", "line", "curve", "rectangle",
            "polygon", "elipse", "rounded_rect"]

herramientas = []
size_tool = 40
margen= 10 

'''for h in nombresH:
    nombre_h = h
    path_h = f"IconosMSPaint/{h}.png"
    i = nombresH.index(h)
    tool = Herramienta(nombre_h, path_h, 10, 10+i*50 )
    herramientas.append(tool)'''

# Versión 2 columnas
for i, nombre_h in enumerate(nombresH):
    fila = i // 2   # número de fila
    col = i % 2     # columna (0 = izquierda, 1 = derecha)
    x = 25 + col * (size_tool + margen)
    y = 115 + fila * (size_tool + margen)
    path_h = f"IconosMSPaint/{nombre_h}.png"
    tool = Herramienta(nombre_h, path_h, x, y, size_tool)
    herramientas.append(tool)

# RECUADRO QUE MUESTRA COLOR SELECCIONADO Y TAMAÑO DEL PINCEL
# creamos un Rect(x, y, ancho, alto)
current_color_rect = pygame.Rect(20, 10, 100, 80)
pygame.draw.rect(screen, (255,255,255), current_color_rect)
pygame.draw.circle(screen, color, (current_color_rect.x + 50, current_color_rect.y + 40), radius)
pygame.draw.rect(screen, (0,0,0), current_color_rect, 2)

# Ciclo de juego

while True:

    # --------- DIBUJAR ELEMENTOS DE LA INTERFAZ ----------
    # Paleta de colores
    for rect, nombre, rgb in cuadros:
        pygame.draw.rect(screen, rgb, rect)
        pygame.draw.rect(screen, (0,0,0), rect, 2)  # borde negro

    # Barra de herramientas
    for h in herramientas:
        h.dibujar(screen)
    
    # Texto de la interfaz
    texto = font.render("¡Comienza a dibujar!", True, (255, 255, 255))
    screen.blit(texto, (200, 20))

    # Establecer límite del lienzo (área de dibujo)
    lienzo_rect = pygame.Rect(150, 100, 600, 400)
    pygame.draw.rect(screen, (255,255,255), lienzo_rect, 2)  # borde

    # ---------- DETECTAR EVENTOS ----------
    for event in pygame.event.get():
        # pygame.quit() es lo opuesto a pygame.init(), reinicia todo y sale del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Comienza/termina de dibujar con el mouse presionado
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            # revisar si se hace click en un color
            pos = pygame.mouse.get_pos()
            for rect, nombre, rgb in cuadros:
                if rect.collidepoint(pos):
                    color_seleccionado = rgb
                    print("Color elegido:", nombre)

                    # mostrar el color actual en el recuadro de color seleccionado
                    pygame.draw.rect(screen, (255,255,255), current_color_rect)
                    pygame.draw.circle(screen, color_seleccionado, (current_color_rect.x + 50, current_color_rect.y + 40), radius*1.5)
                    pygame.draw.rect(screen, (0,0,0), current_color_rect, 2)

            # revisar si se hace click en una herramienta
            for h in herramientas:
                if h.clic(pos):
                    for a in herramientas:
                        a.seleccionada = False
                    h.seleccionada = True
                    print("Herramienta seleccionada:", h.nombre)

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Cambiar color o limpiar pantalla
        elif event.type == pygame.KEYDOWN:
            if event.key in colores:
                # cambiar de color con teclas # PENDIENTE CAMBIO CON CLICK
                color = colores[event.key]
            elif event.key == pygame.K_c:
                # borra todo el dibujo con C
                screen.fill(background_color)
            elif event.key == pygame.K_q:
                # salimos del juego al presionar la tecla Q
                pygame.quit()
                sys.exit()


    # Dibujar en la pantalla
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, pos, radius)
        #limitar a solo dibujar dentro del lienzo (falta refinar)
        if not lienzo_rect.collidepoint(pos):
            drawing = False

    # Para dibujar con Pygame
    # pygame.draw.circle(surface, color, center, radius, width=0)
    # también tiene opción de - line(), rect(), ellipse(), polygon()
    # ejemplo: pygame.draw.polygon(screen,'blue',[(100,100),(100,200),(200,300)],0)

    pygame.display.flip()