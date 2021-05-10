from tkinter import *


class Gui: #FRONT-END
    window = Tk()
    window.wm_title("Programa Conta Comigo")
    window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.gif'))

    txtRR = StringVar()
    txtRC = StringVar()
    txtIDC = StringVar()
    txtIDS = StringVar()
    txtData = StringVar()
    txtLocal = StringVar()

    fonte = ("Calibri", "12")

    lblRR = Label(window, text="Responsável pelo Registro", font=fonte)
    lblRC = Label(window, text="Responsável pela Coleta", font=fonte)
    lblIDC = Label(window, text="ID do Cofre Coletado", font=fonte)
    lblIDS = Label(window, text="ID do Cofre Substituto", font=fonte)
    lblData = Label(window, text="Data do Registro", font=fonte)
    lblLocal = Label(window, text="Local de Captação do Cofre", font=fonte)

    entRR = Entry(window, textvariable=txtRR, font=fonte)
    entRC = Entry(window, textvariable=txtRC, font=fonte)
    entIDC = Entry(window, textvariable=txtIDC, font=fonte)
    entIDS = Entry(window, textvariable=txtIDS, font=fonte)
    entData = Entry(window, textvariable=txtData, font=fonte)
    entLocal = Entry(window, textvariable=txtLocal, font=fonte)

    scrolly = Scrollbar(window, orient=VERTICAL)
    scrollx = Scrollbar(window, orient=HORIZONTAL)
    listCofres = Listbox(window, width=125, font=fonte, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

    btnViewAll = Button(window, text="Ver Todos", font=("Calibri", "11"))
    btnBuscar = Button(window, text="Buscar", font=("Calibri", "11"))
    btnInserir = Button(window, text="Inserir", font=("Calibri", "11"))
    btnUpdate = Button(window, text="Atualizar Selecionado", font=("Calibri", "11"))
    btnDel = Button(window, text="Deletar Selecionado", font=("Calibri", "11"))
    btnClose = Button(window, text="Fechar", font=("Calibri", "11"))

    # SETTANDO AS POSIÇÕES NA JANELA
    lblRR.grid(row=0, column=0)
    lblRC.grid(row=1, column=0)
    lblIDC.grid(row=2, column=0)
    lblIDS.grid(row=3, column=0)
    lblData.grid(row=4, column=0)
    lblLocal.grid(row=5, column=0)
    entRR.grid(row=0, column=1, padx=50, pady=50)
    entRC.grid(row=1, column=1)
    entIDC.grid(row=2, column=1)
    entIDS.grid(row=3, column=1)
    entData.grid(row=4, column=1)
    entLocal.grid(row=5, column=1)
    listCofres.grid(row=0, column=2, rowspan=11)
    scrolly.grid(row=0, column=6, rowspan=11)
    scrollx.grid(row=11, column=2, columnspan=6)
    btnViewAll.grid(row=6, column=0, columnspan=2)
    btnBuscar.grid(row=7, column=0, columnspan=2)
    btnInserir.grid(row=8, column=0, columnspan=2)
    btnUpdate.grid(row=9, column=0, columnspan=2)
    btnDel.grid(row=10, column=0, columnspan=2)
    btnClose.grid(row=11, column=0, columnspan=2)

    scrolly.configure(command=listCofres.yview)
    scrollx.configure(command=listCofres.xview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='WE')
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()