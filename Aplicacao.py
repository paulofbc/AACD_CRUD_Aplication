from GUI import *
import Backend as core
import tkinter.messagebox as tkMessageBox

app = None

# JUNÇÃO DO FRONT E DO BACK EM MÉTODOS
def view_command():
    rows = core.view()
    app.listCofres.delete(0, END)
    for r in rows:
        app.listCofres.insert(END, r)


def search_command():
    app.listCofres.delete(0, END)
    rows = core.search(app.txtRR.get(), app.txtRC.get(), app.txtIDC.get(), app.txtIDS.get(), app.txtData.get(), app.txtLocal.get())
    for r in rows:
        app.listCofres.insert(END, r)


def insert_command():
    result = tkMessageBox.askquestion('Cadastro de Cofre', 'Tem certeza que quer adicionar o cofre?', icon="warning")
    if result == 'yes':
        core.insert(app.txtRR.get(), app.txtRC.get(), app.txtIDC.get(), app.txtIDS.get(), app.txtData.get(), app.txtLocal.get())
        view_command()


def update_command():
    result = tkMessageBox.askquestion('Atualização de Cofre', 'Tem certeza que quer atualizar o cofre selecionado?', icon="warning")
    if result == 'yes':
        core.update(selected[0], app.txtRR.get(), app.txtRC.get(), app.txtIDC.get(), app.txtIDS.get(), app.txtData.get(), app.txtLocal.get())
        view_command()


def del_command():
    result = tkMessageBox.askquestion('Remoção de Cofre', 'Tem certeza que quer deletar o cofre selecionado?', icon="warning")
    if result == 'yes':
        id = selected[0]
        core.delete(id)
        view_command()


def getSelectedRow(event):
    global selected
    index = app.listCofres.curselection()[0]
    selected = app.listCofres.get(index)
    app.entRR.delete(0, END)
    app.entRR.insert(END, selected[1])
    app.entRC.delete(0, END)
    app.entRC.insert(END, selected[2])
    app.entIDC.delete(0, END)
    app.entIDC.insert(END, selected[3])
    app.entIDS.delete(0, END)
    app.entIDS.insert(END, selected[4])
    app.entData.delete(0, END)
    app.entData.insert(END, selected[5])
    app.entLocal.delete(0, END)
    app.entLocal.insert(END, selected[6])


app = Gui()

app.listCofres.bind('<<ListboxSelect>>', getSelectedRow)

app.btnViewAll.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnUpdate.configure(command=update_command)
app.btnDel.configure(command=del_command)
app.btnClose.configure(command=app.window.destroy)

app.run()