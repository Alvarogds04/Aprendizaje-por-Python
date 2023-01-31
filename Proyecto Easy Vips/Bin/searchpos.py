import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
from Bin.SQLite import *
import AVEC2


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
        for localav in AVEC2.liststuff:
            AVEC2.cur.execute('SELECT * FROM "'+localav+'"')
            rowsav = AVEC2.cur.fetchall()
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