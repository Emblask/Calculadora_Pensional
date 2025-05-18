create table if not exists usuarios (
    cedula varchar(15) primary key not null,
    nombre varchar(15) not null,
    apellido varchar(15) not null,
    edad varchar(15) not null,
    genero varchar(10) not null,
    numero_hijos Integer not null,
    semanas_cotizadas Integer not null,
    salario1 NUMERIC(12,2) not null,
    salario3 NUMERIC(12,2) not null,
    salario2 NUMERIC(12,2) not null,
    salario4 NUMERIC(12,2) not null,
    salario5 NUMERIC(12,2) not null,
    salario6 NUMERIC(12,2) not null,
    salario7 NUMERIC(12,2) not null,
    salario8 NUMERIC(12,2) not null,
    salario9 NUMERIC(12,2) not null,
    salario10 NUMERIC(12,2) not null
)
