class Salarios:
    def __init__(self,cedula: int,  salario_1 : int, salario_2 : int, salario_3 : int, salario_4 : int, salario_5 : int, salario_6 : int, salario_7 : int, salario_8 : int, salario_9 : int, salario_10 : int):
        self.cedula = cedula
        self.salario_1 = salario_1
        self.salario_2 = salario_2
        self.salario_3 = salario_3
        self.salario_4 = salario_4
        self.salario_5 = salario_5
        self.salario_6 = salario_6
        self.salario_7 = salario_7
        self.salario_8 = salario_8
        self.salario_9 = salario_9
        self.salario_10 = salario_10
    
    def EsIgual(self, otro):
        if self.cedula != otro.cedula:
            return False
        if self.salario_1 != otro.salario_1:
            return False
        if self.salario_2 != otro.salario_2:
            return False
        if self.salario_3 != otro.salario_3:
            return False
        if self.salario_4 != otro.salario_4:
            return False
        if self.salario_5 != otro.salario_5:
            return False
        if self.salario_6 != otro.salario_6:
            return False
        if self.salario_7 != otro.salario_7:
            return False
        if self.salario_8 != otro.salario_8:
            return False
        if self.salario_9 != otro.salario_9:
            return False
        if self.salario_10 != otro.salario_10:
            return False

        return True