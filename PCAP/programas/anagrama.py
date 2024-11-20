text1=""
while True:
    text1 =input("Introduzca una palabra ").upper() 
    if not text1.isalpha():
        print("Error: '"+text1+ "' no es una palabra ")
        break
    else:
        text2=input("introduzca la segunda palabra: ").upper()
        if not text2.isalpha():
            print("Error: '"+text2+ "' no es una palabra")
            break
    if sorted(text1)==sorted(text2):
        print("Las palabras son anagramas " + text1 + " y " + text2)
    else:
        print("Las palabras no son anagramas " +text1 + "y"+ text2)

