### GESTION DE FICHEROS ###



# r -> read ->  Se abre archivo en modo lectura
# a -> append   -> Se pueden añadir datos al final del fichero
# w -> write    ->  Se sobreescriben los datos en el fichero, machacando los existentes
# x -> create   ->  Se crea el fichero si no existe
# w+    ->  lectura y escritura (rw)
# wb+   ->  Lectura y escritura binaria    
# t -> texto    -> si es texto plano se indica con t
# b -> binary   -> si es binario se indica con una b

#-----------------------------------------------------------------------------------
# La instancia f va a guardar el resultado de ejecutar la función interna open,
# trabajamos con el path indicado y con permisos 'r', de lectura

# f = open ("/etc/passwd", "r")   # open nos devuelve una clase 
# datos = f.read()    # la variabel datos guarda el resultado de ejecutar la instancia f con el método read()
# f.close()   # Cerramos el fichero y liberamos memoria
# print(datos)
#------------------------------------------------------------

#>>>>>>>>>>>>>   Ej.: read(16)      <<<<<<<<<<<<<<<<<<<<<<<<<<
# Si no quisieramos leer el fichero entero, 
# desde el método read podemos indicar el número de bytes que queremos leer

# f = open ("/etc/passwd", 'r')
# datos = f.read(16)  # Aqui limitamos el número de bytes que leemos del fichero
# f.close
# print(datos)
#--------------------------------------------


#--------------------------------------------
# Para leer un fichero linea por linea
 
# f = open ("/etc/passwd", 'r')
# # Con el método readline() leemos la primera línea,
# #  y se coloca al principio de la segunda línea
# datos = f.readline()    
# f.close()
# print(datos)

#--------------------------------------------

# leer un archivo linea por linea :

# >>>>>>>>>    Con while  <<<<<<<<<<
#--------------------------------------------
# while datos != "":
#     f = open("/etc/passwd", 'r')
#     datos = f.readline()
# f.close()

#--------------------------------------------


# >>>>>  Leer un archivo en una lista   <<<<<<<<<<<

# file = open("/etc/passwd", 'r')
# data = file.readlines()
# file.close()
# print("data",data)

#--------------------------------------------
# def main():
#     usuarios = listarUsuarios()
#     for usuario in usuarios:    # Iteramos sobre la lista usuarios
#         print(f'usuario:', usuario)

# def listarUsuarios():
#     f = open("/etc/passwd",'r')
#     datos = f.readlines()
#     f.close()

#     resultado = []            # Creamos una lista vacia donde agregaremos partes[0]
#     for linea in datos:
#         if linea [0] == '#':    # Si la linea comienza por # , continuar sin hacer nada
#             continue

#         if linea[0] == '_':     # Si la linea comienza por _ , continuar sin hacer nada
#             continue

#         partes = linea.split(':')   # Divide cada linea por el caracter que se indica entre los parantesis (:)
#         resultado.append(partes[0])
#         #print(partes[0])            # Con la lista devuelta por split(), se imprime el elemento en la posicion [0]
#     return resultado    # Devolvemos la lista aqlmacenada en resultado con las partes almacenadas

# if __name__=='__main__':
#     main()



#-------------------Escribir en fichero------------------------

# file = open("mifichero.txt",'a') # Si se indica 'w' se machaca lo que estaba escrito, con 'a' se agrega a lo existente
# file.write("datos\n")
# file.write("datos2\n")
# file.close()

#-----------------Añadir datos al fichero con una lista--------------------------

# f = open ("mifichero.txt",'w')
# f.close
# f = open("mifichero.txt",'a')
# list = [
#     'uno\n',
#     'dos\n',
#     'tres\n']
# f.writelines(list)

#-----------------------------------------------------------------------

#---------Función Escribe un fichero con una lista----------------------
# Detectamos si no tiene salto de linea y se le agrega

def escribe(fichero,datos):
    f = open(fichero,'w')

    for line in datos:  # Iteramos sobre la lista que pasamos por parametro "datos"
        if not line.endswith('\n'):
            line +='\n'
        f.write(line)  

    f.close()

list = [
    'first',
    'second',
    'third'
    ]
escribe("mifichero.txt", list)

#-----------------------------------------------------------------------



