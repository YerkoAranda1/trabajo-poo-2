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
    
#     def __init__(self,idProyecto,nombre,descripcion,fechaInicio):
#         self.idProyecto = idProyecto
#         self.nombre = nombre
#         self.descripcion = descripcion
#         self.fechaInicio = fechaInicio





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