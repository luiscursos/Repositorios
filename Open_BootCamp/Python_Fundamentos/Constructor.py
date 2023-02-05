### CONSTRUCTOR ###

# Para crear un constructor se utiliza la funcion reservada __init__
# El constructor sirve para tener un  estado predeterminado de la clase
# El constructor se dispara si instanciamos una clase
class Juguete:

    def __init__(self):
        print("Estoy en el constructor de la clase Juguete")


class Dino(Juguete): # Heredando de la clase Juguete también accedemos al constructor, gracias al método super
    color = None
    nombre = None

    def __init__(self, nombre):
        #Juguete.__init__(self)  # Aqui estamos en el constructor de la clase Juguete
        super().__init__()  # El método super determina quien es la clase padre y ejecuta el método init que es el constructor
        print("Estoy en el constructor de la clase Dino()")

        self.color  = "Verde"   # Valor de color puesto por defecto
        self.nombre = nombre    # El valor de nombre se establece con el parametro que se pasa al método

    def __del__(self):  # Crear Destructor
        pass
        #print("Estoy en el destructor de la clase", self.__class__)



    def verEscamas(self):
        pass


p=Dino("Rex")
#del(p)  # Fuerza la ejecucción del destructor eliminando la variable entre paréntesis
print(p.color)
print(p.nombre)

