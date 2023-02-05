from functools import reduce

## Reduce genera un unico resultado a traves de una lista.
# Ejecuta la funcion ciclicamente sobre el resultado obtenido en la operacion anterior

def suma (a,b):
    print(f"a={a} ; b={b}")
    return a + b 

res = reduce(suma,[1,2,3,4,5])