#!/usr/bin/env python3
#   Importamos el modulo os para limpiar la pantalla
import os
#   Tareas es una lista que va a guardar las tareas
tareas = []


def bienvenido():
    global nombre
    nombre = input("Su nombre: ")
    print(f"""

▗▄▄▖ ▄ ▗▞▀▚▖▄▄▄▄  ▄   ▄ ▗▞▀▚▖▄▄▄▄  ▄    ▐▌ ▄▄▄  
▐▌ ▐▌▄ ▐▛▀▀▘█   █ █   █ ▐▛▀▀▘█   █ ▄    ▐▌█   █ 
▐▛▀▚▖█ ▝▚▄▄▖█   █  ▀▄▀  ▝▚▄▄▖█   █ █ ▗▞▀▜▌▀▄▄▄▀ 
▐▙▄▞▘█                             █ ▝▚▄▟▌      
                                                
                                                
                {nombre}""")


def limpiarPantalla():
    #   Con esto limpio la pantalla(solo en ambiente gnu/linux)
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """
    Esta funcion solo muestra un menu y redirige la eleccion del 
    usuario a otra aplicacion que se encarga de llamar a las funciones
    deacuerdo a lo que el usuario defina
    """
    print("""
        +-----------------------------+
        |    Bienvenido               |                
        +-----------------------------+
        | 1) Listar Tareas            | 
        | 2) Agregar Tareas           |
        | 3) Eliminar Tareas          |
        | 4) Editar Tarea             |      
        | 5) Salir del programa       |
        +-----------------------------+
        | Elija (1/2/3/4/5)           |   
        +-----------------------------+

          """)


def flujoAplicacion(opciones):
    #   Manejamos el menu y el acceso a las opciones
    if (opciones == 1):
        listarTareas(tareas)
    elif (opciones == 2):
        agregarTareas(tareas)
    elif (opciones == 3):
        eliminarTareas(tareas)
    elif (opciones == 4):
        editarTareas(tareas)


def listarTareas(tareas):
    #   Listamos las tareas y sus indices
    limpiarPantalla()
    if (len(tareas) < 1):
        print("No hay tareas cargadas")
    else:
        print("Tareas")
        for i in range(len(tareas)):
            print(f"{i}-{tareas[i]}")


def editarTareas(tareas):
    #   Editamos las tareas por si las cargamos mal
    limpiarPantalla()
    if (len(tareas) < 1):
        print("No hay tareas para editar")
    else:
        listarTareas(tareas)
        indice = int(input("Ingrese el indice de la tarea a editar  "))
        if (indice in range(len(tareas))):
            editado = input("Ingrese la tarea correcta  ")
            tareas[indice] = editado
        else:
            print("Elija un indice existente")
            editarTareas(tareas)


def agregarTareas(tareas):
    #   Agregamos las tareas
    limpiarPantalla()
    titulo = input("Ingrese su tarea ")
    tareas.append(titulo)


def eliminarTareas(tareas):
    #   Eliminar Tareas
    limpiarPantalla()
    if (len(tareas) < 1):
        print("No hay tareas por editar ")
    else:
        listarTareas(tareas)
        eleccion = int(input("Ingresa el indice de la tarea a eliminar  "))
        if (eleccion in range(len(tareas))):
            del tareas[eleccion]
        else:
            eliminarTareas(tareas)


def salirPrograma():
    #   Salimos del programa
    limpiarPantalla()
    print(f"""


▗▖  ▗▖ ▄▄▄   ▄▄▄     ▄   ▄ ▗▞▀▚▖▄▄▄▄   ▄▄▄   ▄▄▄     █ █  ▐▌▗▞▀▚▖  ▄▄▄  
▐▛▚▖▐▌█   █ ▀▄▄      █   █ ▐▛▀▀▘█ █ █ █   █ ▀▄▄      █ ▀▄▄▞▘▐▛▀▀▘ █   █ 
▐▌ ▝▜▌▀▄▄▄▀ ▄▄▄▀      ▀▄▀  ▝▚▄▄▖█   █ ▀▄▄▄▀ ▄▄▄▀     █      ▝▚▄▄▖ ▀▄▄▄▀ 
▐▌  ▐▌                                               █          ▗▄▖     
                                                               ▐▌ ▐▌    
                                                                ▝▀▜▌    
                                                               ▐▙▄▞▘  

                                                    {nombre}""")


bienvenido()

while True:
    #   Arrancamos el programa
    menu()
    opciones = int(input("Elija "))
    flujoAplicacion(opciones)
    if opciones == 5:
        break

salirPrograma()
