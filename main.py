from flask import Flask, request ##importo desde la libreria flask 

app = Flask(__name__) ##inicio la app

@app.route("/home") ## declaro cual va a ser mi ruta desde el url (a esto es le llama endpoint)
def hello():
    user_ip_information = request.remote_addr ##el objeto request accede a la informfacion que esta enviando el cliente 
    return f'Esta es la ip del cliente {user_ip_information}'

app.run(debug = True) ##con esto corro la app y el debug sirve para poder actualizar sola la pagina