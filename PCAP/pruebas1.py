'''saludo = "buenos dias";
subString=saludo[0:6];
print(subString);
subString1 = saludo[7:];
print(subString1);

for i in range (1,11):
   print(i**2);
    
import math
print(math.pi);
print(math.pow(10,2));

'''
'''
cuadrados =[]
for i in range (1,11):
   cuadrados.append(i**2)
print(cuadrados);

cuadrado = [i**2 for i in range(1,11)]
print(cuadrado)

incremento=[]
for i in range (1,6):
   incremento.append(i+10)
print (incremento)

saludos = "Buenos días, buenas tardes , buenas noches"
listaSaludos=saludos.split(",")
print(listaSaludos)
listaSaludosMayusc = [saludos.upper() for saludos in listaSaludos]
print(listaSaludosMayusc)
'''
''' saca los archivos del directorio, los guardo en una lista y busco los que empiezan por m'''
import os 
lista= os.listdir(".")
print(lista)
directorios = [archivo for archivo in lista if archivo.startswith("m") and archivo.endswith(".py")]
print (directorios)
