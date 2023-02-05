### ALL   ANY  ###


# Sirven para verificar que todas o algunas condiciones de una lista se cumplan

listA = [1==1, 2==2, 3==4]
resA = any(listA)
print(resA) #True, una condicion como minimo es True

resB = all(listA)
print(resB) # False, no se True todas las condiciones