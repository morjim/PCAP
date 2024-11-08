# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''


for char in text:
    if not char.isalpha(): #si no es una cifra, pasa
        if char == ' ':
            cipher += ' '
        continue
    char = char.upper() #m-->M
    code = ord(char) + 1 #punto de código siguiente
    if code > ord('Z'):  #si rebasa el alfabeto...
        code = ord('A') #... empieza otra vez
    cipher += chr(code)

print(cipher)

#descrifrado 

descipher = ''
for char in cipher:
    if not char.isalpha():
        if char ==' ':
            descipher += ' '
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    descipher += chr(code)

print(text)