import random # para las formas de las estrellas

# Dependencia
class Canal:
    def __init__(self, numero_de_canal: int) -> None:
        self.numero_de_canal = numero_de_canal
    
    def sintonizar(self) -> str:
        return f'Sintonizando el canal {self.numero_de_canal}'

class VideoCasetera:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def iniciar(self) -> None:
        pass

    def detener(self) -> None:
        pass
    
    def rebobinar(self) -> None:
        pass
    
    # argumento de otra clase: canal
    def reproducir(self, canal: Canal) -> None:
        return f'reproduciendo... {canal.sintonizar()}'

# Dependencia

# Asociación

class Empresa:
    def __init__(self, nombre: str, enfoque: str) -> None:
        self.nombre = nombre
        self.enfoque = enfoque

    def __str__(self) -> str:
        return self.nombre

class Persona:
    def __init__(self, nombre: str, empresa: Empresa) -> None:
        self.nombre = nombre
        self.empresa = empresa

    def __str__(self) -> str:
        return f'{self.nombre} trabaja en una empresa de {self.empresa.enfoque} llamada {self.empresa}'

intel = Empresa('Intel', 'Tecnología')
victor = Persona('Víctor', intel)
print(victor)

# Asociación

# Agregación


class Arma:
    def __init__(self, nombre: str, resistencia: int, destruccion: int) -> None:
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
    
    def __str__(self) -> str:
        return self.nombre


class Superheroe:
    def __init__(self, nombre: str, ataque: str, arma: Arma) -> None:
        self.nombre = nombre
        self.ataque = ataque
        self.arma = arma
        self.salud = 100

    def __str__(self) -> str:
        return self.nombre

    def atacar(self, otro):
        otro.salud -= self.ataque + self.arma.destruccion
        self.arma.resistencia -= 1

martillo = Arma('Martillo', 10, 6)
arco = Arma('Arco', 7, 3)

thor = Superheroe('Thor', 20, martillo)
ojo_de_halcon = Superheroe('Ojo de Halcpon', 18, arco)

print('Salud de ojo de halcón', ojo_de_halcon.salud)
thor.atacar(ojo_de_halcon)
print('Salud de ojo de halcón', ojo_de_halcon.salud)
print('Resistencia del martillo', martillo.resistencia)

del thor # borramos a Thor pero el martillo sigue existiendo

# Agregación

# Composición

class Estrella:
    def __init__(self) -> None:
        self.forma = random.choice(['*', '.', '*']) # random de formas de estrella

    def __str__(self) -> str:
        return self.forma

    def __del__(self) -> None:
        print('Eliminando estrellas')

class Cielo:
    def __init__(self, numero_de_estrellas: int) -> None:
        self.estrellas = []
        for i in range(numero_de_estrellas):
            estrella = Estrella()
            self.estrellas.append(estrella)

    def mostrar_estrellas(self) -> str:
        for i in self.estrellas:
            print(i)

cielo1 = Cielo(5)
cielo1.mostrar_estrellas()

del cielo1

# Composición