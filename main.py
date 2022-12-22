# Importamos las funciones principales
from utilidades import funciones

# Importamos la función time para dar una mejor experiencia de usuario
import time

# Variable para guardar la información del usuario
usuario = None

# Función que ejecuta el programa
def ejecutar():
    bandera = True
    while bandera:
        # opcion = input("Acciones disponibles:\n - Registro\n - Login\n").replace(" ", "").lower()  ---> Opcion de texto
        print("\n----------------------------------------\n")
        print("   ¡BIENVENIDO AL PROGRAMA DE NOTAS!\n")
        print("----------------------------------------")
        print("Acciones disponibles:\n   1- Registro\n   2- Login\n")
        opcion = input("¿Qué quieres hacer?: ")
        if opcion == "1":
            funciones.registro()
            time.sleep(2)
            continue
        elif opcion == "2":
            usuario = funciones.login()
            if usuario:
                bandera = False
        else:
            print("\n❌ Tu opción no ha sido encontrada.")
    bandera = True
    while bandera:
        time.sleep(2)
        print("\nBienvenido ",usuario.nombre," te has registrado en el sistema.\n")
        print('      Acciones disponibles: ')
        print('      1. Crear nota  \n      2. Mostrar Notas  \n      3. Eliminar nota  \n      4. Salir ')
        opcion = input('\n¿Qué quieres hacer?: ')
        if opcion == "1":
            funciones.crearNota(usuario)
        elif opcion == "2":
            funciones.listarNotas(usuario)
        elif opcion == "3":
            funciones.eliminarNota(usuario)
        elif opcion == "4":
            print("\n✔ Gracias ", usuario.nombre ," por utilizar el programa. Hasta pronto!!")
            bandera = False
        else:
            print("\n❌ Tu opción no ha sido encontrada.")
# TODO
# Validación de emailTODO

# Ejecutamos como archivo principal
if __name__ == "__main__":
    ejecutar() 