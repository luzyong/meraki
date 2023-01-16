from views.mainConfiguration import Configuracion
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


root = Tk()

root.geometry("800x500")
root.resizable(width=False, height=False)
root.wm_title("VOSEDA NETWORKS -- Meraki Client")
root.iconbitmap("views/isotipo_voseda_color.ico")
configuracion = Configuracion(root)

root.mainloop()