tareas = ""


def listarTareas():
    print("Las tareas son:")
    print(f"{tareas}")


def agregarTareas():
    titulo = input("Ingrese su tarea")


def eliminarTareas():
    pass


def salirPrograma():
    print("Muchas gracias por usar este programa")


def menu():
    print("Bienvenido a Para-Hacer")
    print("Elija una opcion:")
    print("""          
          1)Listar Tareas
          2)Agregar Tareas
          3)Eliminar Tareas          
          4)Salir del programa
          """)
    desicion = int(input("Elija una opcion 1/2/3"))
    print(f"Su eleccion {desicion}")
    if (desicion == 4):
        salirPrograma()
    elif (desicion == 1):
        listarTareas()
        menu()
    elif (desicion == 2):
        agregarTareas()
        menu()


menu()
