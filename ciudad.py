from pais import paisExist
from variables import TABLA_CIUDADES, LISTA_CIUDADES
from tkinter import messagebox

# Funcion para cargar el listado de las ciudades del txt
def cargarCiudad():
    archivo = open(TABLA_CIUDADES)
    lista = []
    for linea in archivo.readlines():
        lista.append(linea.replace("\n", "").split(";"))

    for ciudad in lista:
        bandera = 0
        for elemento in LISTA_CIUDADES:
            if ciudad[1] == elemento[1]:
                bandera = 1
        if bandera == 0:
            LISTA_CIUDADES.append(ciudad)

# Funcion para obtener ciudad, pasando como parametro su codigo ciduad, retorna una lista
def getCiudad(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return ciudad
    messagebox.showerror("Error", "No se encontro la ciudad")
    return False
            
# Funcion para agregar una nueva ciudad
def addCiudad(codPais, codCiudad, nombre, win):
    if paisExist(codPais) == False: # si el pais no existe
        messagebox.showerror("Error", "Este pais no se encuentra en nuestra base de datos, ingrese otro")
        return 0
    if ciudadExist(codCiudad) == True: # si la ciudad existe
        messagebox.showerror("Error", "Esta ciudad ya existe en la base de datos, intente con otro")
        return 0
    nuevo = [codPais, codCiudad, nombre]
    LISTA_CIUDADES.append(nuevo)
    messagebox.showinfo("Agregado", "Nueva ciudad agregada")
    win.destroy()

def consultarCiudad(codCiudad, win):
    ciudad = getCiudad(codCiudad)
    if ciudad != False:
        messagebox.showinfo("Consulta de Ciudad", f"Codigo Pais: {ciudad[0]}\nCodigo Ciudad: {ciudad[1]}\nNombre Ciudad {ciudad[2]}")
    print(LISTA_CIUDADES)
    win.destroy()

# Funcion para verificar que ciudad exista
def ciudadExist(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return True
    return False


def eliminarCiudad(codCiudad, win):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            LISTA_CIUDADES.remove(ciudad)
            messagebox.showinfo("Eliminado", "Ciudad eliminada")
            win.destroy()
            return LISTA_CIUDADES
    messagebox.showerror("Error", 'Ciudad no encontrada')
    return 0


def modificarCiudad(idCiudad, nombre, win):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == idCiudad:
            ciudad[2] = nombre
            messagebox.showinfo("Error", "El nombre de la ciudad ha sido modificado")
            win.destroy()
            return LISTA_CIUDADES
    messagebox.showerror("Error", "No se encontro la ciudad")
    return 0