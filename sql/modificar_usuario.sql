UPDATE usuarios SET
    nombre = %s,
    apellido = %s,
    edad = %s,
    genero = %s,
    numero_hijos = %s,
    semanas_cotizadas = %s,
    salario1 = %s,
    salario2 = %s,
    salario3 = %s,
    salario4 = %s,
    salario5 = %s,
    salario6 = %s,
    salario7 = %s,
    salario8 = %s,
    salario9 = %s,
    salario10 = %s
WHERE cedula = %s;
