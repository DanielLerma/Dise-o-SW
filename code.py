class Gato:

    # Variables de clase
    color = 'blanco'    

    # Constructor
    # El primer arg. de cualquier constructor: referencia a la instancia
    def __init__(self, nombre, edad, peso, color):
        ''' Definiendo parámetros iniciales de un gatito (: '''
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color

    # Metodo para darle print a mi gatito (:
    def detalles(self) -> str:
        ''' Retorno los detalles de mi gatito '''
        return f'{self.nombre} es un gato de {self.edad} años, de color {self.color} que pesa {self.peso} kilos'

    # Decoradores
    @classmethod
    def changeColor(cls, color):
        ''' Valida que el color del gatito sea correcto '''
        if color in ['blanco', 'negro', 'gris']:
            cls.color = color
        else:
            print('Error. El color no es valido')
    
    @staticmethod
    def horaDeJugar(HH24:int) -> bool:
        ''' Regresa True si es hora de jugar '''
        if HH24 >= 8 and HH24 <= 20:
            return True
        else:
            return False


# Para crear un gato se hacen instancias
tom = Gato('Tom', 3, 5, 'cafe')
print(tom.detalles())

michi = Gato('Michi', 9, 6.2, 'negro')
