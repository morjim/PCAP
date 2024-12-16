
import math
x = float(input("Ingresa un número: "))
try:
    assert x >= 0.0


except AssertionError:
    print("Eres idiota poco asertivo o que, pon un numero positivo")
    exit(1)

x = math.sqrt(x)

print(x)
    