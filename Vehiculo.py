class Vehiculo:
    def __init__(self, tipo, posicion, municion) -> None:
        self.tipo = tipo
        self.posicion = posicion
        self.municion = municion
        self.vivo = True
    
    def destruirVehiculo(self) -> bool:
        if self.vivo:
            self.vivo = False
            return True
        else:
            return False