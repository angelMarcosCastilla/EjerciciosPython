'''5.	Diseñe un algoritmo que lea tres números y determine el número mayor.'''

num1=int(input("ingrese numero1: "))
num2=int(input("ingrese numero2: "))
num3=int(input("ingrese numero3: "))

mayor=num1
if(num2>mayor):
    mayor=num2
if(num3>mayor):
    mayor=num3

print(f"numero mayor es :{mayor}")

#otra manera de resolver es usar max
#print(max(num1, num2, num3))