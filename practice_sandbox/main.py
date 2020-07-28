from flask import Flask, request, redirect, make_response, template_rendered

app = Flask(__name__)

@app.route("/")
def home():
    remote_ip = request.remote_addr
    make_redir  = redirect("/myIP")
    response = make_response(make_redir)
    response.set_cookie("ip_user", remote_ip)

    return response
    

@app.route('/myIP')
def myIP():
    ip_user = request.cookies.get('ip_user')
    
    return template_rendered('myip.html', ip_user)

# NOTAS
# Se declará el nombre de la app
# Utilizando request, se le pide la IP al cliente web.
# Con make_response, se generá una respuesta a cliente que lo redireccióna al path indicado.
# Se le genera una cookie al cliente que almacena su dirección IP.
# Tras la redirección se obtiene la info de la cookie y se imprime en pantalla.
