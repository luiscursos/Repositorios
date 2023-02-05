class Juguete():
    _encendido = False
    _apagado = True

    def encender(self):
        self._encendido = True
        print("Se ha encendido")
        return self._encendido

    def apagar(self):
        self._apagado = True
        print("Se ha apagado")
        

    def isEncendido(self):
        if self._encendido == True:
            return ("Esta encendido")
        else:
            return ("Está apagado")


class Potato(Juguete):

    _sombrero = False

    def Put_hat(self):
        if self._sombrero == False:
            self._sombrero = True
            return ("Hat on")
        else:
            return ("The hat was already on")

    def is_the_hat_on(self):
        if self._sombrero == False:
            return ("He is not wearing a hat")
        else:
            return ("El sombrero esta puesto")


obj = Juguete()
print(obj.isEncendido())
obj.encender()
print(obj.isEncendido())


obj1 = Potato()
obj1.encender()
print(obj1.isEncendido())
print(obj1.is_the_hat_on())
obj1.Put_hat()
print(obj1.is_the_hat_on())

print(dir(obj1))
