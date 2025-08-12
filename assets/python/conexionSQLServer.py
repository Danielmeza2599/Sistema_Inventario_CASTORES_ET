import pyodbc

def conectar_sql_server():
    server = r'.\SQLEXPRESSNEW' # Puede ser una IP o nombre del servidor
    database = 'SistemaInventario'
    username = 'sa'
    password = 'mezasql'
    
    try:
        conexion = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )
        print("✅ Conexión exitosa a SQL Server")
        return conexion
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return None


# Prueba de conexión y confirmacion
if __name__ == '__main__':
    conexion = conectar_sql_server()
    if conexion:
        print("Conexión establecida correctamente")
        conexion.close()  # No olvides cerrar la conexión
        print("sesion finalizada correctamente")
    else:
        print("No se pudo establecer la conexión")