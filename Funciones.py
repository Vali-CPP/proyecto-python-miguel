import pygame
from time import sleep

pygame.init()

fuente_pequeña = pygame.font.Font(None, 35)
fuente_mediana = pygame.font.Font(None, 45)
fuente_grande = pygame.font.Font(None, 65)
fuente_mas_grande = pygame.font.Font(None, 100)
blanco = (255, 255, 255)
rojo = (170, 0, 0)
azul = (0, 0, 170)
verde = (80, 135, 80)
negro = (0, 0, 0)
gris = (100, 100, 100)

#Funciones miscelanias

def mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada):
    pila_de_cartas = [(baraja_carta_reverso_ajustada, (585, 95)), (baraja_carta_reverso_ajustada, (595, 105)), (baraja_carta_reverso_ajustada, (605, 115)), (baraja_carta_reverso_ajustada, (615, 125))]
    ventana.blits(pila_de_cartas)

def renderizar_texto_jugador_mesa(ventana, fuente, texto_jugador_pos_x=200, texto_jugador_pos_y=330, texto_banca_pos_x=1000, texto_banca_pos_y=330):
        texto_jugador = fuente.render("Jugador", 50, azul)
        texto_banca = fuente.render("Banca", 50, rojo)
        blit_sequence_texto = [(texto_jugador, (texto_jugador_pos_x, texto_jugador_pos_y)), (texto_banca, (texto_banca_pos_x, texto_banca_pos_y))]
        ventana.blits(blit_sequence_texto)

def renderizar_texto_ganador_mesa(ventana, fuente, texto_felicidades_pos_x=450, texto_felicidades_pos_y=120, texto_ganaste_pos_x=500, texto_ganaste_pos_y=190):
    texto_felicidades = fuente.render("¡Felicidades", 50, blanco)
    texto_ganaste = fuente.render("Ganaste!", 50, blanco) 
    blit_sequence_texto = [(texto_felicidades,(texto_felicidades_pos_x, texto_felicidades_pos_y)), (texto_ganaste, (texto_ganaste_pos_x, texto_ganaste_pos_y))]
    ventana.blits(blit_sequence_texto)

def renderizar_texto_perdedor_mesa(ventana, fuente, texto_lastima_pos_x=500, texto_lastima_pos_y=120, texto_perdiste_pos_x=500, texto_perdiste_pos_y=190):
    texto_lastima = fuente.render("¡Lastima", 50, blanco)
    texto_perdiste = fuente.render("Perdiste!", 50, blanco) 
    blit_sequence_texto = [(texto_lastima,(texto_lastima_pos_x, texto_lastima_pos_y)), (texto_perdiste, (texto_perdiste_pos_x, texto_perdiste_pos_y))]
    ventana.blits(blit_sequence_texto)

def renderizar_texto_empate_mesa(ventana, fuente, texto_empate_pos_x=490, texto_empate_pos_y=120):
    texto_empate = fuente.render("¡Empate!", 50, blanco)
    ventana.blit(texto_empate,(texto_empate_pos_x, texto_empate_pos_y))

#Pantallas

def  pantalla_menu(ventana, imagen_menu, boton_comenzar, boton_salir):
    ventana.blit(imagen_menu, (0 ,0))
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
    blit_sequence_boton =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_grande.mensaje, (texto_saldo_actual_grande.boton.x+(texto_saldo_actual_grande.boton.width - texto_saldo_actual_grande.mensaje.get_width())/2, texto_saldo_actual_grande.boton.y+(texto_saldo_actual_grande.boton.height - texto_saldo_actual_grande.mensaje.get_height())/2))]
    
    if contador == 0:
        boton_ingrese_texto_inactivo.Dibujar_boton(ventana, verde, boton_ingrese_texto_inactivo.boton)
        ventana.blit(boton_ingrese_texto_inactivo.mensaje, (boton_ingrese_texto_inactivo.boton.x+(boton_ingrese_texto_inactivo.boton.width - boton_ingrese_texto_inactivo.mensaje.get_width())/2, boton_ingrese_texto_inactivo.boton.y+(boton_ingrese_texto_inactivo.boton.height - boton_ingrese_texto_inactivo .mensaje.get_height())/2))
    
    elif contador == 1:
        boton_ingrese_texto_activo.Dibujar_boton(ventana, blanco, boton_ingrese_texto_activo.boton)
        ventana.blit(texto_ingresado_renderizado, (boton_ingrese_texto_activo.boton.x + 5 - desplazamiento_lateral_del_texto, boton_ingrese_texto_activo.boton.y + 5))
        
    ventana.blits(blit_sequence_boton)
    renderizar_texto_jugador_mesa(ventana, fuente)
    texto_ingresar_monto = fuente.render("Ingrese el Monto que Desea Apostar ", 50, blanco)
    texto_saldo_actual = fuente.render("Saldo Actual ", 50, blanco)
    blit_sequence_texto = [(texto_ingresar_monto, (430, 330)), (texto_saldo_actual, (560, 530))]
    ventana.blits(blit_sequence_texto)

