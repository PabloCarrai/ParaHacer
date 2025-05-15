import os
tareas = []

def limpiarPantalla():
    os.system('clear')

def listarTareas(tareas):
    limpiarPantalla()
    print("Tareas")
    for i in range(len(tareas)):
        print(f"{i}-{tareas[i]}")


def agregarTareas(tareas):
    limpiarPantalla()
    titulo = input("Ingrese su tarea ")
    tareas.append(titulo)


def eliminarTareas():
    limpiarPantalla()
    pass


def salirPrograma():
    limpiarPantalla()
    print("Muchas gracias por usar este programa ")


def menu():
    print("Bienvenido a Para-Hacer ")
    print("Elija una opcion: ")
    print("""          
          1)Listar Tareas
          2)Agregar Tareas
          3)Eliminar Tareas          
          4)Salir del programa
          """)
    desicion = int(input("Elija una opcion (1/2/3/4)   "))
    print(f"Su eleccion {desicion}")
    if (desicion == 4):
        salirPrograma()
    elif (desicion == 1):
        listarTareas(tareas)
        menu()
    elif (desicion == 2):
        agregarTareas(tareas)
        menu()


menu()
