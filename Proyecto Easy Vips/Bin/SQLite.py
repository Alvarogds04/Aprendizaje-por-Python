import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import re
import threading


def import_db():
    file_path = filedialog.askopenfilename(filetypes=[("DB files", "*.db")])
    if file_path:
        con = sqlite3.connect(file_path)
        return con

def create_gui():
    v1 = tk.Toplevel() # Nueva ventana
    v1.title("Importando") # Título de la ventana
    v1.geometry("300x100") # Cambia el tamaño de la ventana
    v1.resizable(False, False) # Tamaño mínimo de la ventana

    frame11 = tk.Frame(v1)
    frame11.pack(padx=20, pady=10)

    limportado = tk.Label(frame11, text="Importando: 0%")
    limportado.pack(pady=10) #, padx=20
    progressbar = ttk.Progressbar(frame11, length=200, maximum=100)
    progressbar.pack(pady=0)

    return v1, frame11, limportado, progressbar

def update_db(con, v1, frame11, limportado, progressbar):
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type ='table' order by name DESC")
    rows = cur.fetchall()
    liststuff = []
    for name in rows:
        liststuff.insert(0, name[0])
    num_tablas = len(liststuff)
    for i, word in enumerate(liststuff):
        cur.execute('SELECT rowid, * FROM "'+word+'"')
        rows = cur.fetchall()
        for row in rows:
            columnumber = 0
            res = [str(i or '') and str(re.sub(r'\b0+(\d)', r'\1', str(i))) for i in row] #limpiar nulos
            for column in row:
                if columnumber != 0:
                    cur.execute('UPDATE "'+word+'" SET C'+str(columnumber)+' = "'+str(res[columnumber])+'" WHERE rowid = "'+str(row[0])+'"')
            columnumber+=1
        porcentaje = int((i + 1) / num_tablas * 100)
        limportado["text"] = f"Importando: {porcentaje}%"
        progressbar["value"] = porcentaje
    con.commit()
    limportado["text"] = "Completado"

def exceltodb():
    con = connect_to_db()
    if con:
        v1, frame11, limportado, progressbar = create_gui()
        update_db(con, v1, frame11, limportado, progressbar)

def start_exceltodb_thread(event):
    global exceltodb_thread
    exceltodb_thread = threading.Thread(target=exceltodb)
    exceltodb_thread.daemon = True
    exceltodb_thread.start()