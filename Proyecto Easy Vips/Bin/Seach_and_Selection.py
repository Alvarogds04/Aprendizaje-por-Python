import tkinter as tk
from tkinter import *
from tkinter import ttk

# --- Busqueda avanzada ---    
def busqueda_avanzada():
    
    # GUI
    v2 = tk.Toplevel(v0)
    v2.title("Busqueda avanzada") #titulo
    v2.iconbitmap(resource_path('AVEC.ico'))
    v2.geometry("600x400") # Cambia el tamanno de la ventana
    v2.minsize(width=600, height=400) # tamanno minimo de la ventana

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


def searchpos_command(e2av,treeav):

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

def seleccion(treeav):
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

    print(padre)
    print(texto)
    print(IP)

    e1.delete(0, 'end')
    e1.insert(0, padre)
    search_command()
    View(padre)
    seleccion_focus(padre,texto,IP)

    #title_text = padre


def seleccion_focus(padre,texto,IP):
    """
    cur.execute('SELECT * FROM "'+padre+'" WHERE C4 ="'+str(IP)+'" AND C1 ="'+str(texto)+'"')
    

    selll = cur.fetchall()
    print("ñññññññññ")
    print(selll)
    print("ñññññññññ")
    child_id = 1
    tree.focus(child_id)
    tree.selection_set(child_id)

    """
    #tree.delete(*tree.get_children()) #limpiar lista
    cur.execute('SELECT * FROM "'+padre+'"')
    rows = cur.fetchall()
    count=0
    countrow=0
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
        #res = [str(i or '') and str(re.sub(r'\b0+(\d)', r'\1', str(i))) for i in row] #limpiar nulos
        #print(row[0]) # it print all records in the database
        #print(res)
        ####tree.insert("", tk.END, values=res)
        ### Plantilla patron: "POS0","PRT0","PPD0","UNI0","KDS0","KPT0

        # #re.match(^)

        if str(row[0]).startswith(texto) & str(row[3]).startswith(str(IP)):  #re.match(r"^[a-zA-Z]+.*",row[0]): # str(row[0]).contains('^[Pp]OS')
            print("ppppppppppppp")
            #print(row)
            child_id = tree.get_children()[countrow]
            print(child_id)
            tree.focus(child_id)
            tree.selection_set(child_id)
            tree.see(child_id)
            #tree.insert("", tk.END, values=res,tags=('starbucks',))
            print("ppppppppppppp")

        countrow+=1
    """
    global linea
    curItem = tree.focus()
    linea = tree.item(curItem)['values']
    print(linea)
    print("----linea")
    #global list2
    #list2 = linea

    """