INSERT INTO usuarios (
    cedula, nombre, apellido, edad, genero, numero_hijos, semanas_cotizadas,
    salario1, salario2, salario3, salario4, salario5,
    salario6, salario7, salario8, salario9, salario10
) VALUES (%s, %s, %s, %s, %s, %s, %s,
          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
