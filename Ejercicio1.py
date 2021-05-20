'''Escribí un programa que solicité al usuario ingresar cuatro números para luego
     mostrar el promedio de los tres.'''

#funciones 
def getPromedio(listNumeros):
    promedio=0
    ac=0
    cant=len(listNumeros)
    for x in listNumeros:
        ac+=x
    
    promedio=ac/cant
    return promedio

#main
numeros=[] 
cant=4

while len(numeros)<cant:   
    try:
        num=int(input(f"Ingrese numero{len(numeros)+1}: "))
        numeros.append(num)
    except Exception:
        print("numero incorrecto")

print("\n============resultados==========")
print("los numeros ingresados son: ", numeros)
print("El promedio es : ", getPromedio(numeros))

