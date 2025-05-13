create table if not exists salarios(
    id SERIAL PRIMARY KEY,
    salario_año1 NUMERIC(12,2) not null,
    salario_año2 NUMERIC(12,2) not null,
    salario_año3 NUMERIC(12,2) not null,
    salario_año4 NUMERIC(12,2) not null,
    salario_año5 NUMERIC(12,2) not null,
    salario_año6 NUMERIC(12,2) not null,
    salario_año7 NUMERIC(12,2) not null,
    salario_año8 NUMERIC(12,2) not null,
    salario_año9 NUMERIC(12,2) not null,
    salario_año10 NUMERIC(12,2) not null,
    FOREIGN KEY (cedula) REFERENCES usuarios(cedula),
)