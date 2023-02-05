import sqlite3
import getpass  

def main():
    name = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(name,password):
        print("login correcto")
    else:
        print("login incorrecto")

def verifica_credenciales(name,password):
    conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/Python_Fundamentos/myapplication.db")
    cursor = conn.cursor()

    query=(f"SELECT id FROM users WHERE name='{name}' AND password='{password}'")
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data==None:
        return False
    return True

# Abrir conexión a la base de datos. Indicar el PATH completo donde esta la bbdd
conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/Python_Fundamentos/myapplication.db")

# Cursor es una variable que va cambiando de dato, es un iterador
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users')
for row in rows:
    print(row)

rows = cursor.execute("SELECT * FROM users WHERE name='vroman'")
for row in rows:
    print(row)

# Cerrar el cursor
cursor.close()


# Cerrar conexión a la base de datos
conn.close()


    

if __name__ == '__main__':
    main()
