from tkinter import *
#m20 e9  | m23 e9

def createPopup(master):
   
    popup = Menu(master, tearoff=0)
    popupPaises = Menu(popup)

    popupPaises.add_command(label="Insercion")
    popupPaises.add_command(label="Consultar")
    popupPaises.add_command(label="Eliminar")
    popupPaises.add_command(label="Modificar")
    popup.add_cascade(label="Paises", menu=popupPaises)

# ** FUNCION DE POPUP **
def popupm(button, modulo):
   print(modulo)
   try:         
      x = button.winfo_rootx()
      y = button.winfo_rooty()
      createPopup.tk_popup(x+128, y, 0)
   finally:
      createPopup.grab_release()