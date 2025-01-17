'''
Crear una clase Empleado que modele trabajadores con un nombre y apellidos, un cargo y un salario. El salario debe ser (obligatoriamente) un atributo privado.
'''

class Empleado:
    plantilla= []
    numEmpleados=0
    def __init__(self, nombre: str, apellidos: str, cargo, salario):
        if salario <0 :
            print("El salario no puede ser negativo")
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario=salario
        Empleado.plantilla.append(self)
        Empleado.numEmpleados+=1



    def getSalario(self):
        return self.__salario
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - ({self.cargo}) - Gana:  {round(self.getSalario())}"
    



    
empleado1 = Empleado("Pepe", "Pérez", "Genio", 10000.0)
empleado2 = Empleado("Juan", "Garcia", "Genio", 10000.0)
empleado3= Empleado("Carlos", "Garcia", "Genio", 10000.0)

for empleado in Empleado.plantilla:
    print(empleado)

print(Empleado.__dict__)