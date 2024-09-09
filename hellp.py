from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hola, mundo'

@app.route('/esclavos')
def home():
    return render_template('hello.html')

@app.route("/esclavos/guardar", methods=["POST"])
def esclavos_Guardar():
    return f"Matricula: {request.form["matricula"]} Nombre: {request.form["nombre"]}"

@app.route('/alumnos')
def alumnos():
    return render_template('adios.html')

@app.route("/alumnos/guardar", methods=["POST"])
def alumnos_Guardar():
    return f"Matricula: {request.form["txtMatriculaFA"]} Nombre: {request.form["txtNombreApellidoFA"]}"
   

if __name__ == '__main__':
    app.run(debug=True)
