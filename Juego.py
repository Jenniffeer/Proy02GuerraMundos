from Jugador import Jugador
from time import sleep

class Juego:
    def __init__(self) -> None:
        self.tamanioTablero = 0 #Numero de filas y columnas
        self.numVehiculos = 0 #Numero de carros que se van a generar
        #Dos jugadores para el juego
        self.jugador1 = None 
        self.jugador2 = None
        #Atributos que cambian según la ronda
        self.jugadorActual = None
        self.jugadorEnemigo = None
        #Info de los turnos
        self.maximoTurnos = 100
        self.turnosJugados = 0
        #Atributo que permite retirarse del juego
        self.retirarse = False

    def configurarJuego(self, tamanioTablero, numVehiculos):
        # Configurar tamaño del tablero y número de vehículos
        self.tamanioTablero = tamanioTablero  
        self.numVehiculos = numVehiculos  

        # Crear y configurar Jugador 1
        nombre = input("Ingrese el nombre del jugador 1: ")
        self.jugador1 = Jugador(nombre)
        self.jugador1.generarTablero(self.tamanioTablero)
        self.jugador1.generarVehiculos(self.numVehiculos, self.tamanioTablero)

        # Crear y configurar Jugador 2
        nombre = input("Ingrese el nombre del jugador 2: ")
        self.jugador2 = Jugador(nombre)
        self.jugador2.generarTablero(self.tamanioTablero)
        self.jugador2.generarVehiculos(self.numVehiculos, self.tamanioTablero)

        #Jugadores para el primer turno
        self.jugadorActual = self.jugador1
        self.jugadorEnemigo = self.jugador2

    def empezarJuego(self):
        print("Principio del juego...")
        sleep(1)
        #Bucle que se encarga de jugar todos los turnos hasta que se alcanze el máximo o alguien gane
        while self.turnosJugados < self.maximoTurnos:
            #Jugar turno
            print("-----------------------------")
            print(f"Turno {self.jugadorActual.nombre}")
            print("Tablero enemigo: ")
            self.jugadorEnemigo.imprimirTablero()
            print("-----------------------------")
            sleep(1)
            # Menú de acciones
            while True:
                print("1) Atacar")
                print("2) Ver estadísticas")
                print("3) Rendirse")
                sleep(1)
                opc = input("Seleccione la opción: ").strip() #Quitar los espacios al inicio y al final

                if opc == "1":
                    self.atacar()
                    break
                elif opc=="2":
                    self.verEstadisticas()
                elif opc=="3":
                    self.retirarse = True
                    break
                else: 
                    print("Opción incorrecta, intente de nuevo.")

            #Comprobar victoria
            self.turnosJugados += 1
            if self.verificarCondicionesVictoria():
                print("Fin del juego...")
                sleep(1)
                return

            #Cambiar de turno
            if self.jugadorActual == self.jugador1:
                self.jugadorActual = self.jugador2
                self.jugadorEnemigo = self.jugador1
            else:
                self.jugadorActual = self.jugador1
                self.jugadorEnemigo = self.jugador2


    def atacar(self):
        #Pedir las coordenadas de ataque
        while True:
            fila = int(input("Ingrese el número de fila de su ataque: "))
            col = int(input("Ingrese el número de columna Y de su ataque: "))
            posicion = (fila, col)

            #Acá comprobamos que no haya ninguna coordenada fuera del rango
            if not (fila in range(0, self.tamanioTablero) and col in range(0, self.tamanioTablero)):
                print("Alguno de los valores está fuera del rango de ataque.")
                print()
            else:
                break
        
        #Marcar Tablero
        self.jugadorEnemigo.tablero[fila][col] = "*"
        #Destruir vehiculo
        for vehiculo in self.jugadorEnemigo.vehiculos:
            if vehiculo.posicion == posicion:
                vehiculo.destruirVehiculo()
                print(f"{vehiculo.tipo} destruido.")
                sleep(1)
                return
        print(f"Fallo el tiro.")
        sleep(1)

    #Verifica si se cumple alguna de las condiciones para que uno de los jugadores gane
    def verificarCondicionesVictoria(self):
        #Comprobamos si alguien se retiro
        if self.retirarse:
            print(f"¡Jugador {self.jugadorEnemigo.nombre} gana por retiro!")
            self.finalizarJuego()
            return True

        #Comprobamos si alguno de los jugadores se quedo sin vehículos
        if self.jugadorEnemigo.contarVehiculosVivos() == 0:
            print(f"¡{self.jugadorActual.nombre} gana!")
            self.finalizarJuego()
            return True

        # Verificar condiciones de municiones
        if self.jugadorEnemigo.contarMunicionesDisponibles() == 0:
            print(f"¡{self.jugadorActual.nombre} gana por falta de municiones!")
            self.finalizarJuego()
            return True

        # Verificar si un bando tiene más del 70% de municiones que el otro
        if self.jugadorActual.contarMunicionesDisponibles() > self.jugadorEnemigo.contarMunicionesDisponibles() * 1.7:
            print(f"¡{self.jugadorActual.nombre} gana porque tiene más del 70% de municiones que el jugador enemigo!")
            self.finalizarJuego()
            return True

        # Verificar si un bando tiene más del 80% más vehículos que el otro
        if self.jugadorActual.contarVehiculosVivos() > self.jugadorEnemigo.contarVehiculosVivos() * 1.8:
            print(f"¡{self.jugadorActual.nombre} gana porque tiene más del 80% de vehículos que el jugador enemigo!")
            self.finalizarJuego()
            return True

        return False

    def finalizarJuego(self):
        print("Fin del juego...")
        sleep(1)
        self.mostrarEstadisticasFinales()
    
    #Muestra las estadísticas al finalizar la partida
    def mostrarEstadisticasFinales(self):
        print("\nEstadísticas Finales del Juego:")
        print("-----------------------------")
        
        print(f"Jugador 1: {self.jugador1.nombre}")
        print(f"Vehículos generados: {len(self.jugador1.vehiculos)}")
        vehiculos_destruidos_j1 = len([v for v in self.jugador1.vehiculos if not v.vivo])
        print(f"Vehículos derribados: {vehiculos_destruidos_j1}")
        print(f"Municiones restantes: {self.jugador1.contarMunicionesDisponibles()}")
        print()

        print(f"Jugador 2: {self.jugador2.nombre}")
        print(f"Vehículos generados: {len(self.jugador2.vehiculos)}")
        vehiculos_destruidos_j2 = len([v for v in self.jugador2.vehiculos if not v.vivo])
        print(f"Vehículos derribados: {vehiculos_destruidos_j2}")
        print(f"Municiones restantes: {self.jugador2.contarMunicionesDisponibles()}")
        print("-----------------------------")
        sleep(2)

    def verEstadisticas(self):
        print("\nEstadísticas del Juego:")
        print(f"Vehículos generados y activos en el tablero:")
        print(f"{self.jugador1.nombre}: {self.jugador1.contarVehiculosVivos()} vehículos")
        print(f"{self.jugador2.nombre}: {self.jugador2.contarVehiculosVivos()} vehículos")
        print(f"\nMuniciones restantes:")
        print(f"{self.jugador1.nombre}: {self.jugador1.contarMunicionesDisponibles()} municiones")
        print(f"{self.jugador2.nombre}: {self.jugador2.contarMunicionesDisponibles()} municiones")