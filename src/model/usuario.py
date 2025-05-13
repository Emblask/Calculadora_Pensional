class Usuario:
    def __init__(self, cedula: int, nombre: str, apellido: str, edad: int, genero: str):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def EsIgual(self, otro):

        if self.cedula != otro.cedula:
            return False
        if self.nombre != otro.nombre:
            return False
        if self.apellido != otro.apellido:
            return False
        if self.edad != otro.edad:
            return False
        if self.genero != otro.genero:
            return False
        return True