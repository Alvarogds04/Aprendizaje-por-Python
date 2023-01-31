
import tkinter as tk
from tkinter import *
from Bin.SQLite import *
import AVEC2


# --- Busqueda avanzada ---    


def busqueda_avanzada():
    
    # GUI
    v2 = tk.Toplevel(AVEC2.v0)
    v2.title("Busqueda avanzada") #titulo
    v2.iconbitmap(AVEC2.resource_path('AVEC.ico'))
    v2.geometry("600x400") # Cambia el tamaño de la ventana
    v2.minsize(width=600, height=400) # tamaño minimo de la ventana

    title_text = tk.StringVar()
    lav = tk.Label(v2, text='Busqueda por Nombre | IP | Tipo')
    lav.pack(pady=2)

    frameav1=Frame(v2)
    frameav1.pack()

    frameav2=Frame(v2)
    frameav2.pack(expand=1,fill=BOTH) #,padx=20,pady=10

    treeav = ttk.Treeview(frameav2)

    vsbav = ttk.Scrollbar(frameav2,orient="vertical", command=treeav.yview)
    vsbav.pack(side=RIGHT,fill=BOTH)
    hsbav = ttk.Scrollbar(frameav2,orient="horizontal", command=treeav.xview)
    hsbav.pack(side=BOTTOM,fill=BOTH)

    treeav.configure(yscrollcommand=vsbav.set, xscrollcommand=hsbav.set)
    treeav.tag_configure('localav', background='#4c4a48', foreground="#FFFFFF")
    #tree.bind('<<TreeviewSelect>>',datos)
    e2av = tk.Entry(frameav1, textvariable=title_text, width=35)
    e2av.bind("<Return>", lambda event: AVEC2.searchpos_command(e2av,treeav))
    e2av.pack(pady=2,side=LEFT)

    b2av=Button(frameav1,text="\uD83D\uDD0D", width=2, compound="center",command=lambda:AVEC2.searchpos_command(e2av,treeav))#boton pedir carpeta  height=2,
    b2av.config(bd=0,cursor="hand2", font=(None, 14))#,font="arial")
    b2av.pack() #,padx=20 side=LEFT

    treeav.pack(expand=1,fill=BOTH)

    bav=Button(v2,text="Selecionar", width=30, compound="center",command=lambda:seleccion(treeav))#boton pedir carpeta  height=2,
    bav.config(bg="#4c4a48",bd=0,fg="white",cursor="hand2")#,font="arial")
    bav.pack(pady=5) #,padx=20 side=LEFT

    liststuff = []
    for name in AVEC2.rows:
        #print(name[0])
        liststuff.insert(0, name[0])



