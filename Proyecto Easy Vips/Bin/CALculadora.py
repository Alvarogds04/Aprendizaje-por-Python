import tkinter as tk


def CALculadora():
    
    # GUI
    v3 = tk.Toplevel(v0)
    v3.title("CALculadora") #titulo
    v3.iconbitmap(resource_path('AVEC.ico'))
    v3.geometry("275x370") # Cambia el tamanno de la ventana
    v3.resizable(False, False) # tamanno minimo de la ventana

    title_text = tk.StringVar()
    lcal = tk.Label(v3, text='Introduce los numeros del CAL')
    lcal.pack(pady=2)
    """
    framecal1=Frame(v3)
    framecal1.pack()

    e1cal = tk.Entry(framecal1, textvariable=title_text, width=35)
    e1cal.bind("<Return>", lambda event: CALculo(int(e1cal.get())))
    e1cal.pack(pady=2,side=LEFT)

    b2cal=Button(framecal1,text="\uD83D\uDDA9", width=2, compound="center",command=lambda:CALculo(e1cal.get()))#boton pedir carpeta  height=2,
    b2cal.config(bd=0,cursor="hand2", font=(None, 32))#,font="arial")
    b2cal.pack() #,padx=20 side=LEFT
    """

    input_text = StringVar()
    global codigo
    codigo = ""
    
    """
    input_frame = Frame(v3, width = 100, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1, bg = "#fff")
    input_frame.pack(side = TOP)
    input_field = Entry(input_frame, font = ('arial', 20, 'bold'), textvariable = input_text, width = 18, bd = 0, justify = RIGHT) #, bg = "#eee"
    input_field.grid(row = 0, column = 0)
    input_field.pack(pady = 10)#
    """
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