import numpy as np
import math
print("¡Bienvenido! Este programa permite aproximar el valor de la doble integral gaussiana. \nPor favor, ingresa los siguientes parámetros en valores enteros.")
print("*"*30)
area = int(input("Tamaño del área de integración (ten en cuenta que el valor 'k' que ingreses definirá la región de integración [-k,k]x[-k,k]): "))
print("*"*30)
intervalosX = int(input("Número de subintervalos en el eje X: "))
print("*"*30)
intervalosY = int(input("Número de subintervalos en el eje Y: "))
print("*"*30)
def sumaRiemannGaussiana(a, m, n):
    dx = 2*a / m
    dy = 2*a / n

    # índices i y j (empiezan en 1)
    i = np.arange(1, m+1)
    j = np.arange(1, n+1)

    # puntos de evaluación
    x = -a + (i-0.5) * dx
    y = -a + (j-0.5) * dy

    # malla bidimensional
    X, Y = np.meshgrid(x, y, indexing='ij')

    # función gaussiana
    F = np.exp(-(X**2 + Y**2))
    # suma de Riemann
    return np.sum(F) * dx * dy
resultado = sumaRiemannGaussiana(area,intervalosX,intervalosY)
print("Aproximación: ",resultado)

error = (abs(resultado - math.pi)/(math.pi))*100
print("Porcentaje de error: ",error,"%")
