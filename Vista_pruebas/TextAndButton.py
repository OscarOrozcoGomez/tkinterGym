from tkinter import *

rt = Tk()
rt.config(bg="blue")


frame1 = Frame(rt, width=1200, height=600)
frame1.pack()

miNombre=StringVar()

label = Label(frame1, text="Nombre")
label.grid(row=0, column=0, sticky="w")
label1 = Label(frame1, text="Apedillo")
label1.grid(row=1, column=0, sticky="w")
label2 = Label(frame1, text="Direccion de casa")
label2.grid(row=2, column=0, sticky="w")


cuarotxt = Entry(frame1, bg="yellow", textvariable=miNombre)
cuarotxt.grid(row=0, column=1)
cuarotxt1 = Entry(frame1, bg="yellow")
cuarotxt1.grid(row=1, column=1)
cuarotxt2 = Entry(frame1, bg="yellow")
cuarotxt2.grid(row=2, column=1)
cuarotxt2.config(show="+")

comentarios = Label(frame1, text="Comentarios")
comentarios.grid(row=3, column=0, sticky="w")

cometarioTexto = Text(frame1, padx=10, pady=10, width=20, height=20)
cometarioTexto.grid(row=3, column=1)


#agregar scroll bar a un objeto
scroll = Scrollbar(frame1, command=cometarioTexto.yview)
scroll.grid(row=3, column=2, sticky="nsew")
#Este es para indicar al desplaador que se quede en donde lo dejaste y no e devuelva hasta arriva
cometarioTexto.config(yscrollcommand=scroll.set)

#metodo para el boton
def codigoBoton():
    miNombre.set("Juan")


#boton
boton = Button(rt, text="Enviar", command=codigoBoton)
boton.pack()


rt.mainloop()
