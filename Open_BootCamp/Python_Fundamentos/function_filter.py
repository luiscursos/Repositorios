# Filter aplica una funcion a todos los elementos de una lista. 
# Esa funcion debe devolver True o False. 
# Si es True, filter guarda ese valor, si es False no 
numeros = [1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2 == 0:
        return True
    return False

resultado = filter(lambda x:x%2==0,numeros)
print(list(resultado))