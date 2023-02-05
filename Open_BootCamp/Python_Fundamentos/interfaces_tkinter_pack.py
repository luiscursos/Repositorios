from tkinter import Tk
import tkinter

# 1 -> Creamos Ventana
window = tkinter.Tk()

# --------------------- TENEMOS 3 GEOMETRIAS DISPONIBLES, "pack", "grid", "place" -----------------

# 3 -> Mediante widgets, colocamos objetos dentro de la ventana. 
# El primer parametro de casi todos los widgets, es indicar en que ventana lo queremos situar
# 3.1 -> Windget "label" : Sirve para crear etiquetas

# Creamos etiqueta label_saludo
label1 = tkinter.Label(window, text="label1" ,fg="purple", bg="grey" )
# Creamos etiqueta label_adios
label2 = tkinter.Label(window, text="label2", fg="pink", bg="blue")
# Creamos etiqueta label_good_morning
label3 = tkinter.Label(window, text="label3", fg="lightblue", bg="purple")

# ------------------------USO DE LA GEOMETRIA PACK------------------------------
# Aplicamos geometria pack a la etiqueta label_saludo y label_adios
# LOS PARAMETROS "ipadx" e "ipady" hacen referencia al tamaño horizontal y vertical respectivamente
# "ipad" significa inner padding y se mide desde el widget, en este caso el "Label", hacia fuera
# Parametros de la geometria pack:
#   "ipadx": establece ancho 
#   "ipady": establece alto
#   "side": indica el lado donde permanece el objeto, tiene 4 atributos 
#       #"side=left" -> El objeto se coloca al lado izquierdo
#       #"side=rigth" -> Al lado derecho
#       #"side=top" -> Arriba del todo en el centro
#       #"side=bottom" -> Abajo del todo en el centro
#   "fill": establece como expandir la etiqueta, tiene 3 atributos 
#       "y": expansion vertical. Funciona con side=left o side:right o de otra manera aplicando expand=True
#       "x": expancion horizontal
#       "both": expansion en ambas direcciones
#   "expand": expansion de objeto. Si se aplica sin fill, expande el espacio alrededor de la etiqueta. Si se aplica junto a fill, expande la etiqueta Tiene dos atributos
#       "expand=True" : aplica expansion haciendo efecto sobre el atributo fill. 
#       "expand=False" : no aplica expansion
#    
label1.pack(ipady=50, fill="x") # "fill=x" aplica sin necesidad del atributo "expand"
label2.pack(ipadx=50, fill="y",side="left") # Sin "expand=True" "fill=y" no tendría efecto 
label3.pack(ipady=50, ipadx=50,  expand=True) # Al no indicar fill, expand aplica al objeto, no a label
# 4 Para que la ventana sea visible hay que generar un loop con ella
window.mainloop()
