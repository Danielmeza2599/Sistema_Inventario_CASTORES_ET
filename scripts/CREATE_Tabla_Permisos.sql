-- Tabla de Permisos
CREATE TABLE Permisos (
    id_permiso INT PRIMARY KEY IDENTITY(1,1),
    nombre_permiso VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);