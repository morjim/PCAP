#comprobar si es un palindromo

frase=input("introduce una frase:")

frase2 = frase.lower().replace(' ','')#quita los espacios

if frase == frase2[::-1]:
    print("es un palindromo")
    print (frase)
    print (frase2)
else:
    print("no es un palindromo")
    print (frase)
    print (frase2)

