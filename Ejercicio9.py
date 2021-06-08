#funciones
def calPrecio(cantidad,genero):
    listGenero={
    "salsa":56.00,
    "rock":63.00,
    "pop":87.00,
    "folclore":120.50
    } 
    return cantidad * listGenero[genero]

def calDescuento(precio,cantidad):
    if cantidad <=3:
        return 0
    if cantidad ==4:
        return precio * 0.06
    if cantidad<=10:
        return precio * 0.08
    if cantidad >10:
        return precio * 0.102  
    
def calTotal(precio,descuento):
    return precio-descuento
def getObsequio(cantidad,genero):
    if (genero=="pop" or genero=="rock") and cantidad > 6 :
        return "poster"        
    return "ninguno"

#main
print("generos: \nsalsa\npop\nrock\nfolclore")
genero=input("Ingrese el genero del disco: ")
cantidad=int(input("ingrese la cantidad: "))

precio = calPrecio(cantidad, genero)
descuento=calDescuento(precio,cantidad)
total=calTotal(precio, descuento)
obsequio=getObsequio(cantidad, genero)

print("Importe de la compra: ", precio)
print("Importe del descuento: ", descuento)
print("Importe a pagar: ", total)
print("obsequio: ", obsequio)










