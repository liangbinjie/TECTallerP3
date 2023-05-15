from variables import TABLA_PAISES, LISTA_PAISES, LISTA_CIUDADES
from tkinter import messagebox

def cargarPaises():
    archivo = open(TABLA_PAISES)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for pais in salida:
        if pais not in LISTA_PAISES:
            LISTA_PAISES.append(pais)

def getPais(cod):
    for pais in LISTA_PAISES:
        if pais[0] == cod:
            return pais
    messagebox.showerror("Error", "No se encontro el pais")
    return False

def addPais(codPais, nombrePais):
    if paisExist(codPais): # validar que el pais no este repetido
        messagebox.showerror("Error", "Este pais ya existe")
        return "Codigo repetido"
    
    nuevo = [codPais, nombrePais]
    LISTA_PAISES.append(nuevo)
    messagebox.showinfo("Agregado", "Nuevo pais agregado")
    print(LISTA_PAISES)

def consultarPais(idPais):
    pais = getPais(idPais)
    if pais != False:
        messagebox.showinfo("Informacion de pais", f"Codigo pais: {pais[0]}\nNombre: {pais[1]}")
        

# funcion que retorna si un codigo de pais esta en la lista o no
def paisExist(cod):
    for pais in LISTA_PAISES:
        if pais[0] == cod:
            return True
    return False
