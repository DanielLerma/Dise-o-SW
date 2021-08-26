from abc import ABC, abstractmethod

# Clase Base
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self) -> str:
        ''' Método abstracto para retornar un sonido en str '''
        # método abstracto no tiene comportamiento por defecto
        pass

class Gato(Animal):
    
    def hacer_sonido(self) -> str:
        ''' Método abstracto para retornar un sonido en str '''
        return 'Meow'

class Perro(Animal):
    
    def hacer_sonido(self) -> str:
        ''' Método abstracto para retornar un sonido en str '''
        return 'Woof'

tom = Gato()
benji = Perro()
bolsa = [tom, benji, Gato()]

for animal in bolsa:
    print(animal.hacer_sonido())