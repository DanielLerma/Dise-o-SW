from abc import ABC

# Interfaz
class TransporteAereo(ABC):
    def __init__(self, origen: str, destino: str, pasajeros: int) -> None:
        ''' Constructor de la interfaz '''
        self.origen = origen
        self.destino = destino
        self.pasajeros = pasajeros

    def volar(self) -> str:
        return f'volando de {self.origen} a {self.destino} con {self.pasajeros} pasajeros'

class Helicoptero(TransporteAereo):
    def volar(self) -> str:
        return f'{super().volar()} en un helicóptero'

class Avion(TransporteAereo):
    def volar(self) -> str:
        return f'{super().volar()} en un avión'

### -----------------------------------------------
# Codigo del cliente que trabajará con la interfaz

class Aeropuerto:
    def aceptar(self, transporte_aereo: TransporteAereo):
        ''' Retornar True si el objeto corresponde a el tipo TransporteAereo '''
        return isinstance(transporte_aereo, TransporteAereo)

transporte = Avion('GDL', 'PV', 150)
print(transporte.volar())

benito_juarez = Aeropuerto()
print(benito_juarez.aceptar(transporte))