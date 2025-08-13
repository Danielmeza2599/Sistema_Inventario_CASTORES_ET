-- Almacenista tiene permisos específicos
INSERT INTO Roles_Permisos (id_rol, id_permiso) VALUES
(2, 1), -- Almacenista: Ver inventario
(2, 5), -- Almacenista: Ver módulo salida
(2, 6); -- Almacenista: Sacar inventario