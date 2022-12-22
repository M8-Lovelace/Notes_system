# Ejecutar codigo en MySQL Workbench

# Creación de la base de datos
CREATE DATABASE notas;
# Usar la base de datos
USE notas;

# Creación de las tablas y sus relaciones
CREATE TABLE IF NOT EXISTS usuarios(
  id INT(10) AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  apellidos VARCHAR(20) NOT NULL,
  email varchar(40) NOT NULL,
  contrasena varchar(30) NOT NULL,
  now varchar(30) NOT NULL,
  CONSTRAINT pk_usuarios PRIMARY KEY (id)
  );

CREATE TABLE IF NOT EXISTS notas(
  id INT(10) AUTO_INCREMENT NOT NULL,
  usuario_id INT(10) NOT NULL,
  titulo varchar(20) NOT NULL,
  descripcion varchar(400) NOT NULL,
  now varchar(30) NOT NULL,
  CONSTRAINT pk_notas PRIMARY KEY (id),
  CONSTRAINT fk_notas FOREIGN KEY (usuario_id) references usuarios(id)
  );