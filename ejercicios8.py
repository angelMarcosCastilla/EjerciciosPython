'''Diseñe un algoritmo que verifique si la cantidad de dígitos ingresados de un DNI es 
correcta o no (el DNI tiene 8 dígitos).'''

def validarDni(dni):
    if dni.isdigit()==False or len(dni)!=8:
        return "DNI no valido"
    if(len(dni)==8):
        return "DNI valido"
    
    
dni=input("ingrese su numero de DNI: ")
print(validarDni(dni))
