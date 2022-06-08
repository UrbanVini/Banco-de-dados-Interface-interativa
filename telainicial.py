
from tkinter import *
def tela_inicial():
    root = Tk()
    root.geometry('500x500')
    root.title("Registro AV2 ")

    label_0 = Label(root, text="Registro Turma T.I",width=20,font=("bold", 20))
    label_0.place(x=70,y=53)

    name = Label(root, text="Nome Completo",width=20,font=("bold", 10))
    name.place(x=80,y=130)

    name = Entry(root)
    name.place(x=240,y=130)

    email = Label(root, text="E-mail",width=20,font=("bold", 10))
    email.place(x=68,y=180)

    email= Entry(root)
    email.place(x=240,y=180)

    matricula= Label(root, text="Matricula",width=20,font=("bold", 10))
    matricula.place(x=70,y=230)

    matricula = Entry(root)
    matricula.place(x=240,y=230)

    curso = Label(root, text="Curso",width=20,font=("bold", 10))
    curso.place(x=70,y=280)

    curso = Entry(root)
    curso.place(x=240,y=280)

    campus = Label(root, text="Campus",width=20,font=("bold", 10))
    campus.place(x=70,y=330)

    entrada_5 = Entry(root)
    entrada_5.place(x=240,y=330)

    Button(root, text='Enviar Dados',width=20,bg='brown',fg='white').place(x=180,y=380)

    root.mainloop()
    tela_inicial()