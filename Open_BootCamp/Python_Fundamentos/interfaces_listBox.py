import tkinter

window = tkinter.Tk()
lista =["Windows", "MacOS", "Linux", "OS/2", "MsDOS", "BeOS", "AmigaOS"]
# Hay que importar stringVar y covertir la lista para que la lista sea compatible con listbox
lista_items = tkinter.StringVar(value=lista)
listBox=tkinter.Listbox(window, height=15, listvariable=lista_items)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

listBox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()