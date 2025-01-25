import random
import pygame as pg

pg.init()
# Clase Carta con sus atributos

imagen_carta_as = pg.image.load("Recuros/Acrz").convert()
imagen_carta_2 = pg.image.load("Recuros/2crz").convert()
imagen_carta_3 = pg.image.load("Recuros/3crz").convert()
imagen_carta_4 = pg.image.load("Recuros/4crz").convert()
imagen_carta_5 = pg.image.load("Recuros/5dmt").convert()
imagen_carta_6 = pg.image.load("Recuros/6dmt").convert()
imagen_carta_7 = pg.image.load("Recuros/7dmt").convert()
imagen_carta_8 = pg.image.load("Recuros/8pcz").convert()
imagen_carta_9 = pg.image.load("Recuros/9pcz").convert()
imagen_carta_10 = pg.image.load("Recuros/10pcz").convert()
imagen_carta_J = pg.image.load("Recuros/Jtrb").convert()
imagen_carta_Q = pg.image.load("Recuros/Qtrb").convert()
imagen_carta_K = pg.image.load("Recuros/Ktrb").convert()


# Clase Baraja: Contiene todas las cartas que posee una baraja
class Baraja:
    def __init__(self):
        carta_contenido = {"A": [1, imagen_carta_as], "2": [2, imagen_carta_2], "3": [3, imagen_carta_3], "4": [4, imagen_carta_4], "5": [5, imagen_carta_5], "6": [6, imagen_carta_6], "7": [7, imagen_carta_8], "8": [8, imagen_carta_8], "9": [9, imagen_carta_9], "10": [0, imagen_carta_10], "J": [0, imagen_carta_J], "Q": [0, imagen_carta_Q], "K": [0, imagen_carta_K]}
        self.baraja = []
        for elemento in carta_contenido.items():
            for letra, contenido in elemento:
                for valor, imagen in contenido:
                    carta = Carta(letra, imagen, valor)
                    self.baraja.append(carta)

    def barajar(self):
        nCartas = len(self.baraja)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.baraja[i], self.baraja[j] = self.baraja[j], self.baraja[i]

def calcular_mano(mano):
    valor = sum(carta.valor_numerico for carta in mano)
    return valor % 10

def mostrar_cartas(jugador, banca):
    # Mostrando cartas
    jugadores = [banca, jugador]
    nom_jugadores = ["Banca", "Jugador"]
    for i in range(2):
        print("{}: ".format(nom_jugadores[i]))
        for carta in jugadores[i]:
            print(carta, end=" ")
        print()
    print()

def recibir_tercera_carta_jugador(mano_jugador, baraja):
    valor_jugador = calcular_mano(mano_jugador)
    if valor_jugador <= 5:
        carta = baraja.baraja.pop(0)
        mano_jugador.append(carta)
        return carta
    return None

def recibir_tercera_carta_banca(mano_banca, tercera_carta_jugador, baraja):
    valor_banca = calcular_mano(mano_banca)
    if valor_banca <= 2:
        carta = baraja.baraja.pop(0)
        mano_banca.append(carta)
        return carta
    elif valor_banca == 3 and (tercera_carta_jugador is None or tercera_carta_jugador.valor_numerico != 8):
        carta = baraja.baraja.pop(0)
        mano_banca.append(carta)
        return carta
    elif valor_banca == 4 and tercera_carta_jugador and 2 <= tercera_carta_jugador.valor_numerico <= 7:
        carta = baraja.baraja.pop(0)
        mano_banca.append(carta)
        return carta
    elif valor_banca == 5 and tercera_carta_jugador and 4 <= tercera_carta_jugador.valor_numerico <= 7:
        carta = baraja.baraja.pop(0)
        mano_banca.append(carta)
        return carta
    elif valor_banca == 6 and tercera_carta_jugador and tercera_carta_jugador.valor_numerico in [6, 7]:
        carta = baraja.baraja.pop(0)
        mano_banca.append(carta)
        return carta
    return None

def determinar_ganador(valor_jugador, valor_banca, apuesta, total_apuesta, saldo):
    if valor_jugador > valor_banca:
        if apuesta == "jugador":
            saldo += 2 * total_apuesta
            print("El ganador es el jugador. Ganas el doble de tu apuesta!\n")
        else:
            saldo -= total_apuesta
            print("El ganador es el jugador. Pierdes tu apuesta.\n")
    elif valor_banca > valor_jugador:
        if apuesta == "banca":
            saldo += 2 * total_apuesta
            print("El ganador es la banca. Ganas el doble de tu apuesta!\n")
        else:
            saldo -= total_apuesta
            print("El ganador es la banca. Pierdes tu apuesta.\n")
    else:
        saldo += total_apuesta  # Recupera la apuesta en caso de empate
        print("El juego quedó en empate. Recuperas tu apuesta.\n")
    return saldo

# Crear y barajar el mazo 
baraja = Baraja()
baraja.barajar()
# Mostrar las cartas restantes en el mazo
# baraja.mostrar_baraja()

# Permitir al usuario definir el saldo inicial
saldo = int(input("Ingrese su saldo inicial: "))
print(f"Tu saldo inicial es: {saldo}")

while saldo > 0:
    # Apuesta del jugador
    apuesta = input("¿Apostar al jugador o a la banca? (jugador/banca): ").strip().lower()
    total_apuesta = int(input("¿Cuánto deseas apostar? "))

    if total_apuesta > saldo:
        print("No tienes suficientes fichas para hacer esa apuesta.")
        continue
    elif saldo <= 0:
        print("Te has quedado sin saldo. El juego ha terminado.")
        break

    # Repartiendo cartas
    banca = []
    jugador = []

    for i in range(2):
        carta1 = baraja.baraja.pop(0)
        jugador.append(carta1)
        carta2 = baraja.baraja.pop(0)
        banca.append(carta2)

    mostrar_cartas(jugador, banca)

    # Calculando valores de las manos:
    valor_jugador = calcular_mano(jugador)
    valor_banca = calcular_mano(banca)

    # Determinando si el jugador recibe una tercera carta
    tercera_carta_jugador = recibir_tercera_carta_jugador(jugador, baraja)

    # Determinando si la banca recibe una tercera carta
    recibir_tercera_carta_banca(banca, tercera_carta_jugador, baraja)

    # Recalculando el valor de la mano del jugador y de la banca después de la tercera carta
    valor_jugador = calcular_mano(jugador)
    valor_banca = calcular_mano(banca)

    # Mostrar nuevamente las cartas de los jugadores
    mostrar_cartas(jugador, banca)

    # Mostrando el valor de las manos
    print("El valor de la mano del Jugador es: ", valor_jugador)
    print("El valor de la mano de la Banca es: ", valor_banca)

    # Determinando el ganador y actualizando el saldo
    saldo = determinar_ganador(valor_jugador, valor_banca, apuesta, total_apuesta, saldo)
    print(f"Tu saldo después del juego es: {saldo}")

