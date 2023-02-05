# La composicion dice que una clase está compuesta de otras clases
# La composición no hereda funciones, consiste en que una clase tiene una o mas instancia de otra clase
# # En la herencia una clase hereda las funciones de otra clase, pero no tiene instancias.

# Se puede combinar la herencia y la composición, siendo la seguna más elegante.





class Motor:
    tipo = "Diésel"

class Ventanas:
    cantidad = 5

    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print("El Motor es: ",c.motor.tipo)
print("Ventanas: ",c.carroceria.ventanas.cantidada)

c.carroceria.ventanas.cambiarCantidad(3)
print("Ventanas:", c.carroceria.ventanas.cantidad)