def pantalla_para_barajeo(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar):
    ventana.blit(imagen_mesa, (0, 0))
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    blit_sequence =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_esquina.mensaje, (texto_saldo_actual_esquina.boton.x+(texto_saldo_actual_esquina.boton.width - texto_saldo_actual_esquina.mensaje.get_width())/2, texto_saldo_actual_esquina.boton.y+(texto_saldo_actual_esquina.boton.height - texto_saldo_actual_esquina.mensaje.get_height())/2)), (texto_saldo_apostado_esquina.mensaje, (texto_saldo_apostado_esquina.boton.x+(texto_saldo_apostado_esquina.boton.width - texto_saldo_apostado_esquina.mensaje.get_width())/2, texto_saldo_apostado_esquina.boton.y+(texto_saldo_apostado_esquina.boton.height - texto_saldo_apostado_esquina.mensaje.get_height())/2))]
    ventana.blits(blit_sequence)
    renderizar_texto_jugador_mesa(ventana, fuente_pequeña)
    texto_barajeo = fuente_grande.render("Barajeando...", 50, blanco)
    blit_sequence_texto = [(texto_barajeo,(510, 490))]
    ventana.blits(blit_sequence_texto)

def pantalla_para_elegir_apuesta(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_apuesta_jugador, boton_apuesta_banca, boton_regresar):
    ventana.blit(imagen_mesa, [0, 0])
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    secuencia_de_cartas_barajeadas = [(baraja_carta_reverso_ajustada, (120, 105)), (baraja_carta_reverso_ajustada, (250, 105)), (baraja_carta_reverso_ajustada, (380, 105)), (baraja_carta_reverso_ajustada, (820, 105)), (baraja_carta_reverso_ajustada, (950, 105)), (baraja_carta_reverso_ajustada, (1080, 105))]
    ventana.blits(secuencia_de_cartas_barajeadas)
    pygame.draw.line(ventana, blanco, [400,311], [400, 700], 10)
    pygame.draw.line(ventana, blanco, [886,311], [886, 700], 10)
    blit_sequence_boton =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_esquina.mensaje, (texto_saldo_actual_esquina.boton.x+(texto_saldo_actual_esquina.boton.width - texto_saldo_actual_esquina.mensaje.get_width())/2, texto_saldo_actual_esquina.boton.y+(texto_saldo_actual_esquina.boton.height - texto_saldo_actual_esquina.mensaje.get_height())/2)), (texto_saldo_apostado_esquina.mensaje, (texto_saldo_apostado_esquina.boton.x+(texto_saldo_apostado_esquina.boton.width - texto_saldo_apostado_esquina.mensaje.get_width())/2, texto_saldo_apostado_esquina.boton.y+(texto_saldo_apostado_esquina.boton.height - texto_saldo_apostado_esquina.mensaje.get_height())/2)), (boton_apuesta_jugador.mensaje, (boton_apuesta_jugador.boton.x+(boton_apuesta_jugador.boton.width - boton_apuesta_jugador.mensaje.get_width())/2, boton_apuesta_jugador.boton.y+(boton_apuesta_jugador.boton.height - boton_apuesta_jugador.mensaje.get_height())/2)), (boton_apuesta_banca.mensaje, (boton_apuesta_banca.boton.x+(boton_apuesta_banca.boton.width - boton_apuesta_banca.mensaje.get_width())/2, boton_apuesta_banca.boton.y+(boton_apuesta_banca.boton.height - boton_apuesta_banca.mensaje.get_height())/2))]
    boton_apuesta_jugador.Dibujar_boton(ventana, azul, boton_apuesta_jugador.boton)
    boton_apuesta_banca.Dibujar_boton(ventana, rojo, boton_apuesta_banca.boton)
    ventana.blits(blit_sequence_boton)
    texto_elegir_apuesta = fuente_grande.render("¿A quien apostaras?", 50, blanco)
    blit_sequence_texto = [(texto_elegir_apuesta, (425, 360))]
    ventana.blits(blit_sequence_texto)
    renderizar_texto_jugador_mesa(ventana, fuente_grande, 155, 465, 975, 465)

