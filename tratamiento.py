from variables import LISTA_TRATAMIENTOS,TABLA_TRATAMIENTOS
from tkinter import messagebox

def cargarTratamientos():
    archivo = open(TABLA_TRATAMIENTOS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for elemento in salida:
        if elemento not in LISTA_TRATAMIENTOS:
            LISTA_TRATAMIENTOS.append(elemento)


def tratamientoexist(idtratamiento):
    for tratamiento in LISTA_TRATAMIENTOS:
        if tratamiento[0] == idtratamiento:
            return True
    return False

def tratamientonum(idtratamiento):
    i=0
    while i<=len(LISTA_TRATAMIENTOS):
        if LISTA_TRATAMIENTOS[i][0] == idtratamiento:
            return i
        i=i+1
    return i


def consultartratamiento(idtratamiento):
    if tratamientoexist(idtratamiento)==True:
        numero = tratamientonum(idtratamiento)
        messagebox.showinfo("Consulta de tratamiento", f"ID de Tratamiento: {LISTA_TRATAMIENTOS[numero][0]}\n"+
                            f"Nombre: {LISTA_TRATAMIENTOS[numero][1]}\n"+
                            f"Precio unitario: {LISTA_TRATAMIENTOS[numero][2]}\n")
                            #f"Cantidad: {LISTA_TRATAMIENTOS[numero][3]}\n")
    else:
        messagebox.showerror("Error", "No se encontro el codigo de tratamiento")

def inserciontratamiento(CodigoTrat,nombre,precio,cant):
    if tratamientoexist(CodigoTrat)==True:
         messagebox.showerror("Error", "El codigo de tratamiento esta repetido")
         return "Codigo repetido"
    else:
        nuevo = [CodigoTrat,nombre,precio,cant]
        LISTA_TRATAMIENTOS.append(nuevo)
        print(LISTA_TRATAMIENTOS)

    