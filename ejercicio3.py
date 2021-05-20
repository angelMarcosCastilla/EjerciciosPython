'''Calcular el sueldo de un empleado, ingrese los siguientes
 datos: nombre, horas de trabajo y el salario por hora. Luego incrementar el sueldo en 15%.'''


nombre=input("ingrese Su nombre: ")
horaTrabajo=int(input("ingrese su hora de trabajo: "))
salarioHora=float(input("ingrese su salario por hora: "))

porcentajeIcremento=0.15
sueldo=horaTrabajo*salarioHora
incremento=sueldo*porcentajeIcremento
sueldoTotal=sueldo+incremento;

print(f"\nhola {nombre}")
print(f"tu sueldo es: {sueldo}")
print(f"el incremento es: {incremento}")
print(f"tu sueldo total es:  {sueldoTotal}")