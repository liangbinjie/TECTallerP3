from variables import *
from tkinter import messagebox
from pais import paisExist
from ciudad import ciudadExist

# Funcion para obtener la lista de clientes apartir del txt
def cargarClientes():
    listaClientes = []
    archivo = open(TABLA_CLIENTES)
    for linea in archivo.readlines():
        listaClientes.append(linea.replace("\n", "").split(';'))

    for cliente in listaClientes:
        bandera = 0
        for elemento in LISTA_CLIENTES:
            if cliente[0] == elemento[0]:
                bandera = 1

        if bandera == 0:
            LISTA_CLIENTES.append(cliente)

def addCliente(idCliente, nombreCliente, direccion, pais, ciudad, telefono, fecha, descuento, saldo):
    idCliente = clienteExist(idCliente)
    if idCliente == True:
        return 0
    if paisExist(pais) == False:
        messagebox.showerror("Error", "Este pais no existe en nuestra base de datos")
        return 0
    if ciudadExist(ciudad) == False:
        messagebox.showerror("Error", "Esta ciudad no existe en nuestra base de datos")
        return 0
    nuevo = [idCliente, nombreCliente, direccion, pais, ciudad, telefono] + fecha.split("-") + [descuento, saldo]
    LISTA_CLIENTES.append(nuevo)
    messagebox.showinfo("Agregado", "Cliente nuevo agregado a la base de datos")
    print(LISTA_CLIENTES)
    


# Funcion para verificar si el id del cliente existe, si no existe, retorna el valor del id
def clienteExist(idCliente):
    encontrado = False

    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            encontrado = True
    
    if encontrado == True:
        messagebox.showerror("Error", "Este ID ya existe")
        return True

    else:
        return idCliente
    
def getCliente(idCliente):
    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            return cliente
    return False

def consultarCliente(idCliente):
    cliente = getCliente(idCliente)
    if cliente != False:
        messagebox.showinfo("Consulta de cliente", f"ID: {cliente[0]}\n"+
                  f"Nombre: {cliente[1]}\n"+
                  f"Direccion: {cliente[2]}\n"+
                  f"Codigo pais: {cliente[3]}\n"+
                  f"Codigo ciudad: {cliente[4]}\n"+
                  f"Telefono: {cliente[5]}\n"+
                  f"Fecha ultima visita: {cliente[6]}-{cliente[7]}-{cliente[8]}\n"+
                  f"Porcentaje de despuesto: {cliente[9]}%\n"+
                  f"Saldo a deber: ${cliente[10]}")