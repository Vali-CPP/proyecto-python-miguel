from math import e
import pygame as pg
import Funciones as func
from time import sleep
from random import randint

pg.init()
class Boton:
    def __init__(self, fuente, posicion_x, posicion_y, tamaño_x, tamaño_y, mensaje_texto, mensaje_color):
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.fuente = fuente
        self.tamaño_x = tamaño_x
        self.tamaño_y = tamaño_y
        self.mensaje_texto = mensaje_texto
        self.mensaje_color = mensaje_color

    def Crear_superficie(self):
        self.boton = pg.Rect(self.posicion_x, self.posicion_y, self.tamaño_x, self.tamaño_y)
        self.mensaje = self.fuente.render(str(self.mensaje_texto), True, tuple(self.mensaje_color))
    
    def Dibujar_boton(self, ventana_de_aparicion, boton_color, boton):
        pg.draw.rect(ventana_de_aparicion, boton_color, boton)
    
    def actualizar_mensaje(self, fuente, mensaje_actualizado, mensaje_actualizado_color = (255, 255, 255)):
        self.mensaje_texto  = mensaje_actualizado
        self.mensaje_color = mensaje_actualizado_color
        self.mensaje = fuente.render(str(mensaje_actualizado), True, tuple(mensaje_actualizado_color))
        return mensaje_actualizado

class Carta:
    def __init__(self, caracter, valor_numerico, imagen_carta):
        self.caracter = caracter 
        self.imagen = imagen_carta
        self.valor_numerico = valor_numerico

class Baraja:
    def __init__(self):
        self.Baraja = []

    def agregar_carta(self, Carta):
        self.Baraja.append(Carta)

    def obtener_carta_random(self):
        carta_random = self.Baraja[randint(0,11)]
        return carta_random

class Mano:
    def __init__(self):
        self.cartas = list()

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def obtener_puntuacion(self):
        self.puntuacion = int()
        for i in self.cartas:
            self.puntuacion += i.valor_numerico
        
        if self.puntuacion >= 9:
            return 0
        
        return self.puntuacion

    def obtener_imagenes(self):
        return [self.cartas[0].imagen, self.cartas[1].imagen, self.cartas[2].imagen]
    
    def obtener_valores(self):
        return [self.cartas[0].caracter, self.cartas[1].caracter, self.cartas[2].caracter]

    def limpiar_mano(self):
        self.cartas = list()


#Creando ventana
ventana = pg.display.set_mode([1280, 720])
pg.display.set_caption("Baccarat")

#Carga de imagenes.
mesa = pg.image.load("Recursos/Mesa.jpg").convert()
baraja_carta_reverso_crudo = pg.image.load("Recursos/reverso_baraja_1.jpg").convert()
baraja_carta_reverso_ajustada = pg.transform.scale(baraja_carta_reverso_crudo, (100, 150))
menu = pg.image.load("Recursos/Menu.jpg").convert()
imagen_carta_as = pg.image.load("Recursos/Cartas_a_utilizar/Acrz.PNG").convert()
imagen_carta_2 = pg.image.load("Recursos/Cartas_a_utilizar/2crz.PNG").convert()
imagen_carta_3 = pg.image.load("Recursos/Cartas_a_utilizar/3crz.PNG").convert()
imagen_carta_4 = pg.image.load("Recursos/Cartas_a_utilizar/4crz.PNG").convert()
imagen_carta_5 = pg.image.load("Recursos/Cartas_a_utilizar/5dmt.PNG").convert()
imagen_carta_6 = pg.image.load("Recursos/Cartas_a_utilizar/6dmt.PNG").convert()
imagen_carta_7 = pg.image.load("Recursos/Cartas_a_utilizar/7dmt.PNG").convert()
imagen_carta_8 = pg.image.load("Recursos/Cartas_a_utilizar/8pcz.PNG").convert()
imagen_carta_9 = pg.image.load("Recursos/Cartas_a_utilizar/9pcz.PNG").convert()
imagen_carta_10 = pg.image.load("Recursos/Cartas_a_utilizar/10pcz.PNG").convert()
imagen_carta_J = pg.image.load("Recursos/Cartas_a_utilizar/Jtrb.PNG").convert()
imagen_carta_Q = pg.image.load("Recursos/Cartas_a_utilizar/Qtrb.PNG").convert()
imagen_carta_K = pg.image.load("Recursos/Cartas_a_utilizar/Ktrb.PNG").convert()
imagen_carta_as = pg.transform.scale(imagen_carta_as, (100, 150))
imagen_carta_2 = pg.transform.scale(imagen_carta_2, (100, 150))
imagen_carta_3 = pg.transform.scale(imagen_carta_3, (100, 150))
imagen_carta_4 = pg.transform.scale(imagen_carta_4, (100, 150))
imagen_carta_5 = pg.transform.scale(imagen_carta_5, (100, 150))
imagen_carta_6 = pg.transform.scale(imagen_carta_6, (100, 150))
imagen_carta_7 = pg.transform.scale(imagen_carta_7, (100, 150))
imagen_carta_8 = pg.transform.scale(imagen_carta_8, (100, 150))
imagen_carta_9 = pg.transform.scale(imagen_carta_9, (100, 150))
imagen_carta_10 = pg.transform.scale(imagen_carta_10, (100, 150))
imagen_carta_J = pg.transform.scale(imagen_carta_J, (100, 150))
imagen_carta_Q = pg.transform.scale(imagen_carta_Q, (100, 150))
imagen_carta_K = pg.transform.scale(imagen_carta_K, (100, 150))

