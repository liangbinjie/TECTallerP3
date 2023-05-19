from cliente import clienteExist
from variables import TABLA_MASCOTAS, LISTA_MASCOTAS
from tkinter import messagebox

def cargarMascotas():
    listaMascotas = []
    archivo = open(TABLA_MASCOTAS)
    for linea in archivo.readlines():
        listaMascotas.append(linea.replace("\n", "").split(';'))

    for mascota in listaMascotas:
        if mascota not in LISTA_MASCOTAS:
            LISTA_MASCOTAS.append(mascota)


# Funcion para buscar una mascota por id
def getMascota(idMascota):
    for mascota in LISTA_MASCOTAS:
        print(mascota)
        if mascota[1] == idMascota:
            print("YES")
            return mascota
    messagebox.showerror("Error", "No se encontro la mascota")
    return False


def addMascota(idCliente, idAnimal, nombreAnimal, tipoMascota, raza, fechaN, sexo, color, castrado, fechaUltimaVisita, win):
    # cliente exista
    # id mascota no repetido
    # NumCliente;IdAnimal;Nombre;tipomascota;raza;fechanacimiento;sexo;color; castrado; fechaultimavisita
    if clienteExist(idCliente) == False:
        messagebox.showerror("Error", "No se encontro el cliente en la base de datos")
        return 0
    if mascotaExist(idAnimal) == True:
        return 0
    fechaN = fechaN.split("-")
    fechaUltimaVisita = fechaUltimaVisita.split("-")
    nuevo = [idCliente, idAnimal, nombreAnimal, tipoMascota, raza] + fechaN + [sexo, color, castrado] + fechaUltimaVisita
    LISTA_MASCOTAS.append(nuevo)
    messagebox.showinfo("Agregado", "Mascota agregado a la base de datos")
    print(LISTA_MASCOTAS)
    win.destroy()


def mascotaExist(idMascota):
    encontrado = False

    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            encontrado = True
    
    if encontrado == True:
        messagebox.showerror("Error", "ID de mascota ya existe, ingrese otro")

    else:
        return idMascota


def consultarMascota(idMascota ,win):
    mascota = getMascota(idMascota)
    if mascota != False:
        messagebox.showinfo("Consulta de mascota", f"ID cliente: {mascota[0]}\n"+
                      f"ID mascota: {mascota[1]}\n"+
                      f"Nombre mascota: {mascota[2]}\n"+
                      f"Tipo de mascota: {mascota[3]}\n"+
                      f"Raza mascota: {mascota[4]}\n"+
                      f"Fecha nacimiento de mascota: {mascota[5]}-{mascota[6]}-{mascota[7]}\n"+
                      f"Sexo de mascota: {mascota[8]}\n"+
                      f"Color de mascota: {mascota[9]}\n"+
                      f"Castrado: {mascota[10]}\n"+
                      f"Fecha ultima visita: {mascota[11]}-{mascota[12]}-{mascota[13]}\n")
    win.destroy()

def eliminarMascotas(idMascota, win):
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            LISTA_MASCOTAS.remove(mascota)
            messagebox.showinfo("Elimiando", "La mascota ha sido eliminada")
            win.destroy()
            return LISTA_MASCOTAS
        
    messagebox.showerror("Error", "La mascota no se encontro")
    return 0

def modificarMascota(idMascota, nombre, castrado, win):
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            if nombre != "":
                mascota[2] = nombre
            if castrado != "":
                mascota[10] = castrado
            messagebox.showinfo("Modificado", "Mascota modificada")
            win.destroy()
            return LISTA_MASCOTAS
        
    messagebox.showerror("Error", "Mascota no existe")
    return 0
    