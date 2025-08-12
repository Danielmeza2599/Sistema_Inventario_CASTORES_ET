from flask import Flask, request, jsonify, session, redirect, url_for
import pyodbc
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mezatech_secret' # Cambia esto por una clave secreta más segura en producción

# Configuración de la conexión a SQL Server
def get_db_connection():
    server = r'.\SQLEXPRESSNEW' # Nombre del servidor
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
        print(f"Error de conexión a la base de datos: {e}")
        return None

# Ruta para el login
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        return jsonify({'success': False, 'message': 'Email y contraseña son requeridos'})
    
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Consulta segura con parámetros para evitar SQL injection
            cursor.execute(
                "SELECT id_usuario, nombre, contrasena FROM Usuarios WHERE email = ?", 
                (email,)
            )
            user = cursor.fetchone()
            
            if user:
                # Comparación directa de contraseñas (mejor usar hash en producción)
                if user.contrasena == password:
                    session['user_id'] = user.id_usuario
                    session['user_name'] = user.nombre
                    return jsonify({
                        'success': True, 
                        'redirect': '/dashboard',
                        'username': user.nombre
                    })
                else:
                    return jsonify({'success': False, 'message': 'Contraseña incorrecta'})
            else:
                return jsonify({'success': False, 'message': 'Usuario no encontrado'})
                
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error en la base de datos: {str(e)}'})
        finally:
            conn.close()
    else:
        return jsonify({'success': False, 'message': 'Error de conexión a la base de datos'})

# Prueba de conexión y confirmacion
#if __name__ == '__main__':
 #   conexion = get_db_connection()
  #  if conexion:
   #     print("Conexión establecida correctamente")
    #    conexion.close()  # No olvides cerrar la conexión
     #   print("sesion finalizada correctamente")
    #else:
     #   print("No se pudo establecer la conexión")