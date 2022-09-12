# Actividad: Función Cuadrática - Sesion 11
# Actividad: Básica
from cmath import sqrt

def f_cuadratica(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print("X1: ",x1)
    print("X2: ",x2)
    return x1,x2

print("Programa que calcula la función cuadratica")
a = float(input("\nIngrese valor de a: "))
b = float(input("\nIngrese valor de b: "))
c = float(input("\nIngrese valor de c: "))

f_cuadratica(a,b,c)

