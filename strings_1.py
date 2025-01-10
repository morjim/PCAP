#strings_1.py
# usar input() para la entrada de usuario:

num = int(input("introduce un número;"))

print ('Nº introducido: ', num)
print('Tipo del dato: ', type(num))


saludo= 'Hola,'
quien = "compae"
#concatenar cadenas
saludo = saludo + quien
print (saludo)

#iterar a través de la cadena
for c in saludo :
    print(c , end='')
print()
#long. de la cadena en (caracteres)
print(len(saludo))

print ('a' in 'saludo')#true
print ('at' not in 'saludo')#true5
