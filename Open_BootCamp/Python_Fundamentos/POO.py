## Hay dos tipos de clase: 
#   Global     ->
#   Dinamicas  -> Se instancian las clases y se crean zonas de memoria diferentes y los cambios no afectan entre ellas
#   Estáticas  -> Comparten zona de memoria, los cambios afectan a todas las variables internas, métodos,..

# Creamos la calse Dino
# En Python por defecto todo es público(clases, funciones, métodos, TODO..)
# Por Convencción -> Si una propiedad o una funcion empieza con un guión bajo,... 
#                  ... NO se debe manipular desde fuera de la clase

class Dino:     
    encendido = False   # Propiedad de la clase
    apagado = True      # Propiedad de la clase


    def enciende(self): # Creamos una funcion
        # Para hacer referenecia a la propiedad "encendido"de la clase 
        # hay que anteponer el método "self." Si no estaría declarando una variable local
        self.encendido = True
        return self.encendido   
        

    def apaga(self):
        self.apagado = False
        return self.apagado

    
    def isEncendido(self):
        return self.encendido


# La clase se instancia creando un objeto, aquí el objeto es "d".
# Para utilizar un método de una clase primero hay que instanciar la clase
d = Dino()

print(d.enciende())
print(d.apaga())
print(d.isEncendido())



d2 = Dino()
print(d2.enciende())
print(d2.apaga())


print(dir(d))