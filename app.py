from flask import Flask
from flask import render_template
from flask import request

import pusher



app = Flask(__name__)
@app.route("/")
def index():
    return render_template("app.html")
@app.route("/evento")
def evento()
    pusher_client = pusher.Pusher(
      app_id='1864238',
      key='2ea386b7b90472052932',
      secret='578df1dc2b254c75c850',
      cluster='us2',
      ssl=True
    )

    pusher_client.trigger('conexion', 'evento', {'message': 'hello world'})

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
