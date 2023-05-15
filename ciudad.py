from pais import paisExist
from variables import TABLA_CIUDADES, LISTA_CIUDADES
from tkinter import messagebox

# Funcion para cargar el listado de las ciudades del txt
def cargarCiudad():
    archivo = open(TABLA_CIUDADES)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for ciudad in salida:
        if ciudad not in LISTA_CIUDADES:
            LISTA_CIUDADES.append(ciudad)


# Funcion para obtener ciudad, pasando como parametro su codigo ciduad, retorna una lista
def getCiudad(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return ciudad
    messagebox.showerror("Error", "No se encontro la ciudad")
    return False
            
# Funcion para agregar una nueva ciudad
def addCiudad(codPais, codCiudad, nombre):
    if paisExist(codPais) == False: # si el pais no existe
        messagebox.showerror("Error", "Este pais no se encuentra en nuestra base de datos, ingrese otro")
        return 0
    if ciudadExist(codCiudad) == True: # si la ciudad existe
        messagebox.showerror("Error", "Esta ciudad ya existe en la base de datos, intente con otro")
        return 0
    nuevo = [codPais, codCiudad, nombre]
    LISTA_CIUDADES.append(nuevo)
    messagebox.showinfo("Agregado", "Nueva ciudad agregada")

def consultarCiudad(codCiudad):
    ciudad = getCiudad(codCiudad)
    if ciudad != False:
        messagebox.showinfo("Consulta de Ciudad", f"Codigo Pais: {ciudad[0]}\nCodigo Ciudad: {ciudad[1]}\nNombre Ciudad {ciudad[2]}")
    print(LISTA_CIUDADES)

# Funcion para verificar que ciudad exista
def ciudadExist(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return True
    return False




