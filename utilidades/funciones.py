# Importamos el modelo de usuarios
from usuarios import usuariosModel
from notas import notasModel

# Importamos la función time para dar una mejor experiencia de usuario
import time

# Importamos el módulo que genera la conexión a la base de datos
from conexiones import conectar
conectar = conectar.conexion()
cursor = conectar[1]

# Función para registrar usuarios
def registro():
    print("\nOK! Vamos a registrarte en el sistema...")
    time.sleep(2)
    nombre = input("¿Cual es tu nombre?: ")
    apellidos = input("¿Cual es tu apellido?: ")
    email = input("Ingresa tu email: ")
    verificarEmail = usuariosModel.Usuarios.validar(email)
    if verificarEmail:
        contrasena = input("Ingresa tu contraseña: ")
        usuario = usuariosModel.Usuarios(
            None, nombre, apellidos, email, contrasena)
        usuario.guardar()

# Función para loguearse en el sistema
def login():
    print("\n✔ Vale! Identificate en el sistema...")
    email = input("Ingresa tu email: ")
    contrasena = input("Ingresa tu contraseña: ")
    usuarioLogin = (email, contrasena)
    sql = 'SELECT * FROM usuarios WHERE email = %s AND contrasena = %s'
    try:
        cursor.execute(sql, usuarioLogin)
        respuesta = cursor.fetchone()
        usuario = usuariosModel.Usuarios(
            respuesta[0], respuesta[1], respuesta[2], respuesta[3], respuesta[4])
        print("\n✔ ¡Usuario Logueado correctamente!")
        return usuario
    except:
        print("\n❌ El correo y/o contraseña son incorrectos.")
        print("Intentalo más tarde :c")
        return False

# Función para crear nota
def crearNota(usuario):
    bandera = True
    while bandera:
        print("\n✔ Ok ",usuario.nombre,"! Vamos a crear una nueva nota...")
        time.sleep(2)
        titulo = input('Ingresa el titulo de la nota: ')
        validacion = notasModel.Notas.validar(usuario.id, titulo)
        if validacion :
            bandera = False
        else:
            print('\n❌ Este titulo ya fue usado, elige otro.')
    descripcion = input('Ingresa la descripción: ')
    nota = notasModel.Notas(titulo, usuario.id, descripcion)
    # print(usuario.id)
    nota.guardar()

# Función para listar notas
def listarNotas(usuario):
    notas = notasModel.Notas.listar(usuario.id)
    time.sleep(2)
    print("\n✔ Ok ",usuario.nombre,"! Aqui tienes tus notas: \n")
    for item in notas:
        print("*****************************************")
        print(f"\n{item[2]}:")
        print(f" {item[3]}")
        print("")
        print("*****************************************")
        print("")
    time.sleep(3)

# Función para eliminar notas    
def eliminarNota(usuario):
    print("\n✔ Ok ",usuario.nombre,"! Vamos a eliminar una nota...\n")
    titulo = input('Ingresa el titulo de la nota: ')
    eliminado = notasModel.Notas.eliminar(usuario.id, titulo)
    if eliminado[0] == 0:
        print("\n❌ No se en encontro ninguna Nota con ese titulo.")
    else:
        time.sleep(2)
        print("\n✔ Su nota- ", titulo, " -ha sido eliminada con exito.")


