###  ROUND   ###

# La funcion round redondea. de .1 hasta .3 redondea al numero entero anterior 3.4 lo redondea al 3
# desde el .5 al .9 redondea al numero entero siguiente, 3.6 redondea al 4
a = 5.5
b = 4.5
c = 5.6

print(round)




###  MIN   ###

#L a funcion min devuelve el valor minimo de una lista de entrada de parametros

print(min(1,2,3,4,5,6,7,8,9))


###  POW   ###
# Elevar la potencia de un numero

print(2**2)


###   SORTED  ###
# Ordenar lista

lista = ['a', 'z', 'b', 'k']
ordenada = sorted(lista)
print(ordenada)



###  GETPASS   ###

# No mostrar datos en consola como el password
from getpass import getpass

user = input("Enter user:")
passwd = getpass("Enter passwd:")

print(f"Hola {user}, tu password es {passwd}")




###     ###
# Convertir digito a un string

secreto = 50