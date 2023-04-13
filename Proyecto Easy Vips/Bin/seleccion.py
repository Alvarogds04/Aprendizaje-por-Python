import os
import tkinter as tk
from tkinter import *
import AVEC2
import sqlite3
import subprocess

def seleccion():                                      #HACE LA SELECCION DEL UN ITEM
    global padre
    curItem = AVEC2.treeav.focus()
    print("--------------------------")
    if AVEC2.treeav.parent(curItem) == "":
        padre = AVEC2.treeav.item(curItem)['text']
        texto = ""
        values = ""
        IP = ""
    else:
        padre = AVEC2.treeav.parent(curItem)
        texto = AVEC2.treeav.item(curItem)['text']
        values = AVEC2.treeav.item(curItem)['values']
        IP = values[0]
        ping_time = seleccion_focus.get_ping_time(IP)
        values.append(ping_time)
    print(padre)
    print(texto)
    print(IP)

    AVEC2.e1.delete(0, 'end')
    AVEC2.e1.insert(0, padre)
    search_command()
    AVEC2.View(padre)
    seleccion_focus(padre,texto,IP,ping_time)
    padre2=padre
    
    return padre2


def seleccion_focus(padre,texto,IP,ping_time):                            #TE MUESTRA LOS DATOS DEL ELEMENTO QUE SELECCIONASTE
    
    AVEC2.cur.execute('SELECT IP  FROM "'+ padre + "WHERE type ='TPV1'")
    rows = AVEC2.cur.fetchall()
    AVEC2.cur.execute('SELECT * FROM "'+padre+'"')
    rows = AVEC2.cur.fetchall()
    count=0
    countrow=0
    colname=rows[1]
    AVEC2.tree["columns"] = colname
    AVEC2.tree.column('#0', width=0, stretch=0)
    
    for x in colname:
        count+=1
        AVEC2.tree.column("#"+str(count), minwidth=100, width=115)
    
    for row in rows:
        if str(row[0]).startswith(texto) & str(row[3]).startswith(str(IP)):  
            child_id = AVEC2.tree.get_children()[countrow]
            AVEC2.tree.focus(child_id)
            AVEC2.tree.selection_set(child_id)
            AVEC2.tree.see(child_id)

        countrow+=1
    
    

def search_command(event=None):

    # to compare lower case
    text = AVEC2.e1.get().lower()

    

    if text: # search only if text is not empty
        AVEC2.list1.delete(0, 'end')
        for word in AVEC2.liststuff:
            #if word.lower().startswith(text):
            if text in word.lower():
                AVEC2.list1.insert('end', word)
    else:
        AVEC2.list1.delete(0, 'end')
        for word in AVEC2.liststuff:
            AVEC2.list1.insert('end', word)






