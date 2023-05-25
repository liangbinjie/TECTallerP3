from variables import *
from pais import paisExist
from cliente import getCliente
from tkinter import *
from tkinter import messagebox
from visitas import LISTA_VISITAS
from mascota import LISTA_MASCOTAS


def getListaPaises():
    reporte = open("reportes/reportePais.txt", "w")
    salida = ""
    for pais in LISTA_PAISES:
        salida += f"Codigo: {pais[0]} | Nombre: {pais[1]}\n"
        reporte.write(f"Codigo: {pais[0]} | Nombre: {pais[1]}\n")
    messagebox.showinfo("Lista de paises", salida)

def getListaCiudadesPais(codPais, win):
    for pais in LISTA_PAISES:
        if pais[0] == codPais:
            salida = f"** Pais: {codPais} | {pais[1]} **"
            for ciudad in LISTA_CIUDADES:
                if ciudad[0] == codPais:
                    salida += f"\nCodigo ciudad: {ciudad[1]} | Nombre: {ciudad[2]}"

            reporte = open("reportes/reporteCiudades.txt", "w")
            reporte.write(salida)
            messagebox.showinfo("Ciudades de un pais", salida)
            win.destroy()
            return True
    messagebox.showerror("Error", "No se encontro el pais")
    return 0

def formCiudadesPais():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Reporte de ciudades pertenecientes a un pais")
    Label(t ,text = "Codigo de Pais").grid(row=0,column = 0)
    idPais = Entry(t)
    idPais.grid(row = 0, column = 1)
    Button(t , text="Consultar", command=lambda: getListaCiudadesPais(idPais.get(), t)).grid(row=1,column=1)


def getListaClientes():
    reporte = open("reportes/reporteClientes.txt", "w")
    salida = ""
    for clientes in LISTA_CLIENTES:
        if clientes[0] != 1:
            salida += f"\nID: {clientes[0]} | Nombre: {clientes[1]} | Direccion: {clientes[2]} | Pais: {clientes[3]} | Ciudad: {clientes[4]} | Telefono: {clientes[5]} | Fecha: {clientes[6]}-{clientes[7]}-{clientes[8]} | Descuento: {clientes[9]}% | Saldo: ${clientes[10]}\n"
            reporte.write(f"ID: {clientes[0]} | Nombre: {clientes[1]} | Direccion: {clientes[2]} | Pais: {clientes[3]} | Ciudad: {clientes[4]} | Telefono: {clientes[5]} | Fecha: {clientes[6]}-{clientes[7]}-{clientes[8]} | Descuento: {clientes[9]} | Saldo: {clientes[10]}\n")
    messagebox.showinfo("Lista de clientes", salida)

def getListaMascotasCliente(idCliente, win):
    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            bandera = 0
            salida = f"** LISTA DE MASCOTAS PARA CLIENTE ID: {idCliente} **\n"
            for mascotas in LISTA_MASCOTAS:
                if mascotas[0] == idCliente:
                    bandera = 1
                    salida += f"\nID: {mascotas[1]} | Nombre: {mascotas[2]} | Tipo: {mascotas[3]} | Raza: {mascotas[4]} | Fecha Nacimiento: {mascotas[5]}-{mascotas[6]}-{mascotas[7]} | Sexo: {mascotas[8]} | Color: {mascotas[9]} | Castrado: {mascotas[10]} | Fecha Ultima visita: {mascotas[11]}-{mascotas[12]}-{mascotas[13]}\n"
            
            if bandera == 0:
                messagebox.showwarning("", "Cliente no tiene mascotas")
            else:
                reporte = open("reportes/reporteMascotas.txt", "w")
                reporte.write(salida)
                messagebox.showinfo("Mascotas de un cliente", salida)
            win.destroy()
            return 0
    messagebox.showerror("Error", "No se encontro el cliente")
    return 0

def formMascotasCliente():
    t = Toplevel()
    t.geometry("300x150")
    t.title("Reporte de mascotas pertenecientes a un cliente")
    Label(t ,text = "Codigo de cliente").grid(row=0,column = 0)
    idCliente = Entry(t)
    idCliente.grid(row = 0, column = 1)
    Button(t , text="Consultar", command=lambda: getListaMascotasCliente(idCliente.get(), t)).grid(row=1,column=1)


def clienteMasSaldo():
    mayor = 0
    for cliente in LISTA_CLIENTES:
        if int(cliente[10]) > mayor:
            mayor = int(cliente[10])
            infoCliente = cliente
    
    archivo = open("reportes/clienteMasSaldo.txt", "w")
    archivo.write(f"El cliente con mas saldo es {infoCliente[1]} con id: {infoCliente[0]}, con saldo de ${mayor}")
    messagebox.showinfo("Ciente con mas saldo", f"ID: {infoCliente[0]} | Nombre: {infoCliente[1]} | Saldo: {infoCliente[10]}")

