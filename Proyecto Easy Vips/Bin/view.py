from tkinter import *
import re
import csv
import AVEC2


def View(local):
    AVEC2.tree.delete(*AVEC2.tree.get_children()) #limpiar lista
    AVEC2.cur.execute('SELECT * FROM "'+local+'"')
    rows = AVEC2.cur.fetchall()
    count=0
    colname=rows[1]
    AVEC2.tree["columns"] = colname
    AVEC2.tree.column('#0', width=0, stretch=0)
    
    for x in colname:
        count+=1
        AVEC2.tree.column("#"+str(count), minwidth=100, width=115)
    
    for row in rows:
        nocolor_count = 0
        print(nocolor_count)
        with open('colores.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            
            for rowcsv in csv_reader:
                if re.search(r'\D%s' % rowcsv[0], str(row[0])):
                    AVEC2.tree.insert("", AVEC2.tk.END, values=row,tags=(rowcsv[1],))
                    print("yes--------")
                    nocolor_count = 1
                    print(nocolor_count)
        if nocolor_count == 0:
            AVEC2.tree.insert("", AVEC2.tk.END, values=row)
            print("No--------")

def CurSelet(evt):
    
    value=str((AVEC2.list1.get(AVEC2.list1.curselection())))
    #print(value)
    View(value)
    AVEC2.tree.yview_moveto(0)





