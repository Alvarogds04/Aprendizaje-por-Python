
import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import subprocess
import csv

from Bin.about import *
from Bin.CALculadora import *
from Bin.datos import *
from Bin.resource_path import *
from Bin.Seach_and_Selection import *
from Bin.searchpos import *
from Bin.seleccion import *
from Bin.SQLite import *
from Bin.view import *
from Bin.VNC import *

# -----AVEC 2.0

# --- main ---

con = sqlite3.connect("locales.db", check_same_thread=False)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type ='table' order by name DESC")
rows = cur.fetchall()

# GUI
v0 = Tk()                                                                     # Tk() Es la ventana principal
v0.title("Alsea Vips Easy Connect (2.0)") #titulo
v0.iconbitmap(resource_path_temporal('AVEC.ico'))

#v0.config(bg="#009688") # Le da color al fondo
#v0.config(bg="#4c4a48")

v0.geometry("1200x600")                                                  # Cambia el tamaño de la ventana
v0.minsize(width=1200, height=600)                                       # tamaño minimo de la ventana

menu1 = Menu(v0)
v0.config(menu=menu1)
menu1_1 = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Herramientas", menu=menu1_1)                       #MENU SECUNDARIO
menu1_1.add_command(label="CALculadora",command=lambda:CALculadora())
menu1_1.add_command(label="VNC",command=lambda:subprocess.Popen(r"UVNC\vncviewer.exe"))
menu1_1.add_command(label="Actualizar DB",command=lambda:start_exceltodb_thread(none))
menu1.add_command(label="Info",command=lambda:about())
#menu1_2 = Menu(menu1, tearoff=0)
#menu1.add_cascade(label="Menu2", menu=menu1_2)


##///////// FRAME IZQUIERDO

frame0=Frame(v0)
frame0.pack(padx=10, pady=10, side=LEFT,fill=BOTH) #expand=1,fill=BOTH,

l1 = tk.Label(frame0, text='Buscar Local')
l1.pack(padx=20) #side=LEFT,

title_text = tk.StringVar()
e1 = tk.Entry(frame0, textvariable=title_text, width=35)
e1.bind('<KeyRelease>', search_command)
e1.pack(pady=2) #side=LEFT, padx=20 padx=5,


list1 = tk.Listbox(frame0, height=0, width=35)
list1.bind('<<ListboxSelect>>',CurSelet)
list1.pack(expand=1,fill=BOTH)

lsb = ttk.Scrollbar(list1,orient="vertical", command=list1.yview)
lsb.pack(side=RIGHT,fill=BOTH) # ,fill=Y

list1.configure(yscrollcommand=lsb.set)

b3=Button(frame0,text="Busqueda avanzada", width=30, compound="center",command=lambda: busqueda_avanzada())#boton pedir carpeta  height=2,  
b3.config(bg="#4c4a48",bd=0,fg="white",cursor="hand2")#,font="arial")
b3.pack(pady=5) #,padx=20 side=LEFT

##///////// FRAME DERECHO

frame1=Frame(v0)                        #ARBOL DE LOS LOCALES
frame1.pack(expand=1,fill=BOTH) #,padx=20,pady=10

tree = ttk.Treeview(frame1)

vsb = ttk.Scrollbar(frame1,orient="vertical", command=tree.yview)   #Desplazamiento de la pestaña vertical
vsb.pack(side=RIGHT,fill=BOTH)
hsb = ttk.Scrollbar(frame1,orient="horizontal", command=tree.xview)  #desplazamiento de la pestaña horizontal
hsb.pack(side=BOTTOM,fill=BOTH)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.bind('<<TreeviewSelect>>',datos)   #vista del arbol


tree.pack(expand=1,fill=BOTH)


##///////// FRAME DERECHO ABAJO

frame2=Frame(v0)
frame2.pack(padx=20,pady=10)

lpwd = tk.Label(frame2, text='Contraseña por defecto')
lpwd.pack(side=LEFT) #, padx=20

epwd_text = tk.StringVar()
epwd = ttk.Combobox(frame2, textvariable=epwd_text, width=30) #, show='*'
epwd.pack(side=LEFT) #side=LEFT, padx=20,padx=5,pady=2
epwd['values'] = ('passs1', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2', 'pass2') 
epwd.current(0)
epwd.pack(side=LEFT)

lport = tk.Label(frame2, text='Puerto')
lport.pack(side=LEFT,pady=10) #, padx=20

eport_text = tk.StringVar() 
eport = ttk.Combobox(frame2, width = 10,  
                            textvariable = eport_text)
# Adding combobox drop down list 
eport['values'] = ('5900', '6000') 
eport.current(0)
eport.pack(side=LEFT)

b1=Button(v0,text="Conectar", width=30, compound="center",command=lambda: conectuvnc(linea))#boton pedir carpeta  height=2,
b1.config(bg="#4c4a48",bd=0,fg="white",cursor="hand2")#,font="arial")
b1.pack(pady=5) #,padx=20 side=LEFT

b2=Button(v0,text="Ping", width=30, compound="center",command=lambda: ping(linea))#boton pedir carpeta  height=2,
b2.config(bg="#4c4a48",bd=0,fg="white",cursor="hand2")#,font="arial")
b2.pack(pady=5) #,padx=20 side=LEFT



##////// comandos

ips = []
times = []

with open('colores.csv') as csv_file:               #LEYENDA DE COLORES
    csv_reader = csv.reader(csv_file, delimiter=';')

for ip in ips:
    response = os.popen(f"ping -n 1 {ip}").read()
    if "TTL" in response:
        time = response.split("time=")[1].split("ms")[0]
        times.append(time)
    else:
        times.append("0")

with open('colores.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    lastlabelname =""
    for rowcsv in csv_reader:
        #print(rowcsv)
        #print(rowcsv[1])
        #print(rowcsv[2])

        tree.tag_configure(rowcsv[1], background=rowcsv[2], foreground="#FFFFFF")
        
        labelname = "l"+rowcsv[1]
        print(labelname)
        
        if lastlabelname != labelname :
            lastlabelname = labelname
            labelname = tk.Label(frame1, text='■', foreground=rowcsv[2]) #, background='#036235'
            labelname.pack(side=LEFT) #, padx=20
            labelname = tk.Label(frame1, text=rowcsv[1]+' |')
            labelname.pack(side=LEFT) #, padx=20
            print(lastlabelname)


liststuff = []
for name in rows:
    print(name[0])

    liststuff.insert(0, name[0])


for word in liststuff:
    list1.insert('end', word)

#list2 = []
print(liststuff)

v0.mainloop()