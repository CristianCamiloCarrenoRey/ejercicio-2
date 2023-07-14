import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
        self.cartas = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def calcular_puntuacion(self):
        puntuacion = 0
        tiene_as = False

        for carta in self.mano:
            if carta.valor in ['Jota', 'Reina', 'Rey']:
                puntuacion += 10
            elif carta.valor == 'As':
                tiene_as = True
            else:
                puntuacion += int(carta.valor)

        if tiene_as and puntuacion <= 11:
            puntuacion += 10

        return puntuacion

class Blackjack:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.mazo = Mazo()

    def repartir_cartas_iniciales(self):
        for _ in range(2):
            for jugador in self.jugadores:
                carta = self.mazo.repartir_carta()
                jugador.recibir_carta(carta)

    def jugar_turno(self, jugador):
        while True:
            opcion = input(f"{jugador.nombre}, ¿quieres pedir otra carta? (s/n): ")

            if opcion.lower() == 's':
                carta = self.mazo.repartir_carta()
                jugador.recibir_carta(carta)
                puntuacion = jugador.calcular_puntuacion()

                print(f"Has recibido la carta: {carta}")
                print(f"Tu puntuación actual es: {puntuacion}")

                if puntuacion > 21:
                    print("¡Te has pasado de 21! Pierdes.")
                    return

            elif opcion.lower() == 'n':
                break

    def determinar_ganador(self):
        puntuaciones = {jugador.nombre: jugador.calcular_puntuacion() for jugador in self.jugadores}
        max_puntuacion = max(puntuaciones.values())

        ganadores = [jugador for jugador, puntuacion in puntuaciones.items() if puntuacion == max_puntuacion]

        if len(ganadores) == 1:
            print(f"{ganadores[0]} gana con {max_puntuacion} puntos.")
        else:
            print("¡Es un empate!")

# Crear jugadores
jugador1 = Jugador("Jugador 1")
jugador2 = Jugador("Jugador 2")

# Crear juego de Blackjack
blackjack = Blackjack([jugador1, jugador2])

# Repartir cartas iniciales
blackjack.repartir_cartas_iniciales()

# Turno del jugador 1
blackjack.jugar_turno(jugador1)

# Turno del jugador 2
blackjack.jugar_turno(jugador2)

# Determinar ganador
blackjack.determinar_ganador()
