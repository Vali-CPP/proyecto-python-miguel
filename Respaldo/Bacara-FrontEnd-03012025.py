import pygame
pygame.init()

#Creando ventana
ventana = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("Baccarat")

fuente = pygame.font.Font(None, 35)
#Colores para los cuadros y textos
blanco = (255, 255, 255)
rojo = (170, 0, 0)
azul = (0, 0, 170)
verde = (80, 135, 80)
negro = (0, 0, 0)
color_del_cuadro = verde

#Carga de imagenes.
mesa = pygame.image.load("Mesa.jpg").convert()
baraja_carta_reverso_crudo = pygame.image.load("reverso_baraja_1.jpg").convert()
baraja_carta_reverso_ajustada = pygame.transform.scale(baraja_carta_reverso_crudo, (100, 150))
menu = pygame.image.load("Menu.jpg").convert()

class Boton:
    def __init__(self, fuente, posicion_x, posicion_y, tamaño_x, tamaño_y, mensaje_texto, mensaje_color):
        self.boton = pygame.Rect(posicion_x, posicion_y, tamaño_x, tamaño_y)
        self.mensaje = fuente.render(str(mensaje_texto), True, tuple(mensaje_color))

    def Dibujar_boton(self, ventana_de_aparicion, boton_color, boton):
        pygame.draw.rect(ventana_de_aparicion, boton_color, boton)

boton_comenzar = Boton(fuente, 503, 508, 150, 50, "Comenzar", blanco)
boton_salir = Boton(fuente, 503, 567, 150, 50, "Salir", blanco)
boton_regresar = Boton(fuente, 1115, 3, 150, 50, "Regresar", blanco)
boton_ingrese_texto_inactivo = Boton(fuente, 540, 390, 200, 70, "Escriba", negro)
boton_ingrese_texto_activo = Boton(fuente, 540, 390, 200, 70, "", blanco)

def mostrar_reverso_de_baraja_en_pantalla():
    ventana.blit(baraja_carta_reverso_ajustada, (600, 105))

def  pantalla_menu():
    ventana.blit(menu, (0 ,0))
    blit_sequence =  [(boton_comenzar.mensaje, (boton_comenzar.boton.x+(boton_comenzar.boton.width - boton_comenzar.mensaje.get_width())/2, boton_comenzar.boton.y+(boton_comenzar.boton.height - boton_comenzar.mensaje.get_height())/2)), (boton_salir.mensaje, (boton_salir.boton.x+(boton_salir.boton.width - boton_salir.mensaje.get_width())/2, boton_salir.boton.y+(boton_salir.boton.height - boton_salir.mensaje.get_height())/2))]
    boton_comenzar.Dibujar_boton(ventana, verde, boton_comenzar.boton)
    boton_salir.Dibujar_boton(ventana, verde, boton_salir.boton)
    ventana.blits(blit_sequence)


def pantalla_para_ingresar_apuesta(contador = 0):
        ventana.blit(mesa, [0, 0])
        mostrar_reverso_de_baraja_en_pantalla()
        pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
        pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
        pygame.draw.line(ventana, blanco, [400,510], [881, 510], 10)
        blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2))]
        
        if contador == 0:
            boton_ingrese_texto_inactivo.Dibujar_boton(ventana, verde, boton_ingrese_texto_inactivo.boton)
            ventana.blit(boton_ingrese_texto_inactivo.mensaje, (boton_ingrese_texto_inactivo.boton.x+(boton_ingrese_texto_inactivo.boton.width - boton_ingrese_texto_inactivo.mensaje.get_width())/2, boton_ingrese_texto_inactivo.boton.y+(boton_ingrese_texto_inactivo.boton.height - boton_ingrese_texto_inactivo .mensaje.get_height())/2))
        
        elif contador == 1:
            boton_ingrese_texto_activo.Dibujar_boton(ventana, blanco, boton_ingrese_texto_activo.boton)
            ventana.blit(texto_ingresado_renderizado, (boton_ingrese_texto_activo.boton.x + 5 - desplazamiento_lateral_del_texto, boton_ingrese_texto_activo.boton.y + 5))
        
        ventana.blits(blit_sequence)
        jugador_texto = fuente.render("Jugador", 50, azul)
        banca_texto = fuente.render("Banca", 50, rojo)
        ingresar_monto_texto = fuente.render("Ingrese el Monto que Desea Apostar ", 50, blanco)
        saldo_actual_texto = fuente.render("Saldo Actual ", 50, blanco)
        blit_sequence_texto = [(jugador_texto, (200, 330)), (banca_texto, (1000, 330)), (ingresar_monto_texto, (430, 330)), (saldo_actual_texto, (560, 530))]
        ventana.blits(blit_sequence_texto)


