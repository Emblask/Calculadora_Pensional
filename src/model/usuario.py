class Usuario:
    def __init__(self, cedula: int, nombre: str, apellido: str, edad: int, genero: str, numero_hijos: int):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.numero_hijos = numero_hijos

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
        if self.numero_hijos != otro.numero_hijos:
            return False
        return True