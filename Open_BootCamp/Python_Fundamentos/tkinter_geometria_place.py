import tkinter
import random


### GEOMETRIA PLACE ###        POSICIONAMIENTO ABSOLUTO
# No se utiliza casi nunca


window=tkinter.Tk()

colours = ["blue", "red", "yellow", "purple", "green", "black"]


for x in range(0,10):
    color = random.randint(0, len(colours)-1)
    color2 = random.randint(0, len(colours)-1)
    label = tkinter.Label(window, text="etiqueta", bg=colours[color], fg=colours[color2])
    label.place(x=random.randint(0,100), y=random.randint(0,100))




# Creamos etiqueta con tkinter
label1 = tkinter.Label(window, text="posicionamiento absoluto", bg="blue", fg="white")
# utilizamos geometria place, indicando entre parentesis los pixeles de 'x' y de 'y'
# se mantiene fijo en la posición indicada aunque se amplie o reduzca la pantalla   
label1.place(x=10,y=50)

label2=tkinter.Label(window, text="label2", bg="red" ,fg="yellow")
# posición con parametros relativos a la pantalla, no a la ventana
# relx & rely & relwidth & anchor -> relación de aspecto
label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor="ne")




window.mainloop()