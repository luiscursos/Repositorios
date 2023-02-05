#------------------SERIALIZACION DE DATOS-------------------------

# Convertir un objeto o cosa a una secuencia de datos que se pueda escribir en disco
# La deserelizacion es lo contrario, recuoerar el objeto del archivo
# Se serializa para guardar el estodo de un programa

import pickle

class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

j1 = Juguete("Potato", 10.5)
print(type(j1))
f = open('datos.bin','wb')  # Creamos archivo binario para guardar el objeto
# Guardamos el objeto en el archivo, 
# primero se indica el objeto 'j1' y después el archivo 'f'
pickle.dump(j1,f)           
f.close()


# Para recuperar los datos guardados

f = open('datos.bin', 'rb')
potato = pickle.load(f) # potato = a cargar el contenido que hay en f
f.close

print(type(potato))
print(potato.getNombre())