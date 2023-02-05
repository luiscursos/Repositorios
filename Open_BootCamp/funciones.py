# Cuando la misma variable esta declarada como local y como global , 
# y cuando desaparece la local y reaparece la global se denomina variable shadowing

# Si se quiere manipular una variable global dentro de una funcion, 
# se utiliza la keyword global

hoyHace = 12

def mifuncion(nombre):
    global hoyHace # modifica la variable global con el valor de la local
    hoyHace = 6.0
    print(hoyHace)

mifuncion("luca")
print(hoyHace)




# Parametros por defecto
# Regla -> Los parametros opcionales deben ser todos o los últimos.

def adivinaNombre(nombre="Paco"):
    print("tu nombre es: ",nombre)

adivinaNombre("Luis")
adivinaNombre()

def suma (a=1, b=5, c=1):
    print(a+b+c)

suma()
suma(1,1,1)
suma(a=10,b=20,c=30)



def sumaG(*args):
    resultado = 0
    for arg in args:
        resultado+=arg
    print(resultado)

sumaG(23,3,5,6,7,8)

# kwargs se utiliza para diccionarios con dos asteriscos
def sumaK(**kwargs):        # parametros con nombre, named parameters
    for key, value in kwargs.items():
        if kwargs ["coche"]== "bonito":
            return("Es bonito")
    

sumaK(vivienda="piso", coche="rojo")


def operaciones(a, b):
    return a+b, a-b, a*b, a/b   # Esto retorna una tupla


print(operaciones(2,4))
# Almacenamos los resultados del retorno en diferentes variables
sumar, resta, multi,division= operaciones(2,4)
print(sumar)
print(resta)
print(multi)
print(division)
sumando,*resto_op=operaciones(2,4)
print(sumando)
print(resto_op)



def sumador(**kwargs):
    inicial=kwargs['inicial']
    final = kwargs['final'] if 'final' in kwargs else 0 # Operador ternario

    resultado = 0
    for x in range(inicial, final +1):
        resultado +=x

    return(resultado)

print(sumador(inicial=15, final=30))
print(sumador(inicial=30))



# funcion anonima LAMBDA
# una funcion anonima se asigna la funcion normal a una variable
anonima1 = lambda:print("hola")
anonima = lambda nombre, nombre2:print("hola", nombre, "adios", nombre2)

anonima1()
anonima("pepe", "juan")
