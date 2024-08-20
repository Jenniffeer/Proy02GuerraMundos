from Vehiculo import Vehiculo
import random

class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.tablero = []
        self.vehiculos = []
    
    def generarTablero(self, tamanio) -> None:
        for numFila in range(tamanio):
            fila = []
            for numColumna in range(tamanio):
                fila.append("-")
            self.tablero.append(fila)

    def generarVehiculos(self, cantVehiculos, tamanioTablero) -> None:
        # Generar los carros
        for numVehiculo in range(cantVehiculos):
            repetido = True
            while repetido:
                # Generar posición del vehículo
                x = random.randint(0, tamanioTablero - 1)
                y = random.randint(0, tamanioTablero - 1)
                posicion = (y, x)
                # Comprueba si el vehículo ya existe
                repetido = False
                for vehiculo in self.vehiculos:
                    if vehiculo.posicion == posicion:
                        repetido = True
                        break
            # Crear vehículo
            municiones = random.randint(20, 40)
            self.vehiculos.append(Vehiculo("Carro", posicion, municiones))
        
        # Generar los tanques
        for numVehiculo in range(2):
            repetido = True 
            while repetido:
                # Generar posición del vehículo
                x = random.randint(0, tamanioTablero - 1)
                y = random.randint(0, tamanioTablero - 1)
                posicion = (y, x)
                # Comprueba si el vehículo ya existe
                repetido = False
                for vehiculo in self.vehiculos:
                    if vehiculo.posicion == posicion:
                        repetido = True
                        break
            # Crear vehículo
            municiones = random.randint(50, 70)
            self.vehiculos.append(Vehiculo("Tanque", posicion, municiones))
    
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
        print(" ", end=" ")
        for i in range(len(self.tablero)):
            print(i, end=" ")
        print("")
        for i, f in enumerate(self.tablero):
            print(i, end=" ")
            for c in f:
                print(c, end=" ")
            print()
    
    def imprimirVehiculos(self):
        print("-----------------------------")
        for vehiculo in self.vehiculos:
            print(f"{vehiculo.tipo.upper()} {vehiculo.posicion}: Munición {vehiculo.municion} Vivo {vehiculo.vivo}")
        print("-----------------------------")