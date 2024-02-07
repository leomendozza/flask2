from flask import Flask ##importo desde la libreria flask 

app = Flask(__name__) ##inicio la app

@app.route("/home") ## declaro cual va a ser mi ruta desde el url (a esto es le llama endpoint)
def hello():
    return "hola"

app.run(debug = True) ##con esto corro la app y el debug sirve para poder actualizar sola la pagina