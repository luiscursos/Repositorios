### CLASES ABSTRACTAS ###

from abc import ABC, abstractclassmethod

class Animal(ABC):
    @abstractclassmethod    # es una notación
    def sonido(self):
        pass

# Una clase abstractar no la podemos instanciar, la tenemos que derivar
# Una clase abstracta sirve para definir...
# ...un conjunto de funciones comunes a otras clases


class Perro(Animal):
    def sonido(self):
        return("guau")

p = Perro()
p.sonido