#Variables varias
fuente_pequeña = pg.font.Font(None, 35)
fuente_grande = pg.font.Font(None, 75)
juego_iniciado = False
estado_de_boton_ingresar = False
texto_ingresado = str() 
boton_ingrese_texto_contador = 0
saldo_del_jugador = 1000
saldo_del_jugador_texto = "Saldo: $" + str(saldo_del_jugador)
saldo_del_jugador_texto_grande = "$" + str(saldo_del_jugador)
saldo_apostado = 0
saldo_apostado_texto = "Saldo Apostado: $" + str(saldo_apostado)
game_loop = True
tiempo_congelado_aleatorio = randint(1, 7)
apuesta_eleccion_jugador = 0
verificar_eleccion_jugador = False
segunda_verificacion_eleccion_jugador = False
verificar_congelamiento_barajeo = False
apuesta_no_ingresada = 0
apuesta_en_proceso = 1 
apuesta_ingresada = 2
apuesta_invalida = 4
carta_contenido = [["A", 1, imagen_carta_as], ["2", 2, imagen_carta_2], ["3", 3, imagen_carta_3], ["4", 4, imagen_carta_4], ["5", 5, imagen_carta_5], ["6", 6, imagen_carta_6], ["7", 7, imagen_carta_8], ["8", 8, imagen_carta_8], ["9", 9, imagen_carta_9], ["10", 0, imagen_carta_10], ["J", 0, imagen_carta_J], ["Q", 0, imagen_carta_Q], ["K", 0, imagen_carta_K]]
mano_jugador = Mano() 
mano_banca = Mano()
manos = [mano_jugador, mano_banca]


#Creando las cartas, la baraja y las manos de cada jugador
baraja = Baraja()
for lista in carta_contenido:
    carta = Carta(lista[0], lista[1], lista[2])
    baraja.agregar_carta(carta)

for i in range(1, 4):
    mano_jugador.agregar_carta(baraja.obtener_carta_random())
    mano_banca.agregar_carta(baraja.obtener_carta_random())

puntos_jugador = str(mano_jugador.obtener_puntuacion())
puntos_banca = str(mano_banca.obtener_puntuacion())


#Colores para los cuadros y textos
blanco = (255, 255, 255)
rojo = (170, 0, 0)
azul = (0, 0, 170)
verde = (80, 135, 80)
negro = (0, 0, 0)
color_del_cuadro = verde

#Instanciando de botones
boton_comenzar = Boton(fuente_pequeña , 503, 508, 150, 50, "Comenzar", blanco)
boton_salir = Boton(fuente_pequeña , 503, 567, 150, 50, "Salir", blanco)
boton_regresar = Boton(fuente_pequeña , 1115, 3, 150, 50, "Regresar", blanco)
boton_ingrese_texto_inactivo = Boton(fuente_pequeña , 470, 390, 350, 70, "Escriba", negro)
boton_ingrese_texto_activo = Boton(fuente_pequeña , 470, 390, 350, 70, "", blanco)
boton_apuesta_jugador = Boton(fuente_pequeña, 406, 463, 239, 232, "Click", blanco)
boton_apuesta_banca = Boton(fuente_pequeña, 645, 463, 237, 232, "Click", blanco)


#Esto no es un boton, solamente se utiliza para mostrar el saldo actual y se usa la clase boton por conveniencia
texto_saldo_actual_esquina = Boton(fuente_pequeña, 40, 5, 150, 50, str(saldo_del_jugador_texto), blanco)
texto_saldo_actual_grande = Boton(fuente_grande, 560, 585, 150, 50, str(saldo_del_jugador_texto_grande), blanco)
texto_saldo_apostado_esquina = Boton(fuente_pequeña, 260, 5, 150, 50, str(saldo_apostado_texto), blanco)

