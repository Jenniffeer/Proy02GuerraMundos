from Vehiculo import Vehiculo
import random

class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.tablero = []
        self.vehiculos = []
    
    #Se encarga de generar todas las casillas del tablero
    def generarTablero(self, tamanio) -> None:
        for numFila in range(tamanio):
            fila = []
            for numColumna in range(tamanio):
                fila.append("-")
            self.tablero.append(fila)

    #Función que genera todos los vehículos
    def generarVehiculos(self, cantVehiculos, tamanioTablero) -> None:
        def generarVehiculo(tipo, minMuniciones, maxMuniciones, cantidad=1):
            for _ in range(cantidad):
                #Evitar que hayan dos vehículos en la misma posicion
                repetido = True
                while repetido:
                    # Generar posición del vehículo
                    x = random.randint(0, tamanioTablero - 1)
                    y = random.randint(0, tamanioTablero - 1)
                    posicion = (y, x)
                    # Comprueba si el vehículo ya existe
                    repetido = any(vehiculo.posicion == posicion for vehiculo in self.vehiculos) #Si alguno de los vehículos tiene la misma posicion será True sino false
                # Crear vehículo
                municiones = random.randint(minMuniciones, maxMuniciones)
                self.vehiculos.append(Vehiculo(tipo, posicion, municiones))

        # Generar vehículos
        generarVehiculo("Carro", 20, 40, cantVehiculos)
        generarVehiculo("Tanque", 50, 70, 2)
        generarVehiculo("Submarino", 30, 50, 1)
        generarVehiculo("Avión", 40, 60, 1)
        generarVehiculo("Avioneta", 10, 30, 1)

    def contarVehiculosVivos(self):
        total = 0 
        for vehiculo in self.vehiculos:
            if vehiculo.vivo:
                total += 1
        return total
    
    def contarMunicionesDisponibles(self):
        total = 0
        for vehiculo in self.vehiculos:
            if vehiculo.vivo:
                total += vehiculo.municion
        return total
    
    def imprimirTablero(self):
        #Espacio de la primera fila
        print(" ", end=" ")
        #Los números en la primera fila
        for i in range(len(self.tablero)):
            print(i, end=" ")
        print("") #Brincar de fila
        #Imprimir todas las filas del tablero
        for i, f in enumerate(self.tablero):
            print(i, end=" ") #Imprimir número de fila
            #Imprimir cada celda de la fila
            for c in f:
                print(c, end=" ")
            print()
    
    def imprimirVehiculos(self):
        print("-----------------------------")
        for vehiculo in self.vehiculos:
            print(f"{vehiculo.tipo.upper()} {vehiculo.posicion}: Munición {vehiculo.municion} Vivo {vehiculo.vivo}")
        print("-----------------------------")