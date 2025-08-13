-- Asignar permisos a roles según la matriz proporcionada
-- Administrador tiene todos los permisos excepto los de salida
INSERT INTO Roles_Permisos (id_rol, id_permiso) VALUES
(1, 1), -- Admin: Ver inventario
(1, 2), -- Admin: Agregar productos
(1, 3), -- Admin: Aumentar inventario
(1, 4), -- Admin: Dar de baja/reactivar
(1, 7); -- Admin: Ver histórico