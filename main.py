import sqlite3
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo


conexion = None

try: 
#-------------------------------------------
#           Conexion DB
#-------------------------------------------

    conexion = sqlite3.connect("ecotech.db")
    print("Conexion realizada.")

#-------------------------------------------
#           Creacion de cursor
#-------------------------------------------

    cursor = conexion.cursor()
    print("Cursos creado.")

#-------------------------------------------
#           Create Proyecto
#-------------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS proyecto (
    idProyecto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fechaInicio TEXT NOT NULL
    )    
""")
    conexion.commit()

#-------------------------------------------
#           Insert Proyecto
#-------------------------------------------

    nombreProyecto = input("Ingrese nombre del proyecto: ")
    descProyecto = input("Ingrese descripcion del proyecto: ")
    fechaProyecto = input("Ingrese fecha de Inicio del proyecto: ")
    
    proyecto_1 = Proyecto(None,nombreProyecto,descProyecto,fechaProyecto)

    cursor.execute("""
    INSERT INTO proyecto (nombre,descripcion,fechaInicio)
    values (?, ?, ?)
""", (nombreProyecto,descProyecto,fechaProyecto))

    conexion.commit()
    
#-------------------------------------------
#           Read Proyecto
#-------------------------------------------
    id_buscar = input("Ingrese id a buscar: ")

    cursor.execute("""
    SELECT idProyecto, nombre, descripcion
    FROM proyecto
    WHERE idProyecto = ?
""",(id_buscar,))

    proyecto_encontrado = cursor.fetchall()
    print(f"Proyecto encontrado: {proyecto_encontrado}")

#-------------------------------------------
#       Update Proyecto
#-------------------------------------------

#     cursor.execute("""
#     UPDATE proyecto
#     set idP
# """)
#     conexion.commit()

#-------------------------------------------
#           Delete Proyecto
#-------------------------------------------
#     idP = 1

#     cursor.execute("""
#     DELETE FROM proyecto
#     WHERE idProyecto = ?
# """)
#     conexion.commit()
#     print(f"proyecto {idP} eliminado.")

#----------------------------------------------------------------------
# Captura especificamente los errores de la base de datos
except sqlite3.Error as error:
    print(f"Error en la base de datos de SQLite: {error}")

# Captura cualquier otro tipo de error general en tu código
except Exception as error:
    print(f"Ocurrió un error inesperado: {error}")

# El bloque finally se ejecuta SIEMPRE (haya ocurrido un error o no)
finally:
    if conexion:
        conexion.close()
        print("Conexión a la base de datos cerrada.")