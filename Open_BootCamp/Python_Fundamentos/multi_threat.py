
### MULTI THREAD ###

# Cuando se ejecuta multihilo tenemos que bloquear el programa 
# para que de tiempo a que se ejecute el "bloque" multihilo

import _thread
import time

def hora_actual(nombre_thread, tiempo_de_espera):
    
    count = 0
    while count < 5:
        time.sleep(tiempo_de_espera)
        count+=1
        print(f'hilo:{nombre_thread}-{time.ctime(time.time())}')

# método + (hora_actual es función paralela y 
# lo que ponemos entre paréntesis son los parámetros de la función paralela si los hubiera)
_thread.start_new_thread(hora_actual,("thread_uno",1))
_thread.start_new_thread(hora_actual,("thread_dos",2))

time.sleep(15) # suspendemos la ejecución del programa 0.1 para que de tiempo al bloque multihilo
