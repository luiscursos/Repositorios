import tkinter
import sys


window = tkinter.Tk()
lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
# Las listas hay que convertirlas a un formato soportado por tk
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=20, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

label1 = tkinter.Label(window, text="main menu",bg="blue", fg="black" )
label1.grid()
window.mainloop()
