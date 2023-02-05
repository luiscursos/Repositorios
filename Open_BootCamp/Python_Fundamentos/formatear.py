numero = 511
texto = "quijote"
otromas = 1.2
#   %d es para formateo de numeros emteros digit)
#   %s es para string
#   %f para float
#   %r

# Existen 3 formas de formatear texto

#Primera forma (antigua)
print("El número es %d y el texto es %s y tiene %f"%(numero, texto, otromas)) # 

#Primera forma con solo un valor
print("Valor flotante %.2f"%otromas) # Se limitan decimales a dos,  .2


# Segunda forma, la habitual hasta la version Python 3.6.
print("El número es {} y el texto es {} y tiene {}".format(numero, texto, otromas)) # 

# Segunda B, trata los placeholder como un array, e indiando los index se emplazan los valores
print("El número es {0} y el texto es {2} y tiene {1}".format(numero, texto, otromas)) # 

# Segunda C, asignamos parametros nombrados
print("El número es {n1} y el texto es {texto} y tiene {otromas}".format(n1=numero, texto=texto, otromas=otromas)) # 

numero1 = 2
numero2 = 2
def suma(a,b):
    return numero1 + numero2


    ###
    ###         TERCERA Y ULTIMA OPCION         
    ###


# Tercera, Después de la version 3.6 de Python
# En los placesholder se colocan las variables y sobre ellas se pueden
# aplicar métodos de variables. Se puede utilizar funciones e invocarlas en los placeholder
print(f"El número es {suma(numero1, numero2)} y el texto es {texto.upper()} y tiene {otromas}") # 


# Las funciones str() y repr() son las representaciones textuales de las clases, 
# se invocan cuando realizamos algo con una clase.
# print(str(511)) -> Convertirmos en String el número,  <class 'str'>
#   El método str() se utiliza para una salida informal al usuario final, para hacer una descripción.
# print(repr(num)) -> El método repr() se utiliza para generar salidas de depuración y desarrollo.

# Para poder mostrar en pantalla una representación informal hay que sobrecargar el método str.
# Para realizar esta sobre carga se crea una función __str__



####  Ejemplo de sobrecarga ####


class juguete:
    nombre= ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Este método es el responsable de que se ejecute str por debajo en lenguaje informal, no técnico
    def __str__(self):  # genera salida normal, informal. El método print lo ejecuta implicitamente por debajo.
        return f"My nombre es {self.nombre} y mi precio {self.precio}"

# Para generar nuestro propio repr(), salidas tecnicas, depuracion o desarrollo
    def __repr__(self):
        return f"Potato{self.nombre},{self.precio}"
j1 = juguete("Toys", 100)
print(j1)       #   My nombre es Toys y mi precio 100 

# Con nuestro propio repr() la salida modifica los datos a estos : PotatoToys,100
print(repr(j1)) #   <__main__.juguete object at 0x7f15f2797fd0> , estos son los datos por defecto de repr()

###----tabla repr() and sts()

#   repr()  |   str()   |   Se ejecuta  |
# ----------|-----------|---------------|
#     Si    |    No     |     repr()    |
#     No    |    Si     |    Comportamiento por defecto Python -> <__main__.juguete object at 0x7f15f2797fd0>