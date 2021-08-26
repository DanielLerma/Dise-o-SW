class Avion:
    
    def __init__(self, velocidad, altitud, roll, pitch, yaw) -> None:
        ''' Abstraer el objeto avión en una clase simple con pasajeros '''
        self.velocidad = velocidad
        self.altitud = altitud
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self._pasajeros = 0
    
    def establecer_pasajeros(self, numPasajeros: int) -> None:
        ''' Modifica el valor del atributo privado _pasajeros '''
        self._pasajeros = numPasajeros

    def volar(self) -> str:
        ''' Mostrar información del avión cuando está volando '''
        return f'Se está volando a {self.altitud} metros de altitud y {self.velocidad} km/h y con {self._pasajeros} pasajeros'

    # propiedad de lectura
    @property
    def pasajeros(self) -> None:
        ''' Leemos el valor del atributo privado _pasajeros '''
        return self._pasajeros

    @pasajeros.setter
    def pasajeros(self, valor: int) -> None:
        ''' Modifica el valor del atributo privado _pasajeros '''
        if valor > 0 and valor <= 360:
            self._pasajeros = valor
        else:
            raise Exception('El número de pasajeros no es válido')

volaris747 = Avion(500, 2000, 0, 0, 0)
print(volaris747.volar())

volaris747.pasajeros = 380
print(volaris747.volar())