def clientesMasDescuento():
    mayor = 0
    for cliente in LISTA_CLIENTES:
        if int(cliente[9]) > mayor:
            mayor = int(cliente[9])
    
    archivo = open("reportes/clienteMasDescuento.txt", "w")
    archivo.write("Clientes con mayor descuento\n")
    salida = ""
    for cliente in LISTA_CLIENTES:
        if int(cliente[9]) == mayor:
            archivo.write(f"Nombre: {cliente[1]} con id: {cliente[0]}, con descuento de {mayor}%\n")
            salida += f"Nombre: {cliente[1]} con id: {cliente[0]}, con descuento de {mayor}%\n"
    messagebox.showinfo("Clientes con mayor descuento", salida)

def clientesCredito():
    listaMascotas = []
    for visita in LISTA_VISITAS:
        if visita[6] == "02":
            listaMascotas.append(visita[1])
    
    listaClientes = []
    for mascotas in listaMascotas:
        for mascota in LISTA_MASCOTAS:
            if mascotas == mascota[1]:
                if mascota[0] not in listaClientes:
                    listaClientes.append(mascota[0])
    
    reporte = open('reportes/reporteCredito.txt', "w")
    reporte.write("Lista de clientes de creditos\n")
    salida = "Lista de clientes de creditos\n"
    for cliente in listaClientes:
        reporte.write(f"ID: {cliente}\n")
        salida += f"ID: {cliente}\n"
    messagebox.showinfo("Lista de clientes de credito", salida)

def tratamientoMasUtilizado():
    mayor = 0
    for medicacion in LISTA_MEDICACION:
        if int(medicacion[7]) > mayor:
            mayor = int(medicacion[7])
            medicina = medicacion[5]
    reporte = open("reportes/tratamientoMasUtilizado.txt", "w")
    reporte.write("Tratamiento mas utilizado\n")
    reporte.write(f"ID de tratamiento mas utilizado: {medicina}")
    messagebox.showinfo("Reporte","Reporte generado")
    
            
def reportetratamientos():
    reporte = open("reportes/Tratamientostotal.txt","w")
    for tratamiento in LISTA_TRATAMIENTOS:
       reporte.write(f"{tratamiento}\n")

    messagebox.showinfo("Reporte","Reporte Hecho!")




def mascotaExist(idMascota):
    encontrado = False
    for mascota in LISTA_VISITAS:
        if mascota[1] == idMascota:
            encontrado = True
    return encontrado

def mascotaExistmed(idMascota):
    encontrado = False
    for mascota in LISTA_MEDICACION:
        if mascota[0] == idMascota:
            encontrado = True
    return encontrado

def form_reportevisitas():
    t = Toplevel()
    t.geometry("250x150")
    t.title("Formulario de reporte")
    Label(t, text= "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row=0, column=1)
    Button(t,text = "Reportar", command = lambda: reportesvisitas(idMascota.get())).grid(row = 1, column = 1)

def reportesvisitas(idanim):
    if mascotaExist(idanim) == True:
        reporte = open("reportes/Visitasdeunamascota.txt","w")
        for visita in LISTA_VISITAS:
            if visita[1]==idanim:
                reporte.write(f"{visita}\n")
    else:
        messagebox.showerror("Error","La mascota no tiene visitas o no existe")


def reportesulttratmascota(idanim):
    if mascotaExistmed(idanim) == True:
        reporte = open("reportes/ultimotratamientodeunamascota","w")
        i = len(LISTA_MEDICACION)-1
        while i>=0:
            if LISTA_MEDICACION[i][0] == idanim:
                reporte.write(f"El ultimo tratamiento del animal codigo {idanim} fue dado: {LISTA_MEDICACION[i]}")
                return messagebox.showinfo("Reporte", "Reporte realizado!")
            i=i-1
    else:    
        return messagebox.showerror("Error","La mascota no se ha medicado")

def form_ulttratmascota():
    t = Toplevel()
    t.geometry("250x150")
    t.title("Formulario de reporte")
    Label(t, text= "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row=0, column=1)
    Button(t,text = "Reportar", command = lambda: reportesulttratmascota(idMascota.get())).grid(row = 1, column = 1)

def form_tratmascota():
    t = Toplevel()
    t.geometry("250x150")
    t.title("Formulario de reporte")
    Label(t, text= "Codigo de Mascota").grid(row=0,column = 0)
    idMascota = Entry(t)
    idMascota.grid(row=0, column=1)
    Button(t,text = "Reportar", command = lambda: reportestratmascota(idMascota.get())).grid(row = 1, column = 1)

def reportestratmascota(idanim):
    if mascotaExistmed(idanim) == True:
        reporte = open("reportes/tratamientosdeunamascota","w")
        for med in LISTA_MEDICACION:
            if med[0] == idanim:
                reporte.write(f"El animal fue medicado en {med}")
        return messagebox.showinfo("Reporte", "Reporte realizado!")
    else:    
        return messagebox.showerror("Error","La mascota no se ha medicado")

