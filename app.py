from flask import Flask
from flask import render_template
from flask import request

import pusher
import mysql.connector
import datetime
import pytz

con = mysql.connector.connect(
  host="185.232.14.52",
  database="u760464709_tst_sep",
  user="u760464709_tst_sep_usr",
  password="dJ0CIAFF="
)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("app.html")
@app.route("/buscar")
def buscar():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM sensor_log")
    con.close()
    
    registros = cursor.fetchall()

    return registros

@app.route('/alumnos')
def alumnos():
    return render_template('adios.html')

@app.route("/alumnos/guardar", methods=["POST"])
def alumnos_Guardar():
    matricula= request.form["txtMatriculaFA"]
    nombre=request.form["txtNombreApellidoFA"]
    return f"Matricula: {matricula} Nombre: {nombre}"
    
@app.route("/evento", methods=["GET"])
def evento():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()

    args = request.args
  
    sql = "INSERT INTO sensor_log (Temperatura, Humedad, Fecha_Hora) VALUES (%s, %s, %s)"
    val = (args["temperatura"], args["humedad"], datetime.datetime.now())
    cursor.execute(sql, val)
    
    con.commit()
    con.close()

    pusher_client = pusher.Pusher(
      app_id='1864238',
      key='2ea386b7b90472052932',
      secret='578df1dc2b254c75c850',
      cluster='us2',
      ssl=True
    )
    pusher_client.trigger("conexion", "evento", request.args)

if __name__ == '__main__':
    app.run(debug=True)
