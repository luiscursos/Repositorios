
"""
> Mayor que
>= Mayor o igual que
== Exactamente igual
< Menor que
<= Menor o igual que


--------AND------------

True and True = True
True and False = False
False and True = False
False and False = False

---------OR------------

True or True = True
True or False = True
False or True = True
False or False = False

----------XOR------------
Sólo será cierto en el caso de que uno de los dos sea falso
True ^ True = False
True ^ False = True
False ^ True = True
False ^ False = False


"""
a = 5
b = 6
c = 0

result = (a > b and c < 7)
print(result)


# AND -> El resultado será True cuando todas sean True
print("True and True", True and True)       # True
print("True and False", True and False)     # False 
print("False and True", False and True)     # False
print("False and False", False and False)   # False

# OR -> Una de las dos debe ser True para que de resultado True
print("True or True", True or True)        # True
print("True or False", True or False)      # True
print("False or True", False or True)      # True
print("False or False", False or False)    # False

# XOR -> Debe existir una condiciona False para que el resultado sea True
print("True xor True", True ^ True)         # False
print("True xor False", True ^ False)       # True
print("False xor True", False ^ True)       # True
print("False xor False", False ^ False)     # False


a = 1
b = 6
c = 7

result = (a>=5 or c>7)
print(result)

# El condicional IF sólo se ejecutará si la condición es True.
# Si tenemos varias condiciones que se cumplen, solo se ejecutará la primera
# la parte else es opcional

if a ==1:
    print("a es igual que 5")
elif a >= 6:
    print("a es mayor o igual que 6")
else:
    print("Fin de IF")


# Bucle while
# Mientras la condicion sea True, ejecuta las sentencias del bloque

contador = 0
while contador < 15:
    if contador % 2 == 0:
        print(contador, "es un número par")
    if contador == 5:
        break
    contador +=1
print("outing of while")


# Bucle for

"""
for valor in cosa:
    acciones
"""

lista = [1,2,3,4,5]
lista2 = ["hola", "mensaje", "adios"]

# for valor_actual in lista:
#     print(valor_actual)

# for numero in range(5,10):
#         print(numero)    

longitud = len(lista)

for numero in range(longitud):
    print(lista[numero])

for palabra in lista2:
    if palabra == "mensaje":
        print ("I found the word", palabra)
        break

if "mensaje" not in lista:
    print("no hay mensaje")


lista3 = [3,4,1,2,5]
print(sorted(lista3))
lista_reverse = sorted(lista3, reverse =True)
print(lista_reverse)


### TIpo sWitch ###

### MATCH  ###

valor = 5

match valor:
    case 1:
        print("Valor es 1")
        
    case 2:
        print("Valor es 2")
        
    case 3:
        print("Valor es 3")
        
    case 4:
        print("Valor es 5")
        
    case 5:
        print("Valor es 5")
        
for palagra in lista2:
    if palabra=="mensaje":
        print("Encontrada")
        break
else:
    print("No encontrado")