'''Elabore un algoritmo que permita calcular el área de un triángulo.'''
#funciones
def calcularArea(b,h):
    return (b*h)/2

#main
base=float(input("ingrese la base: "))
altura=float(input("ingrese la altura: "))

print("El area es: ", calcularArea(base, altura))