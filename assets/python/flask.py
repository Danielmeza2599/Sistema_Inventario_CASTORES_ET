from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    conexion = conectar_sql_server()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TuTabla LIMIT 10")
        datos = cursor.fetchall()
        conexion.close()
        return render_template('index.html', datos=datos)
    return "Error de conexión a la base de datos"

@app.route('/consulta', methods=['POST'])
def consulta():
    parametro = request.form['parametro']
    conexion = conectar_sql_server()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM TuTabla WHERE columna = ?", parametro)
        datos = cursor.fetchall()
        conexion.close()
        return render_template('resultados.html', datos=datos)
    return "Error de conexión a la base de datos"

if __name__ == '__main__':
    app.run(debug=True)