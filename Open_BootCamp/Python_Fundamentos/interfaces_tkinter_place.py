###--------------------GEOMETRY PLACE--------------------###

import tkinter
from tkinter import ttk


window = tkinter.Tk()

# La geometria "place" sirve para posicionar de manera absoluta dentro de una ventana
# o de forma relativa a un elemento


label1 = tkinter.Label(window,text="Posicionamiento absoluto",bg="blue" ,fg="white")

# en place se indican las cordenadas dentro de la ventana donde queremos ubicar el objeto
label1.place(x=10, y=50)

# Los atributos "relx" y "rely" son parametros relativos a la pantalla, no a la ventana
label2=tkinter.Label(window,text="otro label",bg="black", fg="red")
# Propiedades de place:
    #relwidth -> ancho de la label
    # rely -> posicion vertical segun pantalla, medida en pixeles
    # relx -> posicion horizontal segun pantalla, medida en pixeles
    # anchor -> especifica posicion segun cruz rosa de los vientos
label2.place(relx=0.1, rely=0.2, relwidth=0.5, anchor='sw')


window.mainloop()

