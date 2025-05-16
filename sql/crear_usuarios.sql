create table if not exists usuarios (
    cedula varchar(15) primary key not null,
    nombre varchar(15) not null,
    apellido varchar(15) not null,
    edad varchar(15) not null,
    genero varchar(10) not null,
    numero_hijos Integer not null,
    semanas_cotizadas Integer not null,
    salario_ano_1 NUMERIC(12,2) not null,
    salario_ano_2 NUMERIC(12,2) not null,
    salario_ano_3 NUMERIC(12,2) not null,
    salario_ano_4 NUMERIC(12,2) not null,
    salario_ano_5 NUMERIC(12,2) not null,
    salario_ano_6 NUMERIC(12,2) not null,
    salario_ano_7 NUMERIC(12,2) not null,
    salario_ano_8 NUMERIC(12,2) not null,
    salario_ano_9 NUMERIC(12,2) not null,
    salario_ano_10 NUMERIC(12,2) not null
)