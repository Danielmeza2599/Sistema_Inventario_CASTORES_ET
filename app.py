from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)  # Habilita CORS

def get_db_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=.\SQLEXPRESSNEW;'
        'DATABASE=SistemaInventario;'
        'UID=sa;'
        'PWD=mezasql'
    )

@app.route('/login', methods=['POST', 'OPTIONS'])  # Añade OPTIONS para CORS
def login():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
        
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)