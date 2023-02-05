import tkinter
from tkinter import ttk
import sys

## Las GUI reaccionan siempre ante eventos, todas las librerias implementan el paradigma de alerta de eventos.
# Los eventos pueden gestionarse a traves de tkinter con la funcion callback que recibe un parametro
window=tkinter.Tk()

selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value='1', variable=selected)
r2 = ttk.Radiobutton(window, text="No", value='2', variable=selected)
r3 = ttk.Radiobutton(window, text="Quizás", value='3', variable=selected)

r1.grid(column=0, row=1, padx=5, pady=5 )
r2.grid(column=0, row=2, padx=5, pady=5 )
r3.grid(column=0, row=3, padx=5, pady=5 )


### CREAR CHECK BUTTON ###
def mifuncion():
    print ("clicado")

## Cuando seleccionamos el radiobutton se guarda en la variable(selected2) el valor del boton
selected2 = tkinter.StringVar()
checkbox=ttk.Checkbutton(window, text="Accept conditions", variable=selected2, command=mifuncion)
checkbox.grid(column=0, row=0)

window.mainloop()

