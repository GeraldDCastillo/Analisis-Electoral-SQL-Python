USE CursoSQL; -- Asegúrate de estar en tu base de datos

-- 1. Crear la tabla de Regiones
CREATE TABLE Regiones (
    Estado NVARCHAR(50),
    Zona NVARCHAR(50)
);

-- 2. Insertar datos (Mapeamos algunos estados clave)
INSERT INTO Regiones (Estado, Zona) VALUES
('MÉXICO', 'Centro'),
('CIUDAD DE MÉXICO', 'Centro'),
('JALISCO', 'Occidente'),
('NUEVO LEÓN', 'Norte'),
('VERACRUZ', 'Sur'),
('PUEBLA', 'Centro'),
('GUANAJUATO', 'Bajío'),
('CHIAPAS', 'Sur'),
('YUCATÁN', 'Sur'),
('SINALOA', 'Norte');

-- 3. ¡LA PRUEBA DE FUEGO! El JOIN
-- Queremos ver los Votos PERO sumados por ZONA, no por estado.
SELECT
    R.Zona,
    SUM(V.Votos) AS Total_Votos_Zona
FROM dbo.votos AS V
INNER JOIN dbo.Regiones AS R
    ON V.ENTIDAD = R.Estado
GROUP BY R.Zona
ORDER BY Total_Votos_Zona DESC;

CREATE VIEW Vista_Reporte_Zonas AS
SELECT
    R.Zona,
    SUM(V.Votos) AS Total_Votos
FROM dbo.votos AS V
INNER JOIN dbo.Regiones AS R
    ON V.ENTIDAD = R.Estado
GROUP BY R.Zona;

UPDATE dbo.votos
SET Votos = Votos + 100000000
WHERE ENTIDAD = 'NUEVO LEÓN';

-- Verificamos el cambio en la Vista inmediatamente
SELECT * FROM Vista_Reporte_Zonas;

UPDATE dbo.votos
SET Votos = Votos - 100000000
WHERE ENTIDAD = 'NUEVO LEÓN';

-- Verificamos el cambio en la Vista inmediatamente
SELECT * FROM Vista_Reporte_Zonas;
