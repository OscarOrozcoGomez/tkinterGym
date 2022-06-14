from tkinter import *

rt = Tk()

frm = Frame(rt, width=500, height=400)

frm.pack()

label1 = Label(frm, text="Hola perros", fg="red", font=("Comic Sans MS", 60))

#label1.pack()

# Este metodo es para localizar el label en algun lugar en relacion a X y Y
label1.place(x=100, y=200)

rt.mainloop()