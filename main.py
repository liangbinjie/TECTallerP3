from TecnoPets import App
from tkinter import *

def main():
    root = Tk()
    app = App()
    app.ventanaPrincipal()
    root.resizable(False, False)
    root.geometry("880x620")
    root.mainloop()

if __name__ == '__main__':
    main()
