'''
    "raise" es equivalente a trow en java
    * Permite simular excepciones reales (p.ej. para hacer pruebas de manejo de excepciones)
    * Permite simular excepciones personalizadas (p.ej. para hacer pruebas)
'''

def mal_asusnto(n):
    #genera una excepcion de tipo división por cero
    raise ZeroDivisionError

try:
    mal_asusnto(0)
except:
    print ("Qué ha pasado??")
    exit()
print ("en fin")