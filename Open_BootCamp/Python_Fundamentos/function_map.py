
### la función map aplica la funcion indicada entre parentesis a cada elemento de la lista
def cuadrado(x):
    return x*x

resultado = map(cuadrado,[1,2,3,4,5,6,7,8,9])
print(list(resultado))