#Creando la superficie sin dibujar de los botones
boton_comenzar.Crear_superficie()
boton_salir.Crear_superficie()
boton_regresar.Crear_superficie()
boton_apuesta_jugador.Crear_superficie()
boton_apuesta_banca.Crear_superficie()
boton_ingrese_texto_inactivo.Crear_superficie()
boton_ingrese_texto_activo.Crear_superficie()
texto_saldo_actual_esquina.Crear_superficie()
texto_saldo_apostado_esquina.Crear_superficie()
texto_saldo_actual_grande.Crear_superficie()


#Pre-Game loop

#Game Loop
while game_loop:

    if not juego_iniciado:
        func.pantalla_menu(ventana, menu, boton_comenzar, boton_salir)

    if juego_iniciado:
        if  boton_ingrese_texto_contador == apuesta_no_ingresada:
            func.pantalla_para_ingresar_apuesta(ventana, mesa, texto_saldo_actual_grande, baraja_carta_reverso_ajustada, boton_regresar, boton_ingrese_texto_inactivo, boton_ingrese_texto_activo, texto_ingresado_renderizado, desplazamiento_lateral_del_texto, fuente_pequeña )

        elif boton_ingrese_texto_contador == apuesta_en_proceso:
            func.pantalla_para_ingresar_apuesta(ventana, mesa, texto_saldo_actual_grande, baraja_carta_reverso_ajustada, boton_regresar, boton_ingrese_texto_inactivo, boton_ingrese_texto_activo, texto_ingresado_renderizado, desplazamiento_lateral_del_texto, fuente_pequeña , 1)

        elif boton_ingrese_texto_contador == apuesta_ingresada:
            if not verificar_congelamiento_barajeo:
                func.pantalla_para_barajeo(ventana, mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar)

                pg.display.flip()

                verificar_congelamiento_barajeo = func.congelamiento_barajeo(tiempo_congelado_aleatorio)

            if verificar_congelamiento_barajeo:

                if not verificar_eleccion_jugador:
                    pg.display.flip()
                    func.pantalla_para_elegir_apuesta(ventana, mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_apuesta_jugador, boton_apuesta_banca, boton_regresar)

                else:
                    func.pantalla_para_mostrar_cartas(ventana, mesa, texto_saldo_actual_esquina, texto_saldo_apostado_esquina, baraja_carta_reverso_ajustada, boton_regresar, mano_jugador.obtener_imagenes(), mano_banca.obtener_imagenes(), mano_jugador.obtener_puntuacion(), mano_banca.obtener_puntuacion())
    
                    pg.display.flip()
    
                    sleep(3)
                    
                    if (mano_jugador.obtener_puntuacion() > mano_banca.obtener_puntuacion() and apuesta_eleccion_jugador == 1) or (mano_jugador.obtener_puntuacion() < mano_banca.obtener_puntuacion() and apuesta_eleccion_jugador == 2): 
                        pg.display.flip()
                        func.pantalla_para_victoria(ventana, mesa)
                        pg.display.flip()
                        sleep(5)
                        boton_ingrese_texto_contador = 0
                        saldo_del_jugador += round((saldo_apostado * 1.5), 0)
                        texto_saldo_actual_grande.actualizar_mensaje(fuente_grande, "$" + str(saldo_del_jugador))
                        saldo_apostado_texto = "Saldo Apostado: $" + str(saldo_apostado)
                        texto_saldo_apostado_esquina.actualizar_mensaje(fuente_pequeña, saldo_apostado_texto)
                        saldo_apostado = 0
                        texto_ingresado = ""
                        verificar_congelamiento_barajeo = False
                        apuesta_eleccion_jugador = 0
                        verificar_eleccion_jugador = False
                        func.limpiar_y_barajear_mano(manos, baraja)
                    elif (mano_jugador.obtener_puntuacion() > mano_banca.obtener_puntuacion() and apuesta_eleccion_jugador == 2) or (mano_jugador.obtener_puntuacion() < mano_banca.obtener_puntuacion() and apuesta_eleccion_jugador == 1):
                        pg.display.flip()
                        func.pantalla_para_mostrar_derrota(ventana, mesa)
                        pg.display.flip()
                        sleep(3)
                        boton_ingrese_texto_contador = 0
                        saldo_apostado = 0
                        texto_ingresado = ""
                        verificar_congelamiento_barajeo = False
                        apuesta_eleccion_jugador = 0
                        verificar_eleccion_jugador = False
                        saldo_apostado_texto = "Saldo Apostado: $" + str(saldo_apostado)
                        texto_saldo_apostado_esquina.actualizar_mensaje(fuente_pequeña, saldo_apostado_texto)
                        func.limpiar_y_barajear_mano(manos, baraja)
                    elif mano_jugador.obtener_puntuacion() == mano_banca.obtener_puntuacion():
                        pg.display.flip()
                        func.pantalla_para_mostrar_empate(ventana, mesa)
                        pg.display.flip()
                        sleep(4)
                        boton_ingrese_texto_contador = 0
                        saldo_del_jugador += saldo_apostado 
                        saldo_apostado_texto = "Saldo Apostado: $" + str(saldo_apostado)
                        texto_saldo_apostado_esquina.actualizar_mensaje(fuente_pequeña, saldo_apostado_texto)
                        texto_saldo_actual_grande.actualizar_mensaje(fuente_grande, "$" + str(saldo_del_jugador))
                        saldo_apostado = 0
                        texto_ingresado = ""
                        verificar_congelamiento_barajeo = False
                        apuesta_eleccion_jugador = 0
                        verificar_eleccion_jugador = False
                        func.limpiar_y_barajear_mano(manos, baraja)


    #Inicio del bucle para capturar eventos, todos los eventos de la pantalla son gestionados dentro de este bucle
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_loop = False

        #Gestionando la accion de diferentes botones.
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

            if boton_comenzar.boton.collidepoint(pg.mouse.get_pos()):
                juego_iniciado = True

            elif boton_salir.boton.collidepoint(pg.mouse.get_pos()) and not juego_iniciado:
                game_loop = False
                boton_ingrese_texto_contador = 0

            elif boton_regresar.boton.collidepoint(pg.mouse.get_pos()):
                juego_iniciado = False
                boton_ingrese_texto_contador = 0
                saldo_apostado = 0
                saldo_del_jugador = 1000
                texto_ingresado = ""
                verificar_congelamiento_barajeo = False
                apuesta_eleccion_jugador = 0
                verificar_eleccion_jugador = False
                texto_saldo_actual_grande.actualizar_mensaje(fuente_grande, "$1000")
            
            #Gestionando la logica de los botones de apuesta.
            if verificar_congelamiento_barajeo:
                if not verificar_eleccion_jugador:
                    if boton_apuesta_banca.boton.collidepoint(pg.mouse.get_pos()):
                        apuesta_eleccion_jugador = 2
                        verificar_eleccion_jugador = True

                    elif boton_apuesta_jugador.boton.collidepoint(pg.mouse.get_pos()):
                        apuesta_eleccion_jugador = 1
                        verificar_eleccion_jugador = True

            #Gestionando la accion del boton Escriba
            if boton_ingrese_texto_inactivo.boton.collidepoint(pg.mouse.get_pos()) and juego_iniciado:  
                boton_ingrese_texto_contador += apuesta_en_proceso

        #Este bloque de codigo se encarga de manejar la logica del ingresado de texto durante la primera pantalla:
        if event.type == pg.KEYDOWN and boton_ingrese_texto_contador == apuesta_en_proceso:
            if event.key == pg.K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]
            elif (event.key == pg.K_RETURN or boton_ingrese_texto_contador == apuesta_ingresada):
                if texto_ingresado != "":
                    if int(texto_ingresado) > saldo_del_jugador or int(texto_ingresado) <= 0:
                        func.pantalla_para_monto_invalido(ventana, mesa, baraja_carta_reverso_ajustada, boton_regresar)
                        pg.display.flip()
                        sleep(2)
                        boton_ingrese_texto_contador = apuesta_no_ingresada
                        texto_ingresado = ""
                    else:
                        saldo_apostado += int(texto_ingresado)
                        saldo_del_jugador -= int(texto_ingresado)
                        saldo_del_jugador_texto = "Saldo: $" + str(saldo_del_jugador)
                        saldo_del_jugador_texto_grande = "$" + str(saldo_del_jugador)
                        saldo_apostado_texto = "Saldo Apostado: $" + str(saldo_apostado)
                        texto_saldo_actual_esquina.actualizar_mensaje(fuente_pequeña, saldo_del_jugador_texto)
                        texto_saldo_apostado_esquina.actualizar_mensaje(fuente_pequeña, saldo_apostado_texto)
                        texto_saldo_actual_grande.actualizar_mensaje(fuente_grande, saldo_del_jugador_texto_grande)
                        boton_ingrese_texto_contador += 1

            else:
                texto_ingresado += event.unicode

    desplazamiento_lateral_del_texto = 0
    texto_ingresado_renderizado = fuente_pequeña.render(texto_ingresado, True, negro)
    ancho_del_texto = texto_ingresado_renderizado.get_width()
    
    # Desplazamiento si el texto excede el ancho del cuadro
    if ancho_del_texto > boton_ingrese_texto_inactivo.boton.w - 10:
        desplazamiento_lateral_del_texto = ancho_del_texto - (boton_ingrese_texto_inactivo.boton.w - 10)
    else:
        desplazamiento_lateral_del_texto = 0

    #mouse_pos = pg.mouse.get_pos()
    #print(mouse_pos)

    pg.display.flip()

pg.quit()
