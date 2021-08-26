class Animal:

    # Variables de clase
    color = 'blanco'    

    # Constructor
    # El primer arg. de cualquier constructor: referencia a la instancia
    def __init__(self, nombre, edad, peso, tipo):
        ''' Definiendo parámetros iniciales de un animalito (: '''
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.tipo = tipo

    # Metodo para darle print a mi gatito (:
    def detalles(self) -> str:
        ''' Retorno los detalles de mi animalito '''
        return f'{self.nombre} es un {self.tipo} de {self.edad} años, de color {self.color} que pesa {self.peso} kilos'

    # Decoradores
    @classmethod
    def changeColor(cls, color):
        ''' Valida que el color del animalito sea correcto '''
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

# Herencia
class Gato(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso, 'gato')

class Perro(Animal):
    def __init__(self, nombre, edad, peso):
        super().__init__(nombre, edad, peso, 'perro')


# Para crear un gato se hacen instancias
tom = Gato('Tom', 3, 5)
print(tom.detalles())

michi = Gato('Michi', 9, 6.2)
print(michi.detalles())

benji = Perro('Benajamin', 2, 2.3)
print(benji.detalles())
