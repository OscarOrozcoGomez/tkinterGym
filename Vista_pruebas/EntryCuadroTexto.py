from tkinter import *

rt = Tk()
rt.config(bg="blue")


frame1 = Frame(rt, width=1200, height=600)
frame1.pack()


label = Label(frame1, text="Nombre")
label.grid(row=0, column=10)


cuarotxt = Entry(frame1, bg="yellow")
cuarotxt.grid(row=0, column=1)

frame2 = Frame(frame1, bg="purple")
label1 = Label(frame2, text="Label1")
label1.pack()
frame2.pack()

rt.mainloop()
