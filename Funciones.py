import pygame
from time import sleep

pygame.init()

fuente_pequeña = pygame.font.Font(None, 35)
fuente_mediana = pygame.font.Font(None, 45)
fuente_grande = pygame.font.Font(None, 65)
blanco = (255, 255, 255)
rojo = (170, 0, 0)
azul = (0, 0, 170)
verde = (80, 135, 80)
negro = (0, 0, 0)
gris = (100, 100, 100)

def mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada):
    pila_de_cartas = [(baraja_carta_reverso_ajustada, (585, 95)), (baraja_carta_reverso_ajustada, (595, 105)), (baraja_carta_reverso_ajustada, (605, 115)), (baraja_carta_reverso_ajustada, (615, 125))]
    ventana.blits(pila_de_cartas)

def renderizar_texto_jugador_mesa(ventana, fuente, jugador_texto_pos_x=200, jugador_texto_pos_y=330, banca_texto_pos_x=1000, banca_texto_pos_y=330):
        jugador_texto = fuente.render("Jugador", 50, azul)
        banca_texto = fuente.render("Banca", 50, rojo)
        blit_sequence_texto = [(jugador_texto, (jugador_texto_pos_x, jugador_texto_pos_y)), (banca_texto, (banca_texto_pos_x, banca_texto_pos_y))]
        ventana.blits(blit_sequence_texto)

def  pantalla_menu(ventana, imagen_menu, boton_comenzar, boton_salir):
    ventana.blit(imagen_menu, (0 ,0))
    boton_salir.Crear_superficie()
    boton_comenzar.Crear_superficie()
    blit_sequence =  [(boton_comenzar.mensaje, (boton_comenzar.boton.x+(boton_comenzar.boton.width - boton_comenzar.mensaje.get_width())/2, boton_comenzar.boton.y+(boton_comenzar.boton.height - boton_comenzar.mensaje.get_height())/2)), (boton_salir.mensaje, (boton_salir.boton.x+(boton_salir.boton.width - boton_salir.mensaje.get_width())/2, boton_salir.boton.y+(boton_salir.boton.height - boton_salir.mensaje.get_height())/2))]
    boton_comenzar.Dibujar_boton(ventana, verde, boton_comenzar.boton)
    boton_salir.Dibujar_boton(ventana, verde, boton_salir.boton)
    ventana.blits(blit_sequence)

def pantalla_para_ingresar_apuesta(ventana, imagen_mesa, texto_saldo_actual_grande, baraja_carta_reverso_ajustada, boton_regresar, boton_ingrese_texto_inactivo, boton_ingrese_texto_activo, texto_ingresado_renderizado, desplazamiento_lateral_del_texto, fuente,  contador = 0):
    ventana.blit(imagen_mesa, [0, 0])
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    pygame.draw.line(ventana, blanco, [400,510], [881, 510], 10)
    boton_regresar.Crear_superficie()
    boton_ingrese_texto_activo.Crear_superficie()
    boton_ingrese_texto_inactivo.Crear_superficie()
    texto_saldo_actual_grande.Crear_superficie()
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_grande.mensaje, (texto_saldo_actual_grande.boton.x+(texto_saldo_actual_grande.boton.width - texto_saldo_actual_grande.mensaje.get_width())/2, texto_saldo_actual_grande.boton.y+(texto_saldo_actual_grande.boton.height - texto_saldo_actual_grande.mensaje.get_height())/2))]
    
    if contador == 0:
        boton_ingrese_texto_inactivo.Dibujar_boton(ventana, verde, boton_ingrese_texto_inactivo.boton)
        ventana.blit(boton_ingrese_texto_inactivo.mensaje, (boton_ingrese_texto_inactivo.boton.x+(boton_ingrese_texto_inactivo.boton.width - boton_ingrese_texto_inactivo.mensaje.get_width())/2, boton_ingrese_texto_inactivo.boton.y+(boton_ingrese_texto_inactivo.boton.height - boton_ingrese_texto_inactivo .mensaje.get_height())/2))
    
    elif contador == 1:
        boton_ingrese_texto_activo.Dibujar_boton(ventana, blanco, boton_ingrese_texto_activo.boton)
        ventana.blit(texto_ingresado_renderizado, (boton_ingrese_texto_activo.boton.x + 5 - desplazamiento_lateral_del_texto, boton_ingrese_texto_activo.boton.y + 5))
        
    ventana.blits(blit_sequence)
    renderizar_texto_jugador_mesa(ventana, fuente)
    ingresar_monto_texto = fuente.render("Ingrese el Monto que Desea Apostar ", 50, blanco)
    saldo_actual_texto = fuente.render("Saldo Actual ", 50, blanco)
    blit_sequence_texto = [(ingresar_monto_texto, (430, 330)), (saldo_actual_texto, (560, 530))]
    ventana.blits(blit_sequence_texto)

