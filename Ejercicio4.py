'''Ingresar 2 números y luego escoger la operación que se quiere
 hacer con ellos (suma, resta, multiplicación o división) y reportar el resultado.'''

#funciones
def operacion(n1,n2,op):
    if op==1:
        return n1+n2
    if op==2:
        return n1-n2
    if op==3:
        return n1*n2
    if op==4:
        return n1/n2
    
#main
print("\n1=suma\n2=resta\n3=multiplicacion\n4=division")
op=int(input("ingrese una operacion: "))
num1=int(input("ingrese numero1: "))
num2=int(input("ingrese numero2: "))

print("el resultado es : ",operacion(num1,num2,op))