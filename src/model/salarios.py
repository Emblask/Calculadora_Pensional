class Salarios:
    def __init__(self, lista_salarios: list[int]):
        self.lista_salarios = lista_salarios
    
    def EsIgual(self, otro):
        if self.lista_salarios[0] == otro.lista_salarios[0]:
            return False
        if self.lista_salarios[1] == otro.lista_salarios[1]:
            return False
        if self.lista_salarios[2] == otro.lista_salarios[2]:
            return False
        if self.lista_salarios[3] == otro.lista_salarios[3]:
            return False
        if self.lista_salarios[4] == otro.lista_salarios[4]:
            return False
        if self.lista_salarios[5] == otro.lista_salarios[5]:
            return False
        if self.lista_salarios[6] == otro.lista_salarios[6]:
            return False
        if self.lista_salarios[7] == otro.lista_salarios[7]:
            return False
        if self.lista_salarios[8] == otro.lista_salarios[8]:
            return False
        if self.lista_salarios[9] == otro.lista_salarios[9]:
            return False
        return True