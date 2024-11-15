# Cifrado César.
text = input("Ingresa tu mensaje: ")

cipher = ''

while True: 
    desplazamiento = int(input("Ingresa la clave (1-25): "))
    if desplazamiento in range(1, 26):
        break
    else:
        print("La clave debe estar entre 1 y 25. Intenta de nuevo.")

cipher = ''
for char in text:
    if not char.isalpha():  # si no es una letra, pasa
        if char == ' ':
            cipher += ' '
        continue
    char = char.upper()  # convertir a mayúscula
    code = ord(char) + desplazamiento  # punto de código siguiente
    if code > ord('Z'):  # si rebasa el alfabeto...
        code = ord('A')# + (code - ord('Z') - 1)  # ... empieza otra vez
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