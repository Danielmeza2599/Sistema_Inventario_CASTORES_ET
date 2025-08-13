-- Crear índices para mejorar rendimiento
CREATE INDEX idx_productos_activos ON Productos(activo);
CREATE INDEX idx_movimientos_fecha ON Movimientos(fecha_movimiento);
CREATE INDEX idx_movimientos_producto ON Movimientos(id_producto);
CREATE INDEX idx_movimientos_usuario ON Movimientos(id_usuario);