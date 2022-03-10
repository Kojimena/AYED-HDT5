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


env = simpy.Environment()
#Parámetros de la simulación
SIMRAM = simpy.Container(env, init =RAM, capacity=RAM)
SIMCPU = simpy.Resource(env, capacity = CPU)
ESPERA = simpy.Resource(env, capacity = 2) #Operaciones IO