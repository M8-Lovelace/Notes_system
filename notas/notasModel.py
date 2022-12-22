
# Importamos la librería datetime de python
from datetime import datetime

# Importamos el módulo que genera la conexión a la base de datos
from conexiones import conectar

# Generamos la conexión y extraemos los datos que nos retorna
conectar = conectar.conexion()
database = conectar[0]
cursor = conectar[1]

class Notas:
    def __init__(self, titulo, usuario_id, descripcion):
        self.titulo = titulo
        self.usuario_id = usuario_id
        self.descripcion = descripcion

    def guardar(self):
        now = datetime.now()
        now = now.date()
        sql = "INSERT INTO notas VALUES (null, %s,%s,%s,%s)"
        usuario = (self.usuario_id, self.titulo,self.descripcion, now)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            print("\n✔ Perfecto! Has guardado la nota: ",self.titulo)
        except:
            print("\n❌ Error en creación de la nota, verifique sus datos")

    def listar(usuario_id):
        # Sentencia SQL
        sql = f"SELECT * FROM notas where usuario_id = '{usuario_id}'"
        # Ejecución de la sentencia SQL
        cursor.execute(sql)
        # Guardar los resultados en la variable result
        return cursor.fetchall()

    def eliminar(usuario_id, titulo):
        sql = f"DELETE FROM notas where usuario_id = {usuario_id} AND titulo = '{titulo}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount]

    @staticmethod
    def validar(usuario_id, titulo):
        sql = f"SELECT * FROM notas where titulo = '{titulo}' AND usuario_id = '{usuario_id}'"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            return True
        else:
            print("\n❌ El titulo ingresado ya existe!")
            return False