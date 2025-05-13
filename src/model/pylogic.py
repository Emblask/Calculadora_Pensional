Porcentaje_pension = 0.65
salario_minimo = 1423500
semanas_mujer = 1000

class NegativeNum(Exception):
    def __init__(self):
        super().__init__(f"Al parecer dijitaste un numero incorrecto, verifica los datos.")

class InvalidAgeError(Exception):
    def __init__(self, edad):
        super().__init__(f"""Edad inferior a la permitida para solicitar un fondo de pensiones. la {edad} es inferior a la establecida por el estado. Por favor ingrese una edad valida""")
    

class InvalidWeeksError(Exception):
    def __init__(self, semanas_requeridas, semanas_obtenidas):
        super().__init__(f"""Las semanas cotizadas son inferiores a las semanas minimas. Tienes {semanas_obtenidas} y necesitass {semanas_requeridas}. Por favor verifica tus semanas""")
    

class InvalidDatesError(Exception):
    """Las semanas cotizadas y la edad no son suficiente. Tienes menos semanas de las requeridas. Por favor completa los requisitos"""

def calculo_IBL(lista: list[int], idx = 0):
    if idx == len(lista):
        return 0
    
    if lista[idx] < 0:
        raise NegativeNum()
    
    
    return lista[idx] + calculo_IBL(lista, idx + 1)


def pension_total(lista: list[int], genero: str, edad: int, semanas: int, numero_hijos: int):
    if not lista:
        return 0
    
    if numero_hijos > 3: 
            numero_hijos = 3
        
    cuenta_semanas = semanas_mujer - (50 * numero_hijos)

    if (genero == "Femenino" and semanas < semanas_mujer - (50 * numero_hijos) and edad < 57) or (genero == "Masculino" and semanas < 1300 and edad < 62):
        raise InvalidDatesError()
    if genero == "Femenino" and edad < 57:
        raise InvalidAgeError(edad)
    if genero == "Masculino" and edad < 62:
        raise InvalidAgeError(edad)
    if genero == "Femenino" and semanas < semanas_mujer - (50 * numero_hijos):
        raise InvalidWeeksError(cuenta_semanas, semanas)
    

    pension = round(calculo_IBL(lista) / len(lista) * Porcentaje_pension, 2)

    if (genero == "Masculino" and edad >= 62 and semanas >= 1300):
        if pension < salario_minimo:
            return salario_minimo
        else:
            return pension
    
    if (genero == "Femenino" and edad >= 57):
        if pension < salario_minimo:
            return salario_minimo

        if (semanas >= cuenta_semanas):
            return pension
        
        else:
            return "No cumple con todos los requisitos"

    else:
        return "No cumple con todos los requisitos"
    

