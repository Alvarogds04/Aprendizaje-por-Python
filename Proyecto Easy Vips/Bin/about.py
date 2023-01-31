from tkinter import * 
from tkinter import Tk 
from Bin.SQLite import *
import AVEC2
import resource_path

def about():
    vinfo = tk.Toplevel(AVEC2.v0) # Tk() Es la ventana principal
    vinfo.title("About info") #titulo
    vinfo.iconbitmap(resource_path.resource_path('AVEC.ico'))
    vinfo.geometry("300x100") # Cambia el tamanno de la ventana
    vinfo.resizable(False, False) # tamanno minimo de la ventana

    frameinfo=Frame(vinfo)
    frameinfo.pack(padx=5,pady=5) #padx=20,pady=10

    linfo = tk.Label(frameinfo, text="Alsea Vips Easy Connect 2.0\nDesarrollado por Javier Trijueque Pegalajar",anchor='w', justify='left')
    linfo.pack(fill='both') #, padx=20
    linfo2 = tk.Label(frameinfo, text="Esta obra está bajo una Licencia Creative Commons\nAtribución-NoComercial-SinDerivadas 4.0 Internacional.\nCC BY-NC-ND",anchor='w', justify='left', font = ('arial', 7))
    linfo2.pack(fill='both') #, padx=20