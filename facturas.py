from tkinter import *
from tkinter import ttk, messagebox
from variables import LISTA_TRATAMIENTOS, LISTA_CLIENTES, LISTA_MASCOTAS

productos = []

def form_factura():
    import datetime
    current_time = datetime.datetime.now()
    t = Toplevel()
    t.geometry("300x300")
    t.title("Formulario de Factura")
    nF = f"{current_time.year}{current_time.month}{current_time.day}{current_time.hour}{current_time.minute}"
    Label(t, text=nF).grid(row=0, column=1)
    Label(t ,text = "ID Cliente").grid(row = 1,column = 0)
    idCliente = Entry(t)
    idCliente.grid(row=1, column=1)
    Label(t, text="ID Mascota").grid(row=2, column=0)
    idMascota = Entry(t)
    idMascota.grid(row=2, column=1)
    Label(t, text="Medicamento").grid(row=3, column=0)
    combo = ttk.Combobox(t,
    state="readonly",
    values=medicamentos()
    )
    combo.grid(row=3, column=1)
    Button(t, text="Agregar", command=lambda: agregar_producto(combo.get())).grid(row=3, column=2)
    Label(t, text="Subtotal").grid(row=4, column=0)
    Button(t, text="Ver subtotal", command=getSaldo).grid(row=4, column=1)
    cb = IntVar()
    descuento = Checkbutton(t, text="Descuento?", variable=cb, onvalue=1, offvalue=0).grid(row=5, column=0)
    Label(t, text="Forma de pago").grid(row=6, column=0)
    formaPago = ttk.Combobox(t,
    state="readonly",
    values=["01", "02"]
    )
    formaPago.grid(row=6, column=1)
    Button(t, text="Facturar", command=lambda: facturar(nF, idCliente.get(), idMascota.get(), productos, getSaldo2(), 1, formaPago.get())).grid(row=7, column=1)


def medicamentos():
    lista = []
    for medicamento in LISTA_TRATAMIENTOS:
        lista.append(medicamento[1])
    return lista

def agregar_producto(medicamento):
    bandera = 0
    for i in range(len(productos)):
        if productos[i][0] == medicamento:
            bandera = 1
            index = i
    if bandera == 1:
        productos[index][1] += 1
    else:
        productos.append([medicamento, 1])
    # print(productos)

def getSaldo():
    saldo = 0
    for med in productos:
        for tratamiento in LISTA_TRATAMIENTOS:
            if tratamiento[1] == med[0]:
                saldo += int(med[1])*int(tratamiento[2])
    messagebox.showinfo("Subtotal", f"Subtotal de la factura: ${saldo}")
    return saldo

def getSaldo2():
    saldo = 0
    for med in productos:
        for tratamiento in LISTA_TRATAMIENTOS:
            if tratamiento[1] == med[0]:
                saldo += int(med[1])*int(tratamiento[2])
    return saldo


def facturar(nF, idCliente, idMascota, productos, subtotal, descuento, formaPago):
    encontrado = 0
    subO = subtotal
    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            nombreC = cliente[1]
            if descuento == 1:
                subtotal = str(int(subtotal) - (int(subtotal) * (int(cliente[9])/100)))
            if formaPago == "02":
                cliente[10] = str(int(cliente[10]) + int(subtotal))
            encontrado = 1
    if encontrado == 0:
        return 0
    encontrado = 0
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            nombreM = mascota[2]
            encontrado = 1
    if encontrado == 0:
        return 0
    compra = ""
    for med in productos:
        for trat in LISTA_TRATAMIENTOS:
            if trat[1] == med[0]:
                compra += f"Medicamento: {med[0]} | Cant: {med[1]} | Precio Uni: {trat[2]}\n"
                # nueva_cant = int(trat[1]) - int(med[1])
                # if nueva_cant < 0:
                #     return 0
                # else:
                #     trat[1] = str(nueva_cant)
    
    print(f"Factura {nF}\nCliente: {nombreC, idCliente}\nMascota: {nombreM, idMascota}\nCompra:\n{compra}\nSubtotal: {subO}\nDescuento: {descuento}\nForma pago: {formaPago}\nTotal: {subtotal}")
    with open(f"facturas/{nF}.txt", "w") as f:
        f.write(f"Factura {nF}\nCliente: {nombreC, idCliente}\nMascota: {nombreM, idMascota}\nCompra:\n{compra}\nSubtotal: {subO}\nDescuento: {descuento}\nForma pago: {formaPago}\nTotal: {subtotal}")






