/*----1. CREACION DEL ENTORNO ----*/
CREATE DATABASE EvetosTechDB;
USE EventosTechDB;

/*-----2. DEFINICION DE TABLAS----*/


CREATE TABLE Asistentes (
    
    Asistentes_id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    empresa VARCHAR(100),
    email VARCHAR(100)
);


CREATE TABLE Conferencias (
    
    id_conferencia INT PRIMARY KEY,
    titulo VARCHAR(100),
    sala VARCHAR(50),
    capacidad_maxima INT
);

CREATE TABLE Inscripciones (
    
    id_inscripcion INT PRIMARY KEY,
    id_asistente INT,
    id_conferencia  INT,
    fecha_registro DATE
);

/*-------3. INTEGRIDAD REFERENCIAL----*/
ALTER TABLE  Inscripciones
add CONSTRAINT fk_asistente
REFERENCES Asistente(id_asistente);
add CONSTRAINT fk_asistente
ALTER TABLE Inscripciones
add CONSTRAINT fk_conferencia
FOREIGN KEY (id_conferencia);

/*-------3. INTEGRIDAD REFERENCIAL----*/
ALTER TABLE  Inscripciones
add CONSTRAINT fk_asistente
REFERENCES Asistente(id_asistente);
add CONSTRAINT fk_asistente
ALTER TABLE Inscripciones
add CONSTRAINT fk_conferencia
FOREIGN KEY (id_conferencia);



/*--------4. OPTIMIZACION --------*/
CREATE INDEX idx_empresa ON
Asistentes(empresa);

/*-------5. POBLADO DE DATOS-----*/
INSERT INTO Asistentes (Asistentes_id, nombre, apellido, empresa, email) VALUES
(101,'Juan', 'Perez', 'TechNova', 'juan.perez@email.com'),
(102, 'Ana', 'García','Apple', 'ana.garcia@email.com'),
(103, 'Carlos', 'Rodriguez', 'Samsung', 'carlos.r@email.com'),
(104, 'Maria', 'Lopez', 'Amazon', 'maria.lopez@email.com'),
(105, 'Luis', 'Martinez', 'Movistar', 'luis.martinez@email.com');

INSERT INTO Conferencias ( id_conferencia, titulo, sala, capacidad_maxima) VALUES
(201, 'Programador', 'Sala A1', 50),
(202, 'Backend ', 'Sala B2', 30),
(203, 'QSL Avanzado', 'Sala C3', 40),
(204, 'Frontend', 'Sala D4', 20),
(205, 'Ciberseguridad', 'Sala E5', 25);

INSERT INTO Inscripciones (id_inscripcion, id_asistente, id_conferencia, fecha_registro) VALUES
(1001, 101, 201, '05/10/2023'),
(1002, 102, 202, '02/06/2024'),
(1003, 103, 203, '03/09/2025'),
(1004, 104, 204, '04/02/2021'),
(1005, 105, 205, '19/5/2020');

-----Parte2-----------Video-------------

/*-----6. Simulacion de Error/Cambio------*/
/*-----CAMBIO-----*/
UPDATE Asistentes 
SET empresa = 'Movilnet' 
 WHERE nombre = 'Luis'
    AND apellido = 'Martinez'
    AND empresa = 'Movistar';


/*----ERROR-----*/
 DELETE FROM Inscripciones WHERE id_inscripcion = 1005;

/*------7.MODIFICACION DE ESTRUCTURA------*/
ALTER TABLE Conferencias ADD COLUMN precio INT;

UPDATE Conferencias SET precio = 100 WHERE id_conferencia = 201;
UPDATE Conferencias SET precio = 150 WHERE id_conferencia = 202;
UPDATE Conferencias SET precio = 200 WHERE id_conferencia = 203;
UPDATE Conferencias SET precio = 200 WHERE id_conferencia = 204;
UPDATE Conferencias SET precio = 200 WHERE id_conferencia = 205;

/*-------8. REPORTE DE INGRESOS (AGREGACION)-------*/
SELECT c.titulo, COUNT(i.id_inscripcion) AS total_inscritos 
FROM Conferencias c  
INNER JOIN Inscripciones i ON c.id_conferencia = i.id_conferencia
GROUP BY c.titulo
HAVING COUNT(i.id_inscripcion) > 2;

/*--------9. FILTRO DE EXITO(HAVING)----*/ 
SELECT c.titulo,
COUNT(i.id_inscripcion) AS total_inscritos
FROM Conferencias c
INNER JOIN Inscripciones i ON c.id_conferencia = i.id_conferencia
GROUP BY c.titulo
HAVING COUNT(i.id_inscripcion) > 2;

/*------10. LISTADO DETALLADO(JOINS)-----*/
SELECT 
    Asistentes.nombre, 
    Asistentes.apellido, 
    Conferencias.titulo, 
    Conferencias.sala
FROM Inscripciones
INNER JOIN Asistentes ON Inscripciones.id_asistente = Asistentes.Asistentes_id
INNER JOIN Conferencias ON Inscripciones.id_conferencia = Conferencias.id_conferencia;

/*-------11.AUDITORIA DE VACIOS(LEFT JOIN)-----*/
SELECT Conferencias.titulo AS Conferencia_Sin_Inscritos
FROM Conferencias
LEFT JOIN Inscripciones ON Conferencias.id_conferencia = Inscripciones.id_conferencia
WHERE Inscripciones.id_conferencia IS NULL;

/*--------12.CONSULTA VIP(SUBCONSULTO)------*/
SELECT 
    nombre, 
    apellido 
FROM Asistentes 
WHERE Asistentes_id IN (
    SELECT id_asistente 
    FROM Inscripciones 
    WHERE id_conferencia = (
        SELECT id_conferencia 
        FROM Conferencias 
        ORDER BY capacidad_maxima DESC 
        LIMIT 1
    )
);

/*------13.LIMPIEZA (DROP)------*/
CREATE TABLE Notas_Finales (
    id_nota INT PRIMARY KEY,
    comentario VARCHAR(255)
);

INSERT INTO Notas_Finales (id_nota, comentario) 
VALUES (1, 'Proyecto de Base de Datos completado con éxito');

SELECT * FROM Notas_Finales;
DROP TABLE Notas_Finales;

/*--CHAOOOOOOOOOOOOOOOOOOOOOOO PORFINNNNNNNNNNNNN---------*/