from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Aquí iría tu lógica de conexión a SQL Server
    # y validación de credenciales
    
    if email == "daniel@gmail.com" and password == "meza":  # Ejemplo temporal
        return jsonify({'success': True, 'message': 'Login exitoso'})
    else:
        return jsonify({'success': False, 'message': 'Credenciales incorrectas'}), 401

if __name__ == '__main__':
    app.run(port=5500, debug=True)