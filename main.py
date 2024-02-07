from flask import Flask, request, make_response, redirect, render_template #importo desde la libreria flask 

app = Flask(__name__) #inicio la app

@app.route("/index") #declaro cual va a ser mi ruta desde el url (a esto es le llama endpoint)
def index():
    user_ip_information = request.remote_addr #el objeto request accede a la informfacion que esta enviando el cliente 
    response = make_response(redirect('/show_information_address')) #el make response crea una redireccion como respuesta
    response.set_cookie('user_ip_information', user_ip_information) #la cookie sirve para cuando accede el cliente se cree automaticamente en la web y se puedan a acceder a los parametros
    return response

@app.route('/show_information_address') #aca creamos la url donde vamos a redirigir a cliente
def show_information():
    user_ip=request.cookies.get("user_ip_information")
    return render_template("ip_information.html", user_ip=user_ip)#con render_template leo el html y con user_ip=user_ip le envio el valor desde python al html
    
app.run(debug = True) #con esto corro la app y el debug sirve para poder actualizar sola la pagina