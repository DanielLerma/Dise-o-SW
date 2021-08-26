from abc import ABC

class Animal:
    def __init__(self) -> None:
        pass
        
class CuatroPatas(ABC):
    def __init__(self) -> None:
        pass

    def correr(self):
        return 'corriendo'

class Respirador(ABC):
    def __init__(self) -> None:
        pass

    def respirar(self):
        return 'respirando'

# ---------------------------------------------
# Herencia múltiple
class Gato(Animal, CuatroPatas, Respirador):
    def __del__(self):
        ''' Dunder method usado cuando python libera el recurso '''
        print('El gatito murió')

tom = Gato()
print(tom.respirar())
print(tom.correr())