#Universidad Del Valle de Guatemala
#Algoritmos y Estructura de Datos
#Creadora: Jimena Hernández carné: 21199
#Viernes 11 de Marzo de 2022

#Módulos que deben ser importados
import simpy
import random
import statistics 

RANDOM_SEED = 20 #Semilla

RAM = 100 #Ram total

CPU = 1 #Un proceso por unidad de tiempo

PROCESOS =25 #Cantidad de procesos iniciales

INTERVALO=10 #Intervalo de catidad de procesos totales

INSTRUCCIONES = 3 #Instrucciones por minuto

#lista de tiempos para los cálculos
lista_tiempos=[]
total_time=0

def Generador( nomproceso,env, procesoram, instotales, tprocesos, velocity):
    #Variables globales https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html
    global total_time
    global lista_tiempos
    
#NEW(PROCESOS NUEVOS)
    yield env.timeout(tprocesos)
    print('\n(ESTADO: new) %s, Solicita %d de RAM en tiempo: %5.1f' %  (nomproceso, procesoram, env.now)) #
    tiempo_ingreso = env.now   
#READY(LISTO PARA SER ACEPTADO)
    yield SIMRAM.get(procesoram)
    print('\n(ESTADO: READY) %s, aceptada la solicitud %d de RAM en tiempo: %5.1f' %  (nomproceso, procesoram, env.now))

    ins_terminadas=0 #contador de instrucciones terminadas.

    while (ins_terminadas < instotales):
        with SIMCPU.request() as rq1:
            yield rq1
#Si la cant de instrucciones es mayor a la velocidad se reducen a la velocidad del mismo
            if (instotales - ins_terminadas) >= velocity:
                ninstrucciones = velocity
            else:
                ninstrucciones = (instotales - ins_terminadas) 
            print('\n(ESTADO: READY) %s, CPU ejecutará %d instrucciones en  tiempo: %5.1f' %  (nomproceso, ninstrucciones, env.now))
            yield env.timeout(ninstrucciones/velocity)

            ins_terminadas+= ninstrucciones
            print('\n(ESTADO: TERMINATED) %s, Instrucciones terminadas: %d tiempo: %5.1f' % (nomproceso, ins_terminadas, env.now)) 

#Se generá un número random entre 1 y 2, si es 1 pasa a WAITING y hace OPERACIONES IO.
#Si necesitará hacer I/O operations se hace un request
            cont = random.randint(1,2)
            if(cont == 1 and ins_terminadas < instotales):
                with ESPERA.request() as req2:
                    yield req2
                    yield env.timeout(1)
                print('\n(ESTADO: WAITING %s, en operacioness I/O tiempo: %5.1f ' % (nomproceso,env.now))

#Ejecución del proceso
    yield SIMRAM.put(memoriaRam)
    print('\n(ESTADO: TERMINATED) %s  RAM: %d' % (nomproceso, memoriaRam))
#El tiempo total
    total_time += (env.now - tiempo_ingreso)
#Añadir tiempos a lista de tiempos para uso de estadísticas
    lista_tiempos.append(env.now - tiempo_ingreso)

#Simpy environmet. 
# Setup and start the simulation 
print('----------------------------SIMULACION DES----------------------------')
random.seed(RANDOM_SEED)

env = simpy.Environment()
#Parámetros de la simulación
SIMRAM = simpy.Container(env, init =RAM, capacity=RAM)
SIMCPU = simpy.Resource(env, capacity = CPU)
ESPERA = simpy.Resource(env, capacity = 2) #Operaciones IO

for i in range(PROCESOS):
    ins = random.randint(1,10)
    memoriaRam = random.randint(1, 10)
    Tproceso = random.expovariate(1.0/INTERVALO)
    env.process(Generador('Proceso #%d' %i, env, memoriaRam, ins, Tproceso, INSTRUCCIONES))
#Se inicia la simulación, se detendrá hasta que se acaben los procesos
env.run()