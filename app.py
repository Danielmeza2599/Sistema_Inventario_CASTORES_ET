from flask import Flask, request, jsonify, render_template
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a SQL Server
def get_db_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=.\SQLEXPRESSNEW;'
        'DATABASE=SistemaInventario;'
        'UID=sa;'
        'PWD=mezasql'
    )

# Ruta para manejar el login
@app.route('/login', methods=['POST']) # Acepta solo POST
def login():
        
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'No se recibieron datos'}), 400
            
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({'success': False, 'message': 'Email y contraseña son requeridos'}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_usuario, nombre FROM Usuarios WHERE email = ? AND contrasena = ?", 
            (email, password)
        )
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return jsonify({
                'success': True,
                'user': {
                    'id': user.id_usuario,
                    'name': user.nombre
                }
            })
        else:
            return jsonify({'success': False, 'message': 'Credenciales incorrectas'}), 401
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/inventario')
def mostrar_inventario():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Consulta para obtener los productos del inventario
        cursor.execute('''
            SELECT id_producto, nombre, descripcion, cantidad, activo, 
            fecha_creacion, fecha_modificacion 
            FROM Productos
            ORDER BY fecha_creacion ASC
        ''')
        
        # Obtener los nombres de las columnas
        columns = [column[0] for column in cursor.description]
        
        # Obtener los datos
        productos = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        cursor.close()
        conn.close()
        
        return render_template('inventario.html', productos=productos)
    
    except Exception as e:
        return f"Error al conectar a la base de datos: {str(e)}"



# Ruta para mostrar el dashboard
@app.route('/inventario')
def inventario(id):
    return render_template('inventario.html')

# Ruta principal que redirige
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5500, debug=True)