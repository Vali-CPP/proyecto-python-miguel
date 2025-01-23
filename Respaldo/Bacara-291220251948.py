import pygame
pygame.init()

#Creando ventana
ventana = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Baccarat")

fuente = pygame.font.Font(None, 32)

class Boton:
    def __init__(self, fuente, posicion_x, posicion_y, tamaño_x, tamaño_y, mensaje_texto, mensaje_color):
        self.boton = pygame.Rect(posicion_x, posicion_y, tamaño_x, tamaño_y)
        self.mensaje = fuente.render(str(mensaje_texto), True, tuple(mensaje_color))

    def Dibujar_boton(self, ventana_de_aparicion, boton_color, boton):
        pygame.draw.rect(ventana_de_aparicion, boton_color, boton)

boton_comenzar = Boton(fuente, 503, 508, 150, 50, "Comenzar", (255,255,255))
boton_salir = Boton(fuente, 503, 567, 150, 50, "Salir", (255,255,255))

def  pantalla_menu():
        menu = pygame.image.load("Menu.jpg").convert()
        ventana.blit(menu, (0 ,0))
        blit_sequence =  [(boton_comenzar.mensaje, (boton_comenzar.boton.x+(boton_comenzar.boton.width - boton_comenzar.mensaje.get_width())/2, boton_comenzar.boton.y+(boton_comenzar.boton.height - boton_comenzar.mensaje.get_height())/2)), (boton_salir.mensaje, (boton_salir.boton.x+(boton_salir.boton.width - boton_salir.mensaje.get_width())/2, boton_salir.boton.y+(boton_salir.boton.height - boton_salir.mensaje.get_height())/2))]
        boton_comenzar.Dibujar_boton(ventana, (100,100,100), boton_comenzar.boton)
        boton_salir.Dibujar_boton(ventana, (100, 100, 100), boton_salir.boton)
        ventana.blits(blit_sequence)

def pantalla_juego_iniciado():
        mesa = pygame.image.load("Mesa.jpg").convert()
        ventana.blit(mesa, [0, 0])


juego_iniciado = False
done = True

while done:

    if juego_iniciado == False:
        pantalla_menu()
    else:
        pantalla_juego_iniciado()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if boton_comenzar.boton.collidepoint(pygame.mouse.get_pos()):
                juego_iniciado = True
            elif boton_salir.boton.collidepoint(pygame.mouse.get_pos()):
                done = False
    
    pygame.display.flip()

pygame.quit()