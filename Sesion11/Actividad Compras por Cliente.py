# Actividad: Compras por Cliente - Sesion 11
# Actividad: Básica

total = 0
monto = 0
monto = float(input("Ingrese el monto (0 para salir):"))

while monto != 0:
    while monto < 0:
        print("Solo se permiten valores positivos, intente de nuevo")
        monto = float(input("Ingrese el monto (0 para salir):"))
    total += monto
    monto = float(input("Ingrese el monto (0 para salir):"))

if total > 1000:
    print("\nTiene descuento del 10%\n")
    total = total * .9

print("Total es:",total)
