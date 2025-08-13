from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    # Aquí ira la lógica de conexión a SQL Server
    # y validación de credenciales
    
    if email == "daniel@gmail.com" and password == "meza":  # Ejemplo temporal
        return jsonify({'success': True, 'message': 'Login exitoso'})
    else:
        return jsonify({'success': False, 'message': 'Credenciales incorrectas'}), 401

# Ruta para mostrar el dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta principal que redirige
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5500, debug=True)