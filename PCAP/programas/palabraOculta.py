#encuentra la palabra oculta


palabra =input("introduce la palabra a buscar: ").upper()
grupo = input("introduce el grupo de caracteres: ").upper()

contiene = True
inicio=0

for c in palabra:
    pos=grupo.find(c,inicio)

    if pos ==-1:
        contiene = False
        break
    inicio = pos + 1

if contiene:
    print ("si")
else: 
    print ("no")
        




   