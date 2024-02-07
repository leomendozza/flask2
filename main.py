from flask import Flask, request, make_response, redirect ##importo desde la libreria flask 

app = Flask(__name__) ##inicio la app

@app.route("/index") ## declaro cual va a ser mi ruta desde el url (a esto es le llama endpoint)
def index():
    user_ip_information = request.remote_addr ##el objeto request accede a la informfacion que esta enviando el cliente 
    response = make_response(redirect('/show_information_address'))
    response.set_cookie('user_ip_information', user_ip_information)
    return response

@app.route('/show_information_address')
def show_information():
    user_ip=request.cookies.get("user_ip_information")
    return f"Esta es la direccion ip del cliente {user_ip}" 
    
app.run(debug = True) ##con esto corro la app y el debug sirve para poder actualizar sola la pagina