
import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
import re
import subprocess
import csv
from Bin.SQLite import *


# -----AVEC 2.0

# --- functions ---

def search_command(event=None):

    # to compare lower case
    text = e1.get().lower()

    

    if text: # search only if text is not empty
        list1.delete(0, 'end')
        for word in liststuff:
            #if word.lower().startswith(text):
            if text in word.lower():
                list1.insert('end', word)
    else:
        list1.delete(0, 'end')
        for word in liststuff:
            list1.insert('end', word)


def CurSelet(evt):
    value=str((list1.get(list1.curselection())))
    #print(value)
    View(value)
    tree.yview_moveto(0)

def datos(evt):
    global linea
    curItem = tree.focus()
    print(curItem)
    linea = tree.item(curItem)['values']
    #print(linea)
    #child_id = tree.get_children()
    #print(child_id)
    print("----linea")
    #global list2
    #list2 = linea


def View(local):

    tree.delete(*tree.get_children()) #limpiar lista
    
    #conn = sqlite3.connect("test.db")
    #cur = conn.cursor()
    cur.execute('SELECT * FROM "'+local+'"')
    rows = cur.fetchall()
    count=0
    colname=rows[1]
    tree["columns"] = colname
    tree.column('#0', width=0, stretch=0)
    
    for x in colname:
        #print(x)
        count+=1
        #print(count)
        #tree.heading(x, text=x)
        tree.column("#"+str(count), minwidth=100, width=115)
    
    for row in rows:
        #res = [str(i or '') and str(re.sub(r'\b0+(\d)', r'\1', str(i))) for i in row] #limpiar nulos e IP

        #print(row) # it print all records in the database

        
        nocolor_count = 0
        print(nocolor_count)
        with open('colores.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            
            for rowcsv in csv_reader:
                #print(rowcsv)
                #print(rowcsv[1])
                #print(rowcsv[2])
                #regexmarca = "r'\D"+rowcsv[0]+"'"
                #regexmarca = "\D"+rowcsv[0]
                #print(regexmarca)
                if re.search(r'\D%s' % rowcsv[0], str(row[0])):
                    tree.insert("", tk.END, values=row,tags=(rowcsv[1],))
                    print("yes--------")
                    nocolor_count = 1
                    print(nocolor_count)
        if nocolor_count == 0:
            tree.insert("", tk.END, values=row)
            print("No--------")

def conectuvnc(list2):
    print(list2)
    print(".....")
    IP=list2[3]
    #IP = re.sub(r'\b0+(\d)', r'\1', list2[3])
    passwd=epwd.get()
    port=eport.get()
    subprocess.Popen(r"UVNC\vncviewer.exe -autoscaling -encoding tight -compresslevel 8 -quality 3 -8greycolors -connect "+IP+":"+port+" -password "+passwd)
    #subprocess.Popen(r"UVNC\vncviewer.exe -connect "+IP+":"+port+" -quickoption 4 -password "+passwd)
    #os.system(r"UVNC\vncviewer.exe -connect "+IP+":"+port+" -quickoption 4 -password "+passwd)

def ping(list2):
    print(list2)
    print(".....")
    IP=list2[3]
    #IP = re.sub(r'\b0+(\d)', r'\1', list2[3])
    passwd=epwd.get()
    #os.system(r"UVNC\vncviewer.exe -connect "+IP+":6000 -quickoption 4 -password "+passwd)
    os.system("start cmd /c ping "+IP+" -t")

def resource_path(relative_path):
    #obtener ruta de carpeta temporal
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
# --- Busqueda avanzada ---    
def busqueda_avanzada():
    
    # GUI
    v2 = tk.Toplevel(v0)
    v2.title("Busqueda avanzada") #titulo
    v2.iconbitmap(resource_path('AVEC.ico'))
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
    e2av.bind("<Return>", lambda event: searchpos_command(e2av,treeav))
    e2av.pack(pady=2,side=LEFT)

    b2av=Button(frameav1,text="\uD83D\uDD0D", width=2, compound="center",command=lambda:searchpos_command(e2av,treeav))#boton pedir carpeta  height=2,
    b2av.config(bd=0,cursor="hand2", font=(None, 14))#,font="arial")
    b2av.pack() #,padx=20 side=LEFT

    treeav.pack(expand=1,fill=BOTH)

    bav=Button(v2,text="Selecionar", width=30, compound="center",command=lambda:seleccion(treeav))#boton pedir carpeta  height=2,
    bav.config(bg="#4c4a48",bd=0,fg="white",cursor="hand2")#,font="arial")
    bav.pack(pady=5) #,padx=20 side=LEFT

    liststuff = []
    for name in rows:
        #print(name[0])
        liststuff.insert(0, name[0])


def searchpos_command(e2av,treeav):                         #BUSCA INFORMACION EN LA BD

    # to compare lower case
    textav = e2av.get().lower()
    currentlocal=""
    # POS0390402

    treeav.delete(*treeav.get_children()) #limpiar lista
    #conn = sqlite3.connect("test.db")
    #cur = conn.cursor()



    #cur.execute('SELECT * FROM "'+local+' WHERE C1 like '+text+'"')
    if textav: # search only if text is not empty
        #list1.delete(0, 'end')
        for localav in liststuff:
            cur.execute('SELECT * FROM "'+localav+'"')
            rowsav = cur.fetchall()
            #count=0
            #largolocalav=len(localav)
            #print(largolocalav)
            #colname=rowsav[1]
            treeav["columns"] = ('#1','#2')
            treeav.column('#0', minwidth=210, width=210, stretch=0)
            treeav.column('#1', minwidth=100, width=115, stretch=0)
            treeav.column('#2', minwidth=250, width=250, stretch=0)
            """
            for x in colname:
                count+=1

                treeav.column("#"+str(count), minwidth=100, width=115)
            """
            for rowav in rowsav:
                #resav = [str(i or '') and str(re.sub(r'\b0+(\d)', r'\1', str(i))) for i in rowav]
                #resav = [str(i or '') for i in rowav] #limpiar nulos e ip
                #if str(rowav[0]).lower().startswith(textav) | str(rowav[3]).lower().startswith(textav) | str(rowav[5]).lower().startswith(textav):
                if str(textav).lower() in str(rowav[0]).lower() or textav in str(rowav[3]).lower() or textav in str(rowav[5]).lower(): #.lower().startswith(textav) | str(rowav[3]).lower().startswith(textav) | str(rowav[5]).lower().startswith(textav):
                    if currentlocal != localav:
                        currentlocal=localav
                        print("--------------------------")
                        print(localav)
                        treeav.insert("", 0, localav, text=localav,tags=('localav',), open=True)
                    print(rowav)
                    treeav.insert(localav, tk.END, text=rowav[0], values=(rowav[3],rowav[5]))

def seleccion(treeav):                                      #HACE LA SELECCION DEL UN ITEM
    curItem = treeav.focus()
    print("--------------------------")
    if treeav.parent(curItem) == "":
        padre = treeav.item(curItem)['text']
        texto = ""
        values = ""
        IP = ""
    else:
        padre = treeav.parent(curItem)
        texto = treeav.item(curItem)['text']
        values = treeav.item(curItem)['values']
        IP = values[0]
        ping_time = get_ping_time(IP)
        values.append(ping_time)

    print(padre)
    print(texto)
    print(IP)

    e1.delete(0, 'end')
    e1.insert(0, padre)
    search_command()
    View(padre)
    seleccion_focus(padre,texto,IP,ping_time)



def seleccion_focus(padre,texto,IP,ping_time):                            #TE MUESTRA LOS DATOS DEL ELEMENTO QUE SELECCIONASTE
    cur.execute('SELECT * FROM "'+padre+'"')
    rows = cur.fetchall()
    count=0
    countrow=0
    colname=rows[1]
    tree["columns"] = colname
    tree.column('#0', width=0, stretch=0)
    
    for x in colname:
        count+=1
        tree.column("#"+str(count), minwidth=100, width=115)
    
    for row in rows:
        if str(row[0]).startswith(texto) & str(row[3]).startswith(str(IP)):  
            child_id = tree.get_children()[countrow]
            tree.focus(child_id)
            tree.selection_set(child_id)
            tree.see(child_id)

        countrow+=1
    
    def get_ping_time(ip):
        response = os.popen("ping -c 1 " + ip).read()
        time_index = response.find("time=")
        if time_index != -1:
            time = response[time_index+5:time_index+9]
            return float(time)
        return None
    ping_time = get_ping_time(IP)
    if ping_time:
        print("Tiempo de ping: ", ping_time, "ms")
        values.append(ping_time) # agregar tiempo de ping como una nueva variable
        tree.item(child_id, values=values) # actualizar los valores de la fila con el nuevo tiempo de ping
    else:
        print("No se pudo obtener el tiempo de ping")


def CALculadora():
    
    # GUI
    v3 = tk.Toplevel(v0)
    v3.title("CALculadora")                         #titulo
    v3.iconbitmap(resource_path('AVEC.ico'))
    v3.geometry("275x370")                          # Cambia el tamanno de la ventana
    v3.resizable(False, False)                      # tamanno minimo de la ventana

    title_text = tk.StringVar()
    lcal = tk.Label(v3, text='Introduce los numeros del CAL')
    lcal.pack(pady=2)


    input_text = StringVar()
    global codigo
    codigo = ""
    

    btns_frame = Frame(v3, width = 230, height = 272, bg = "grey", highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    btns_frame.pack()

    input_frame = Frame(btns_frame, width = 230, height = 50, bd = 0, bg = "#fff").grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
    #input_frame.pack(side = TOP)
    input_field = Entry(btns_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 17, bd = 0, justify = RIGHT).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1) #, bg = "#eee", width = 18
    #input_field.grid(row = 0, column = 0)
    #input_field.pack(pady = 10)

    equals = Button(btns_frame, text = "CALcular", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 1, column = 0, columnspan = 3, padx = 1, pady = 1)

    seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 2, column = 0, padx = 1, pady = 1)
    eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 2, column = 1, padx = 1, pady = 1)
    nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 2, column = 2, padx = 1, pady = 1)

    four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 3, column = 0, padx = 1, pady = 1)
    five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 3, column = 1, padx = 1, pady = 1)
    six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 3, column = 2, padx = 1, pady = 1)

    one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 4, column = 0, padx = 1, pady = 1)
    two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 4, column = 1, padx = 1, pady = 1)
    three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 4, column = 2, padx = 1, pady = 1)

    zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)
    clear = Button(btns_frame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 5, column = 2, padx = 1, pady = 1)

    def btn_clear():
        global codigo
        codigo = ""
        input_text.set("")

    def btn_click(item):
        global codigo
        codigo = codigo + str(item)
        input_text.set(codigo)

    def btn_equal():
        global codigo
        #print(codigo)
        #input_text.get()
        codigo = input_text.get()
        result = int(codigo[0])*int(codigo[1])+int(codigo[3])+int(codigo[5]) 
        input_text.set(result)
        codigo = ""

    def codigo_limit(input_text):
        if len(input_text.get()) > 0:
            input_text.set(input_text.get()[:6])

    input_text.trace("w", lambda *args: codigo_limit(input_text))


