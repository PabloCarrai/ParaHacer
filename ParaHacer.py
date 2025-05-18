#!/usr/bin/env python3
#   Importamos el modulo os para limpiar la pantalla
import os
#   Tareas es una lista que va a guardar las tareas
tareas = []

#   Con esto limpio la pantalla(solo en ambiente gnu/linux)


def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def volverMenu():
    volvemos = int(input("Regresamos al menu? 1=Si"))
    if (volvemos == 1):
        limpiarPantalla()
        menu()


#   Listamos las tareas y sus indices


def listarTareas(tareas):
    limpiarPantalla()
    print("Tareas")
    for i in range(len(tareas)):
        print(f"{i}-{tareas[i]}")
    volverMenu()

#   Editamos las tareas por si las cargamos mal


def editarTareas(tareas):
    listarTareas(tareas)
    indice = int(input("Ingrese el indice de la tarea a editar  "))
    editado = input("Ingrese la tarea correcta  ")
    tareas[indice] = editado

#   Agregamos las tareas


def agregarTareas(tareas):
    limpiarPantalla()
    titulo = input("Ingrese su tarea ")
    tareas.append(titulo)

#   Eliminar Tareas


def eliminarTareas(tareas):
    pass


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
    print(f"Su eleccion {desicion}")
    if (desicion == 5):
        salirPrograma()
    elif (desicion == 1):
        listarTareas(tareas)
    elif (desicion == 2):
        agregarTareas(tareas)
        volverMenu()
    elif (desicion == 3):
        eliminarTareas(tareas)
    elif (desicion == 4):
        editarTareas(tareas)
        volverMenu()


#   Arrancamos el programa
menu()
