-- Tabla de Movimientos
CREATE TABLE Movimientos (
    id_movimiento INT PRIMARY KEY IDENTITY(1,1),
    id_producto INT NOT NULL,
    id_usuario INT NOT NULL,
    tipo_movimiento VARCHAR(10) CHECK (tipo_movimiento IN ('entrada', 'salida')) NOT NULL,
    cantidad INT NOT NULL,
    fecha_movimiento DATETIME DEFAULT GETDATE(),
    notas TEXT NULL,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);