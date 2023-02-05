import tkinter
from tkinter import ttk
import sys

window = tkinter.Tk()

botton=tkinter.Button(window, text="Do clic")
botton.pack()

#Binding, unir evento a una accion

def saludar(event):
    print("Han hecho clic en saludar")
botton.bind('<Button-1>', saludar) # Asociamos al boton uno la funcion saludar
# el evento Double es doble clic

def saludardobleclic(event):
    print("Han hecho clic en doble clic")
botton.bind('<Double-1>', saludardobleclic) # Asociamos el doble clic a la funcion saludardobleclic


# Creamos boton salir
def salir(event):
    print("Adios!")
    window.quit()
    sys.exit(0)
botton_salir = tkinter.Button(window, text="Exit")
botton_salir.pack()
botton_salir.bind('<Button-1>',salir)

window.mainloop()