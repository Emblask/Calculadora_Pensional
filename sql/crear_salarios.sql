create table if not exists salarios(
    id SERIAL PRIMARY KEY,
    cedula varchar(15) not null,
    salario_ano1 NUMERIC(12,2) not null,
    salario_ano2 NUMERIC(12,2) not null,
    salario_ano3 NUMERIC(12,2) not null,
    salario_ano4 NUMERIC(12,2) not null,
    salario_ano5 NUMERIC(12,2) not null,
    salario_ano6 NUMERIC(12,2) not null,
    salario_ano7 NUMERIC(12,2) not null,
    salario_ano8 NUMERIC(12,2) not null,
    salario_ano9 NUMERIC(12,2) not null,
    salario_ano10 NUMERIC(12,2) not null,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula)
);