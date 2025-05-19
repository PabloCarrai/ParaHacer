#!/usr/bin/env python3
#   Importamos el modulo os para limpiar la pantalla
import os
#   Tareas es una lista que va a guardar las tareas
tareas = []

#   Con esto limpio la pantalla(solo en ambiente gnu/linux)


def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def flujoAplicacion(desicion):
    print(f"Su eleccion {desicion}")
    if (desicion == 5):
        salirPrograma()
    elif (desicion == 1):
        listarTareas(tareas)
        menu()
        # listarTareas(["tareas","tareas"])
    elif (desicion == 2):
        agregarTareas(tareas)
        menu()
    elif (desicion == 3):
        eliminarTareas(tareas)
        menu()
    elif (desicion == 4):
        editarTareas(tareas)
        menu()


#   Listamos las tareas y sus indices
def listarTareas(tareas):
    limpiarPantalla()
    if (len(tareas) == 0):
        print("No hay tareas cargadas")
    else:
        print("Tareas")
        for i in range(len(tareas)):
            print(f"{i}-{tareas[i]}")


#   Editamos las tareas por si las cargamos mal


def editarTareas(tareas):
    if (len(tareas) == 0):
        print("No hay tareas para editar")
    else:
        listarTareas(tareas)
        indice = int(input("Ingrese el indice de la tarea a editar  "))
        editado = input("Ingrese la tarea correcta  ")
        tareas[indice] = editado

#   Agregamos las tareas


def agregarTareas(tareas):
    limpiarPantalla()
    titulo = input("Ingrese su tarea ")
    tareas.append(titulo)
    menu()

#   Eliminar Tareas


def eliminarTareas(tareas):
    limpiarPantalla()    
    if (len(tareas) > 0):
        listarTareas(tareas)
        eleccion = int(input("Ingresa el numero de la tarea a eliminar"))
        del tareas[eleccion]
    else:
        print("no hay tarea para eliminar")


#   Salimos del programa
def salirPrograma():
    limpiarPantalla()
    print("Muchas gracias por usar este programa ")
    print("""

▗▖  ▗▖ ▗▄▖  ▗▄▄▖    ▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖  ▗▄▄▖    ▗▖   ▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖ ▗▄▖ 
▐▛▚▖▐▌▐▌ ▐▌▐▌       ▐▌  ▐▌▐▌   ▐▛▚▞▜▌▐▌ ▐▌▐▌       ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌
▐▌ ▝▜▌▐▌ ▐▌ ▝▀▚▖    ▐▌  ▐▌▐▛▀▀▘▐▌  ▐▌▐▌ ▐▌ ▝▀▚▖    ▐▌   ▐▌ ▐▌▐▛▀▀▘▐▌▝▜▌▐▌ ▐▌
▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘     ▝▚▞▘ ▐▙▄▄▖▐▌  ▐▌▝▚▄▞▘▗▄▄▞▘    ▐▙▄▄▖▝▚▄▞▘▐▙▄▄▖▝▚▄▞▘▝▚▄▞▘


            """)

#   Menu del programa


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
    desicion = int(input(""))
    flujoAplicacion(desicion)


#   Arrancamos el programa
menu()
