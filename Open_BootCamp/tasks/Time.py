from time import localtime,  strptime 

"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajo.
"""
current = localtime()[3] # 

if current >= strptime("07:00"[:2],"%H")[3]:
     print("It's time go to home")
else:

# Se convierte en entero los valores de los indices 0 y 1.
# Se formatea con strptime, el entero obtenido antes se formatea con %H, el resto de valores de struc_time se ponen por defecto
# El método strptime devuelve una tupla, extraemos el indice 3 y se resta del valor que tiene current
     work_time_left = strptime("07:00"[:2],"%H")[3]-current  
     print(work_time_left," hours left to get off work")
     
# ver:  sintaxis extendida de indexación. 


# 
