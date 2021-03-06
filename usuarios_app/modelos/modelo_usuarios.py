from usuarios_app.config.mysqlconnection import connectToMySQL


class Usuario:
    def __init__(self,id, first_name,last_name,email,created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name =last_name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at
    
    @classmethod
    def obtenerListaUsuarios (cls):
        query = "SELECT * FROM users;"
        resultado = connectToMySQL ("users_db").query_db(query)
        listaUsuarios = []
        for usuario in resultado:
            listaUsuarios.append (Usuario (usuario["id"],usuario["first_name"],usuario["last_name"], usuario ["email"], usuario["created_at"], usuario['updated_at']))
        return listaUsuarios


    @classmethod
    def crear(cls, nuevoUsuario):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('users_db').query_db(query,nuevoUsuario)
        return result
        

