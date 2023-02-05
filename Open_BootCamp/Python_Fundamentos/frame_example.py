import tkinter
from tkinter import ttk
import sys

window =tkinter.Tk()

frame = ttk.Frame(window) 
frame["relief"] = "sunken"
label = ttk.Label(frame, text="hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

# El frame es un marco donde dentro se pueden colocar otros elementos
# En este ejemplo se coloca 
# frame se utiliza para agrupar cosas
frame.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

window.mainloop()

# Todo el codigo que estuviera debajo de esta linea no se ejecutaría
sys.exit(0)