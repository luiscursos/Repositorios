import sqlite3


def main():
    create_user(5, "juan", "pekas")

def create_user(id, name, password):
    # Con isolation_level con cada "EXECUTE" se almacena en el cursor y se envia al servidor
    conn = sqlite3.connect("/home/lucato/Documents/Curso_Python/Repositorios/Open_BootCamp/Python_Fundamentos/myapplication.db", isolation_level=None)
    cursor = conn.cursor()

    query = f"INSERT INTO users (id, name, password) VALUES({id}, '{name}', '{password}')"
    rows = cursor.execute(query)

    # Commit es necesario cuando se modifica la tabla bien DELETE o INSERT
    conn.commit()
   

    cursor.close()
    conn.close()

   
if __name__ == '__main__':
    main()