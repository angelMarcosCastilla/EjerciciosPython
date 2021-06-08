def obtenerTarifaOrdinaria(turno):
    tarifaOrdinaria=37.00
    if turno=="t":
        return tarifaOrdinaria + 1.20
    if turno=="n":
        return tarifaOrdinaria + 1.50
    return tarifaOrdinaria

def calcularSalarioBruto(tarifaOrdinaria,horasTrabajadas):
    return horasTrabajadas * tarifaOrdinaria

def obtenerDescuento(salarioBruto,turno):
    if turno=="n":
        if salarioBruto>=2000 and salarioBruto<=5000:
            return salarioBruto * 0.15
        if salarioBruto>=8000 and salarioBruto<=10000:
            return salarioBruto * 0.17
    return 0

def calcularSalarioNeto(salarioBruto,descuento):
    return salarioBruto - descuento

#main
trabajadores=[]
ban=True

while ban:
    nombre=input("Ingrese nombres: ")
    horasTrabajadas=int(input("ingrese la cantidad de horas trabajadas: "))
    turno=input("Ingrese un turno(m=mañana,t=tarde,n=noche): ").lower()
    
    trabajador={
        "nombre":nombre,
        "turno":turno,
        "horasTrabajadas":horasTrabajadas
        }
    trabajadores.append(trabajador)
    op=input("deseas continuar S/N: ").lower()
    if(op!="s"):
        ban=False

for trabajador in trabajadores:
    tarifaOrdinaria=obtenerTarifaOrdinaria(trabajador["turno"])
    salarioBruto=calcularSalarioBruto(tarifaOrdinaria, trabajador["horasTrabajadas"])
    descuento=obtenerDescuento(salarioBruto,trabajador["turno"])
    salarioNeto=calcularSalarioNeto(salarioBruto, descuento)
    print(f"{trabajador['nombre']} su salario es:",salarioNeto)
        
        
        
        
        
        
        
        
        
        
        
        
        
