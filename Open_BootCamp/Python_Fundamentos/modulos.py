### MODULOS ###

# Los Módulos es un ficher en un hdd con sentencias en python y... 
# ...con extension en .py


import sys
# Agregar ruta al path para indicar un lugar donde estén los módulos
#sys.path.append("path/of/modules")

import pprint
pprint.pprint(sys.path)

import operaciones
from operators import sumar
import operators.sumar

def main():
    print(operaciones.como_me_llamo())
    res = operaciones.resta(200,2)
    sum = operaciones.suma(1,200)
    op = operaciones.Operador()
    print(op.multiplicador(4,2))

    print("El resultado de la resta es ",res, ", y el de la suma es ", sum)

    print(operators.sumar.sumar(234,567))

    mp = operators.sumar.multiplicador()
    print(mp.multiplica(12,54))

print(operaciones.como_me_llamo())


if __name__=='__main__':
    main()