def about():
    vinfo = tk.Toplevel(v0) # Tk() Es la ventana principal
    vinfo.title("About info") #titulo
    vinfo.iconbitmap(resource_path('AVEC.ico'))
    vinfo.geometry("300x100") # Cambia el tamanno de la ventana
    vinfo.resizable(False, False) # tamanno minimo de la ventana

    frameinfo=Frame(vinfo)
    frameinfo.pack(padx=5,pady=5) #padx=20,pady=10

    linfo = tk.Label(frameinfo, text="Alsea Vips Easy Connect 2.0\nDesarrollado por Javier Trijueque Pegalajar",anchor='w', justify='left')
    linfo.pack(fill='both') #, padx=20
    linfo2 = tk.Label(frameinfo, text="Esta obra está bajo una Licencia Creative Commons\nAtribución-NoComercial-SinDerivadas 4.0 Internacional.\nCC BY-NC-ND",anchor='w', justify='left', font = ('arial', 7))
    linfo2.pack(fill='both') #, padx=20

# --- main ---

con = sqlite3.connect("locales.db", check_same_thread=False)
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type ='table' order by name DESC")
rows = cur.fetchall()

# GUI
v0 = Tk()                                                                     # Tk() Es la ventana principal
v0.title("Alsea Vips Easy Connect (2.0)") #titulo
v0.iconbitmap(resource_path('AVEC.ico'))

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
menu1_1.add_command(label="Actualizar DB",command=lambda:start_exceltodb_thread(None))
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