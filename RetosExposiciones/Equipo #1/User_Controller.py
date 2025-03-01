import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Creamos la tabla si no existe 
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
conn.commit()

class UserController:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

    def create_user(self, name, email):
        """Crea un usuario en la base de datos"""
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()
        print(f"Usuario {name} creado con éxito.")

    def get_users(self):
        """Obtiene todos los usuarios de la base de datos"""
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        for user in users:
            print(user)

    def delete_user(self, user_id):
        """Elimina un usuario de la base de datos"""
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()
        print(f"Usuario con ID {user_id} eliminado.")

# Menú interactivo 
if __name__ == "__main__":
    controller = UserController()
    
    while True:
        print("\n1. Crear usuario")
        print("2. Ver usuarios")
        print("3. Eliminar usuario")
        print("4. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            controller.create_user(name, email)
        elif option == "2":
            controller.get_users()
        elif option == "3":
            user_id = input("ID del usuario a eliminar: ")
            controller.delete_user(user_id)
        elif option == "4":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")