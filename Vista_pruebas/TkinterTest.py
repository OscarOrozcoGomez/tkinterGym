from tkinter import *

raiz = Tk()

raiz.title("Oscar")

# ESTE ES PARA PERMITIR HACER RESIZE
#raiz.resizable(0,0)

#ESTE ES PARA PONER UN ICONO CUAL QUERAMOS
raiz.iconbitmap(r"..\\recursos\\imagenes\\iconos\\pacman.ico")

#Este es para poner una tamaño estable a la pagina.
#raiz.geometry("650x350")

#Este es para poner un color de fondo a la pantalla.
raiz.config(bg="blue")

frame = Frame()
frame1 = Frame()
frame2 = Frame()
frame3 = Frame()

frame.pack(side="left", anchor="n")
frame1.pack(side="right")
frame2.pack(side="bottom")
frame3.pack(side="top")

frame.config(width="650", height="200", bg="orange", bd=10, relief="groove", cursor="heart")
frame1.config(width="550", height="200", bg="yellow", bd=10, relief="sunken", cursor="dotbox")
frame2.config(width="450", height="200", bg="purple", cursor="hand2")
frame3.config(width="350", height="200", bg="brown", cursor="circle")


raiz.mainloop()