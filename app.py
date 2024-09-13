from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("app.html")

@app.route('/alumnos')
def alumnos():
    return render_template('adios.html')

@app.route("/alumnos/guardar", methods=["POST"])
def alumnos_Guardar():
    matricula= request.form["txtMatriculaFA"]
    nombre=request.form["txtNombreApellidoFA"]
    return f"Matricula: {matricula} Nombre: {nombre}"
   

if __name__ == '__main__':
    app.run(debug=True)
