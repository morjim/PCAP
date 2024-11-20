
fecha="";
while True:
    fecha=input("Introduce tu fecha de nacimiento (en formato AAAAMMDD): ")
    if fecha.isnumeric():
        break
    print("Debes introducir una fecha en formato AAAAMMDD")

digito=0
suma=0
for i in fecha :
    suma+=int(i)

if len(str(suma))>1:
    for i in str(suma):
        digito+=int(i)
else:
    digito=suma
  
print ("Tu dígito vital es :",digito)