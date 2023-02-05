import sqlite3
import getpass

def main():
    name = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(name, password):
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

if __name__ == '__main__':
    main()