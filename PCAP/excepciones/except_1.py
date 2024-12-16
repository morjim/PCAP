'''
El orden de las excepciones importa:
    *Coloca los tipos de excepción más generales al final
    *Si no, el código para excepciones más concretas será inalcanzable
    *Prueba a cambiar el orden de las excepciones para comprobarlo.
'''

try:
    y=1/0
#excepción más concreta
except ZeroDivisionError:
    print("No se puede dividir por cero")
#excepción más abstracto/generica
except ArithmeticError:
    print ("Problema aritmético")
except: #excepción general
    print ("Algo ha cascao aquí...")

print ("FIN")