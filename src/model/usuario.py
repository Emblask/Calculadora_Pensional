class Usuario:
    def __init__(self, cedula: int, nombre: str, apellido: str, edad: int, genero: str):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def EsIgual(self, otro):
        assert(self.cedula == otro.cedula)
        assert(self.nombre == otro.nombre)
        assert(self.apellido == otro.apellido)
        assert(self.edad == otro.edad)
        assert(self.genero == otro.genero)
        return True