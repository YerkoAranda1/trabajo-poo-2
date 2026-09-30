import sqlite3
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo

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
