from tkinter import *

rt = Tk()
rt.config(bg="blue")


frame1 = Frame(rt, width=1200, height=600)
frame1.pack()


label = Label(frame1, text="Nombre", )
label.grid(row=0, column=0, sticky="w")
label1 = Label(frame1, text="Apedillo")
label1.grid(row=1, column=0, sticky="w")
label2 = Label(frame1, text="Direccion de casa")
label2.grid(row=2, column=0, sticky="w")


cuarotxt = Entry(frame1, bg="yellow")
cuarotxt.grid(row=0, column=1)
cuarotxt1 = Entry(frame1, bg="yellow")
cuarotxt1.grid(row=1, column=1)
cuarotxt2 = Entry(frame1, bg="yellow")
cuarotxt2.grid(row=2, column=1)
cuarotxt2.config(show="+")


rt.mainloop()
