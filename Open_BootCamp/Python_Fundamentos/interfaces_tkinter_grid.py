### --------- GEOMETRY GRID ----------###
import tkinter
from tkinter import ttk

window = tkinter.Tk()

# La geometria "grid" se ubica como en una hoja de calculo (rows & columns) 
# Entorno a las filas y columnas se colocan los objetos


# (0,0) (1,0) (2,0)
# (0,1) (1,1) (2,1)
# (0,2) (1,2) (2,2)
# (0,3) (1,3) (2,3)

# label_username    username_Entry           (2,0)
# label_password    password_Entry           (2,1)
#       (0,2)           (1,2)                (2,2)
#       (0,3)           (1,3)             login_button


# ------CONFIGURAR GRID------

# El primer numero es el indice de la columna 
# "weight" es el número de objetos en la columna
window.columnconfigure(0,weight=3)
window.columnconfigure(1,weight=3)


# Creamos etiqueta con ttk. 
# ttk aplica estetica del sistema operativo, que es más consistente que Tk



# Se aplican atributos a geometria "grid"
    # column=0 -> Indica la columna donde se posiciona el objeto
    # row=0 -> Indica fila donde se posiciona el objeto
    # sticky=tkinter.W -> Indica donde se fija la label según "Rosa de los Vientos". La W = Western
label_username = ttk.Label(window, text="Username:")
label_username.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

# Creamos entrada de texto con input box, indicando en la ventana que debe generarse
# El parametro "show='*'", sirve para ocultar el texto y que se muestren asteriscos
username_entry = ttk.Entry(window, show='*')
# Mostramos el input box username_entry
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

# El parametro "show='*'", sirve para ocultar el texto y que se muestren asteriscos
password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

# Crear un botón
login_button = ttk.Button(window, text="Reset")
login_button.grid(column=2, row=3, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()