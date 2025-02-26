import sqlite3

# Clase que se encarga unicamente de la interaccion con la base de datos
class UserRepository:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    #Creador de la Base de Daros
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        self.conn.commit()

    #Funcion para insertar Usuario
    def insertUser(self, name, email):
        Consulta = f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')"
        self.cursor.execute(Consulta)
        self.conn.commit()
        return self.cursor.lastrowid

    #Obtener todos los usuarios
    def users(self):
        Consulta = "SELECT * FROM users"
        self.cursor.execute(Consulta)
        return self.cursor.fetchall()

    #Eliminar un usuario
    def removeUser(self, user_id):
        Consulta = f"DELETE FROM users WHERE id = {user_id}"
        self.cursor.execute(Consulta)
        self.conn.commit()


# Controlador que se encarga de recibir las peticiones y dirigirlas al repositorio
#(Intermediario entre la vista y el modelo)

#Clase que se encarga de la logica de negocio de Usuario
class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    #Crear un usuario
    def createUser(self, name, email):
        user_id = self.user_repository.insertUser(name, email)
        return f"Usuario {name} creado con éxito con ID {user_id}."

    #Obtener todos los usuarios
    def getUsers(self):
        return self.user_repository.users()

    #Eliminar un usuario
    def deleteUser(self, user_id):
        self.user_repository.removeUser(user_id)
        return f"Usuario con ID {user_id} eliminado."

# Función principal que actúa como capa de interfaz (View)
def main():
    repo = UserRepository()
    controller = UserController(repo)

    while True:
        print("\n1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Eliminar usuario")
        print("4. Salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            result = controller.createUser(name, email)
            print(result)
        elif option == "2":
            users = controller.getUsers()
            for user in users:
                print(user)
        elif option == "3":
            try:
                user_id = int(input("ID del usuario a eliminar: "))
                result = controller.deleteUser(user_id)
                print(result)
            except ValueError:
                print("Por favor, ingresa un ID numérico.")
        elif option == "4":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")


main()