def pantalla_para_mostrar_cartas(ventana, imagen_mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar, mano_imagenes_jugador, mano_imagenes_banca, puntaje_jugador, puntaje_banca):
    ventana.blit(imagen_mesa, [0, 0])
    mazo_de_barajeo(ventana, baraja_carta_reverso_ajustada)
    pygame.draw.line(ventana,blanco, [640,311], [640,700], 10)
    blit_sequence_boton =  [(boton_regresar.mensaje, (boton_regresar.boton.x+(boton_regresar.boton.width - boton_regresar.mensaje.get_width())/2, boton_regresar.boton.y+(boton_regresar.boton.height - boton_regresar.mensaje.get_height())/2)), (texto_saldo_actual_esquina.mensaje, (texto_saldo_actual_esquina.boton.x+(texto_saldo_actual_esquina.boton.width - texto_saldo_actual_esquina.mensaje.get_width())/2, texto_saldo_actual_esquina.boton.y+(texto_saldo_actual_esquina.boton.height - texto_saldo_actual_esquina.mensaje.get_height())/2)), (texto_saldo_apostado_esquina.mensaje, (texto_saldo_apostado_esquina.boton.x+(texto_saldo_apostado_esquina.boton.width - texto_saldo_apostado_esquina.mensaje.get_width())/2, texto_saldo_apostado_esquina.boton.y+(texto_saldo_apostado_esquina.boton.height - texto_saldo_apostado_esquina.mensaje.get_height())/2))]
    ventana.blits(blit_sequence_boton)
    bs_imagenes_carta_volteadas = [(mano_imagenes_jugador[0], (120, 105)), (mano_imagenes_jugador[1], (250, 105)), (mano_imagenes_jugador[2], (380, 105)), (mano_imagenes_banca[0], (820, 105)), (mano_imagenes_banca[1], (950, 105)), (mano_imagenes_banca[2], (1080, 105))]
    ventana.blits(bs_imagenes_carta_volteadas)
    texto_puntuacion_jugador = fuente_mediana.render("Puntuacion: ", 50, blanco)
    texto_puntuacion_banca = fuente_mediana.render("Puntuacion: ", 50, blanco)
    texto_numeros_ptos_jugador = fuente_mediana.render(puntaje_jugador, 50, blanco)
    texto_numeros_ptos_banca = fuente_mediana.render(puntaje_banca, 50, blanco)
    textos_y_numeros_puntuacion = [(texto_puntuacion_jugador,(280, 390)), (texto_puntuacion_banca, (830, 390)), (texto_numeros_ptos_jugador, (360, 445)), (texto_numeros_ptos_banca, (910, 445))]
    ventana.blits(textos_y_numeros_puntuacion)
    renderizar_texto_jugador_mesa(ventana, fuente_grande, 280, 330, 850, 330)

def pantalla_para_victoria(ventana, imagen_mesa):
    ventana.blit(imagen_mesa, [0, 0])
    texto_saldo_ganado = fuente_pequeña.render("Saldo Ganado", 50, blanco)
    texto_saldo_apostado = fuente_pequeña.render("Saldo Apostado", 50, blanco)
    texto_mano_ganadora = fuente_mediana.render("Mano Ganadora", 50, blanco)
    blit_sequence_texto = [(texto_saldo_ganado, (150, 360)), (texto_saldo_apostado, (410, 360)), (texto_mano_ganadora, (865, 360))]
    ventana.blits(blit_sequence_texto)
    renderizar_texto_ganador_mesa(ventana, fuente_mas_grande)

def pantalla_para_mostrar_derrota(ventana, imagen_mesa):
    ventana.blit(imagen_mesa, [0, 0])
    texto_saldo_perdido = fuente_pequeña.render("Saldo Perdido", 50, blanco)
    texto_saldo_apostado = fuente_pequeña.render("Saldo Apostado", 50, blanco)
    texto_mano_perdedora = fuente_mediana.render("Mano Perdedora", 50, blanco)
    blit_sequence_texto = [(texto_saldo_perdido, (150, 360)), (texto_saldo_apostado, (410, 360)), (texto_mano_perdedora, (865, 360))]
    ventana.blits(blit_sequence_texto)
    renderizar_texto_perdedor_mesa(ventana, fuente_mas_grande)

def pantalla_para_mostrar_empate(ventana, imagen_mesa):
    ventana.blit(imagen_mesa, [0, 0])
    texto_mensaje_empate = fuente_grande.render("Ni Ganas, Ni Pierdes", 50, blanco)
    ventana.blit(texto_mensaje_empate, (430, 460))
    renderizar_texto_empate_mesa(ventana, fuente_mas_grande)


def congelamiento_barajeo(tiempo_de_congelamiento):
    sleep(tiempo_de_congelamiento)
    return True