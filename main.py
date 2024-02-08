from flask import Flask, request, make_response, redirect, render_template #importo desde la libreria flask 
from flask_bootstrap import Bootstrap 
app = Flask(__name__) #inicio la app

bootstrap = Bootstrap(app)

items = ["item 1", "item 2", "item 3", "item 4"]
@app.errorhandler(404) #ruta especial para los errores
def not_found_endpoint(error):
    return render_template('404.html', error=error) #lee el html 404.html donde vamos a crear una plantilla para cuando se genere un error


@app.route("/index") #declaro cual va a ser mi ruta desde el url (a esto es le llama endpoint)
def index():
    user_ip_information = request.remote_addr #el objeto request accede a la informfacion que esta enviando el cliente 
    response = make_response(redirect('/show_information_address')) #el make response crea una redireccion como respuesta
    response.set_cookie('user_ip_information', user_ip_information) #la cookie sirve para cuando accede el cliente se cree automaticamente en la web y se puedan a acceder a los parametros
    return response

@app.route('/show_information_address') #aca creamos la url donde vamos a redirigir a cliente
def show_information():
    user_ip=request.cookies.get("user_ip_information")
    context ={
        "user_ip":user_ip,
        "items": items
    }
    return render_template("ip_information.html", **context)#con render_template leo el html y con user_ip=user_ip le envio el valor desde python al html - con **descomprime la lista y puedo llamar directamente en el html
    
app.run(debug = True) #con esto corro la app y el debug sirve para poder actualizar sola la pagina


