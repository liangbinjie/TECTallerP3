from tkinter import *
from ._forms import formulario_insercionpais

def popupLugares(self, btn):
    self.popup = Menu(self.master, tearoff=0)
    self.popupPaises = Menu(self.popup)
    self.popupPaises.add_command(label="Insercion", command= lambda: formulario_insercionpais(self))
    self.popupPaises.add_command(label="Consultar")
    self.popupPaises.add_command(label="Eliminar")
    self.popupPaises.add_command(label="Modificar")
    self.popup.add_cascade(label="Paises", menu=self.popupPaises)
    self.popupCiudades = Menu(self.popup)
    self.popupCiudades.add_command(label="Insercion")
    self.popupCiudades.add_command(label="Consultar")
    self.popupCiudades.add_command(label="Eliminar")
    self.popupCiudades.add_command(label="Modificar")
    self.popup.add_cascade(label="Ciudades", menu=self.popupCiudades)

    try:         
        x = btn.winfo_rootx()
        y = btn.winfo_rooty()
        self.popup.tk_popup(x+128, y, 0)
    finally:
        self.popup.grab_release()