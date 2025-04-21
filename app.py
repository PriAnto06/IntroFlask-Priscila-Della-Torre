from flask import Flask, render_template
import sqlite3 

app = Flask(__name__)

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

db = None
def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory 

def cerrarConexion():
    global db
    db.close()
    db = None

@app.route('/test-db')
def testDB():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) AS cant FROM usuarios ;")
    res =cursor.fetchone()
    registros = res ["cant"]
    cerrarConexion()
    return f"Hay {registros} registros en la tabla de ususario"

@app.route("/crear-usuario")
def testCrear():
    nombre = "leandro"
    email = "leandro@etec.uba.ar"
    abrirConexion()
    cursor = db
    consulta = "INSERT INTO usuarios(usuario, email)VALUES (?,?);"
    cursor.execute(consulta,(nombre,email))
    db.commit()
    cerrarConexion()
    return f"Registro agregado({nombre})"


@app.route("/crear-usuario/<string:nombre>/<string:email>")
def testCrearXArgumento(nombre,email):
    abrirConexion()
    cursor = db
    consulta = "INSERT INTO usuarios(usuario, email)VALUES (?,?);"
    cursor.execute(consulta,(nombre,email))
    db.commit()
    cerrarConexion()
    return f"Registro agregado({nombre},{email})"


@app.route('/saludar/hola')
def hello():
    return 'Hello, World!'

@app.route('/saludar/chau')
def chau():
    return 'Bye'

@app.route('/sumar/<int:n1>/<int:n2>')
def sum(n1,n2):
    s = n1+n2
    return f'<p>  {n1}+{n2}={s} </p>'

#21-04-25

@app.route('/mostrar-datos/<int:id>')
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id,usuario,email FROM usuarios WHERE id = ?",(id,))
    res =cursor.fetchone()#cuando no hay nada me devuelve none(nada)
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario=res['usuario']
        email=res ['email']
    return render_template("datos.html",id=id,usuario=usuario,email=email)     


    #registros = res ["cant"]
    #cerrarConexion()
    #return f"Hay {registros} registros en la tabla de ususario"
