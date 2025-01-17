'''
Crear una clase Empleado que modele trabajadores con un nombre y apellidos, un cargo y un salario. El salario debe ser (obligatoriamente) un atributo privado.
'''

class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario=25000.50):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario=salario

    def getSalario(self):
        return self.__salario
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos} - ({self.cargo}) - Gana:  {round(self.getSalario())}'
    
listaEmpleados =[
    Empleado('Juan', 'Perez', 'Gerente', 75000.0),
    Empleado('Ana', 'Garcia', 'Secretaria', 80000.0),
    Empleado('Pedro', 'Lopez', 'Programador', 2800.0),
    Empleado('Mario', 'Rodriguez', 'Conserge', 20000.0)
]

empelados_vip=[
    empleado for empleado in listaEmpleados
    if empleado.getSalario() > 50000.0
]

for e in empelados_vip:
    print(e)

    
