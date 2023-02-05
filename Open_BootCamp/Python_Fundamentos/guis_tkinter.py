import tkinter 


window = tkinter.Tk()

label1 = tkinter.Label(window, text="label1", fg ="Green", bg = "orange") # Creamos label con parámetros
#label1.pack(ipadx=50, ipady=30, expand="True") # Utilizamos la geometria pack y aplicamos atributos ipadx, ipady, expand

label1.pack(ipadx=50, ipady=30, side="left")


label2 = tkinter.Label(window, text="label2", fg = "Blue", bg = "pink")
label2.pack(ipadx=60, fill = "y", side="right")

# label3 = tkinter.Label(window, text="label3", fg = "purple", bg = "yellow")
# label3.pack(ipadx=60, ipady=33, fill="both")

window.mainloop()