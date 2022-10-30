#importar libreria
#conexion a la base de datos
#crear el cursor 
#crear tabla 
#insertar registro(valores a las filas)
import sqlite3

def createDB():
    conexion = sqlite3.connect("data.db")
    conexion.commit()
    conexion.close()

def createTableUsuarios():
    conexion = sqlite3.connect("data.db")
    cursor=conexion.cursor()
    cursor.execute(
        """CREATE TABLE usuarios (
            pk INTEGER,
            name TEXT,
            apellido TEXT,
            puesto TEXT,
            correoElectronico TEXT,
            password TEXT 
    );"""
    )

    conexion.commit()
    conexion.close()

def insertRowInUsuarios():
    conexion = sqlite3.connect("data.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO usuarios (pk, name, apellido, puesto, correoElectronico, password)
        VALUES (1, 'Pepe', 'Pepito', 'Gerente', 'pepe@gmail.com', 'pepe12344');
    """)
    conexion.commit()
    conexion.close()
    
def readRow():
    conexion = sqlite3.connect("data.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM usuarios"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    
    conexion.commit()
    conexion.close()
    print(datos)

def updateRow():
    conexion = sqlite3.connect("data.db")
    cursor = conexion.cursor()
    update = f"UPDATE usuarios SET name='nuevomail@gmail.com' WHERE pk=1"
    cursor.execute(update)
    conexion.commit()
    conexion.close()


def deleteRow():
    conexion = sqlite3.connect("data.db")
    cursor = conexion.cursor()
    delete = f"DELETE FROM usuarios WHERE pk=1"
    cursor.execute(delete)
    conexion.commit()
    conexion.close()

# CREATE READ UPDATE DELETE = CRUD
if __name__ == "__main__":
    try:
        createDB()
    except:
        pass
    try:
        createTableUsuarios()
    except:
        pass

    insertRowInUsuarios()
    readRow()

    updateRow()
    readRow()

    deleteRow()
    readRow()