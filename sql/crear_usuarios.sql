create table if not exists usuarios (
    cedula varchar(15) primary key not null,
    nombre varchar(15) not null,
    apellido varchar(15) not null,
    edad varchar(15) not null,
    genero varchar(10) not null,
    numero_hijos Integer not null,
    semanas_cotizadas Integer not null,
    salario_1 NUMERIC(12,2) not null,
    salario_3 NUMERIC(12,2) not null,
    salario_2 NUMERIC(12,2) not null,
    salario_4 NUMERIC(12,2) not null,
    salario_5 NUMERIC(12,2) not null,
    salario_6 NUMERIC(12,2) not null,
    salario_7 NUMERIC(12,2) not null,
    salario_8 NUMERIC(12,2) not null,
    salario_9 NUMERIC(12,2) not null,
    salario_10 NUMERIC(12,2) not null
)
