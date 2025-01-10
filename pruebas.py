'''
edad =27

if edad <18:
    print("Eres menor de edad")
elif edad <50:
    print("Eres de mediada edad")
else:
    print("Eres un viejales")
'''

'''i =1
while i <= 5:
    print(i)
    i +=1

'''

'''
for i in range (1,21,2):
    print(i)

for i in range (1,21):
    if(i %2 != 0):
        print(i)

'''
'''
numbers = [1,2,3,4,5]
numbers[0]
numbers.append("HOLA CARACOLA")
print(numbers)
numbers.insert(1, 99.99)
print (numbers)
numbers.pop()
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print (numbers)
numeros = [1 ,'a', 7.5]
numeros1=numeros.copy()
print (numeros1)
numeros = [1,5,8,9,4,0.5]
numeros.sort()
print (numeros)
numeros.find(0.5)
print (numeros)

coordenadas =(1,2,3)
x, y, z = coordenadas
print(y)
'''

customer = {
    "name": "Juan",
    "age": 25,
    "is_verified":True

}

print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
print(customer.get("type", "age"))
customer["nombre"]= "Pepito"
print(customer['name'])