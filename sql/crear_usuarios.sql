create table if not exist usuarios (
    cedula varchar(15) primary key not null,
    nombre varchar(15) not null,
    apellido varchar(15) not null,
    edad varchar(15) not null,
    genero varchar(10) not null
)