def pantalla_para_barajeo():
    fuente_para_barajeo = pygame.font.Font(None, 65)
    ventana.blit(mesa, (0, 0))
    mostrar_reverso_de_baraja_en_pantalla()
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2))]
    ventana.blits(blit_sequence)
    jugador_texto = fuente.render("Jugador", 50, azul)
    banca_texto = fuente.render("Banca", 50, rojo)
    barajeo_texto = fuente_para_barajeo.render("Barajeando...", 50, blanco)
    blit_sequence_texto = [(jugador_texto, (200, 330)), (banca_texto, (1000, 330)), (barajeo_texto,(510, 490))]
    ventana.blits(blit_sequence_texto)



def pantalla_para_elegir_apuesta():
    ventana.blit(mesa, [0, 0])
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2))]
    ventana.blits(blit_sequence)
    jugador_texto = fuente.render("Jugador", 50, azul)
    banca_texto = fuente.render("Banca", 50, rojo)
    blit_sequence_texto = [(jugador_texto, (200, 330)), (banca_texto, (1000, 330))]
    ventana.blits(blit_sequence_texto)


juego_iniciado = False
done = True
""""Esto tambien es parte de la logica del cuadro de texto"""
estado_de_boton_ingresar = False
texto_ingresado = ""
boton_ingrese_texto_contador = 0
saldo_del_jugador = 1000
saldo_apostado = 0

while done:

    if juego_iniciado == False:
        pantalla_menu()

    elif juego_iniciado and boton_ingrese_texto_contador == 0:
        pantalla_para_ingresar_apuesta()

    elif juego_iniciado and boton_ingrese_texto_contador == 1:
        pantalla_para_ingresar_apuesta(1)

    elif juego_iniciado and boton_ingrese_texto_contador == 2:
        pantalla_para_barajeo()

    #Inicio del bucle para capturar eventos, todos los eventos de la pantalla son gestionados dentro de este bucle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        #Gestionando la accion del boton Iniciar
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if boton_comenzar.boton.collidepoint(pygame.mouse.get_pos()):
                juego_iniciado = True
            elif boton_salir.boton.collidepoint(pygame.mouse.get_pos()):
                done = False
                boton_ingrese_texto_contador = 0
            elif boton_regresar.boton.collidepoint(pygame.mouse.get_pos()):
                juego_iniciado = False
                boton_ingrese_texto_contador = 0

            #Gestionando la accion del boton Escriba
            if boton_ingrese_texto_inactivo.boton.collidepoint(pygame.mouse.get_pos()):  
                boton_ingrese_texto_contador += 1

        #Este bloque de codigo se encarga de manejar la logica del ingresado de texto durante la primera pantalla:
        if event.type == pygame.KEYDOWN and boton_ingrese_texto_contador == 1:
            if event.key == pygame.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]
            elif (event.key == pygame.K_RETURN or boton_ingrese_texto_contador == 2) and int(texto_ingresado) < saldo_del_jugador:
                saldo_del_jugador -= int(texto_ingresado)
                saldo_apostado = int(texto_ingresado)
                boton_ingrese_texto_contador += 1
            else:
                texto_ingresado += event.unicode


    desplazamiento_lateral_del_texto = 0
    texto_ingresado_renderizado = fuente.render(texto_ingresado, True, negro)
    ancho_del_texto = texto_ingresado_renderizado.get_width()
    
    # Desplazamiento si el texto excede el ancho del cuadro
    if ancho_del_texto > boton_ingrese_texto_inactivo.boton.w - 10:
        desplazamiento_lateral_del_texto = ancho_del_texto - (boton_ingrese_texto_inactivo.boton.w - 10)
    else:
        desplazamiento_lateral_del_texto = 0


    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)

    pygame.display.flip()

pygame.quit()
