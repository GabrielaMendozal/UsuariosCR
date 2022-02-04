from flask import Flask, render_template, request , redirect
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario

#rutas
@app.route ('/', methods = ['GET'])
def inicio():
    return redirect('/users')

@app.route ('/users', methods = ['GET'])
def users():
    return render_template ("index.html", usuarios =Usuario.obtenerListaUsuarios() )

@app.route ('/user/new')
def nuevoUsuario():
    return render_template ("index2.html")

@app.route ('/user/create', methods = ['POST'])
def registrarUsuario():
    nuevoUsuario = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    
    if nuevoUsuario["first_name"] == "" or nuevoUsuario["last_name"] == "" or nuevoUsuario["email"] == "":
        return redirect ("/user/new")
    
    resultado = Usuario.crear( nuevoUsuario )
    
    if type( resultado ) is int and resultado == 0:
        return redirect( '/users' )
    else:
        return redirect ("/user/new")
                