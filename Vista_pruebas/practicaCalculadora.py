from tkinter import *

rt = Tk()

frame = Frame(rt)

frame.pack()

operacion = ""

resultado = 0

# <Pantalla>
numeroPantalla = StringVar()

pantalla = Entry(frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")


# Pulsaciones teclado
def numeroPulsado(num):
    global operacion

    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = "suma"

    numeroPantalla.set(resultado)


def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0

# <Pantalla/>

# <Fila 1 botones>
boton7 = Button(frame, text="7", width=7, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(frame, text="8", width=7, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(frame, text="9", width=7, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDividir = Button(frame, text="/", width=7)
botonDividir.grid(row=2, column=4)
# <Fila 1 botones/>

# <Fila 2 botones>
boton4 = Button(frame, text="4", width=7, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(frame, text="5", width=7, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(frame, text="6", width=7, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMultiplicar = Button(frame, text="*", width=7)
botonMultiplicar.grid(row=3, column=4)
# <Fila 2 botones/>

# <Fila 3 botones>
boton1 = Button(frame, text="1", width=7, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(frame, text="2", width=7, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(frame, text="3", width=7, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRestar = Button(frame, text="-", width=7)
botonRestar.grid(row=4, column=4)
# <Fila 3 botones/>

# <Fila 4 botones>
boton0 = Button(frame, text="0", width=7, command=lambda: numeroPulsado("0"))
boton0.grid(row=6, column=1)
botonDot = Button(frame, text=".", width=7, command=lambda: numeroPulsado("."))
botonDot.grid(row=6, column=2)
botonIgual = Button(frame, text="=", width=7, command=lambda: el_resultado())
botonIgual.grid(row=6, column=3)
botonSumar = Button(frame, text="+", width=7, command=lambda: suma(numeroPantalla.get()))
botonSumar.grid(row=6, column=4)
# <Fila 4 botones/>


rt.mainloop()