def pantalla_para_barajeo(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar):
    ventana.blit(imagen_mesa, (0, 0))
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    boton_regresar.Crear_superficie()
    texto_saldo_actual_esquina.Crear_superficie()
    texto_saldo_apostado_esquina.Crear_superficie()
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_esquina.mensaje, (texto_saldo_actual_esquina.boton.x+(texto_saldo_actual_esquina.boton.width - texto_saldo_actual_esquina.mensaje.get_width())/2, texto_saldo_actual_esquina.boton.y+(texto_saldo_actual_esquina.boton.height - texto_saldo_actual_esquina.mensaje.get_height())/2)), (texto_saldo_apostado_esquina.mensaje, (texto_saldo_apostado_esquina.boton.x+(texto_saldo_apostado_esquina.boton.width - texto_saldo_apostado_esquina.mensaje.get_width())/2, texto_saldo_apostado_esquina.boton.y+(texto_saldo_apostado_esquina.boton.height - texto_saldo_apostado_esquina.mensaje.get_height())/2))]
    ventana.blits(blit_sequence)
    renderizar_texto_jugador_mesa(ventana, fuente_pequeña)
    barajeo_texto = fuente_grande.render("Barajeando...", 50, blanco)
    blit_sequence_texto = [(barajeo_texto,(510, 490))]
    ventana.blits(blit_sequence_texto)

def pantalla_para_elegir_apuesta(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_apuesta_jugador, boton_apuesta_banca, boton_regresar):
    ventana.blit(imagen_mesa, [0, 0])
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    secuencia_de_cartas_barajeadas = [(baraja_carta_reverso_ajustada, (120, 105)), (baraja_carta_reverso_ajustada, (250, 105)), (baraja_carta_reverso_ajustada, (380, 105)), (baraja_carta_reverso_ajustada, (820, 105)), (baraja_carta_reverso_ajustada, (950, 105)), (baraja_carta_reverso_ajustada, (1080, 105))]
    ventana.blits(secuencia_de_cartas_barajeadas)
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    boton_regresar.Crear_superficie()
    boton_apuesta_banca.Crear_superficie()
    boton_apuesta_jugador.Crear_superficie()
    texto_saldo_apostado_esquina.Crear_superficie()
    texto_saldo_actual_esquina.Crear_superficie()
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_esquina.mensaje, (texto_saldo_actual_esquina.boton.x+(texto_saldo_actual_esquina.boton.width - texto_saldo_actual_esquina.mensaje.get_width())/2, texto_saldo_actual_esquina.boton.y+(texto_saldo_actual_esquina.boton.height - texto_saldo_actual_esquina.mensaje.get_height())/2)), (texto_saldo_apostado_esquina.mensaje, (texto_saldo_apostado_esquina.boton.x+(texto_saldo_apostado_esquina.boton.width - texto_saldo_apostado_esquina.mensaje.get_width())/2, texto_saldo_apostado_esquina.boton.y+(texto_saldo_apostado_esquina.boton.height - texto_saldo_apostado_esquina.mensaje.get_height())/2)), (boton_apuesta_jugador.mensaje, (boton_apuesta_jugador.boton.x+(boton_apuesta_jugador.boton.width - boton_apuesta_jugador.mensaje.get_width())/2, boton_apuesta_jugador.boton.y+(boton_apuesta_jugador.boton.height - boton_apuesta_jugador.mensaje.get_height())/2)), (boton_apuesta_banca.mensaje, (boton_apuesta_banca.boton.x+(boton_apuesta_banca.boton.width - boton_apuesta_banca.mensaje.get_width())/2, boton_apuesta_banca.boton.y+(boton_apuesta_banca.boton.height - boton_apuesta_banca.mensaje.get_height())/2))]
    boton_apuesta_jugador.Dibujar_boton(ventana, azul, boton_apuesta_jugador.boton)
    boton_apuesta_banca.Dibujar_boton(ventana, rojo, boton_apuesta_banca.boton)
    ventana.blits(blit_sequence)
    elegir_apuesta_texto = fuente_grande.render("¿A quien apostaras?", 50, blanco)
    blit_sequence_texto = [(elegir_apuesta_texto, (425, 360))]
    ventana.blits(blit_sequence_texto)
    renderizar_texto_jugador_mesa(ventana, fuente_grande, 155, 465, 975, 465)
    

#def pantalla_para_mostrar_cartas(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar):



def congelamiento_barajeo(tiempo_de_congelamiento):
    sleep(tiempo_de_congelamiento)
    return True