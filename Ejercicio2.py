'''Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte
una cantidad distinta. Obtener el porcentaje que cada uno invierte con respecto a 
la cantidad total invertida'''

#funciones 
def getPorcentaje(cant,total):
    porcentaje= (cant*100)/total
    return porcentaje

def showPerson(listPerson):
    for person in listPerson:
        print(f"{person['name']} ha invertido {person['cantidad']} ===> {person['porcentaje']}%")
    
#main
cantPerson=3;
inversores=[]
total=0

for x in range(1,cantPerson+1):
    name=input("ingrese su nombre: ")
    cantidad=input("ingrese una cantidad a invertir: ")
    
    while(cantidad.isdigit()== False):
         cantidad=input("ingrese una cantidad a invertir: ")
    
    cantidad=int(cantidad)
    person={"name":name,"cantidad":cantidad}
    total=total+cantidad        
    inversores.append(person)

for i in range(len(inversores)):
   porcentaje=getPorcentaje(inversores[i]["cantidad"],total)
   inversores[i]["porcentaje"]=porcentaje

showPerson(inversores)    
    