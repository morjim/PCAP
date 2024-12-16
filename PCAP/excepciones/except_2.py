try:
    y=1/0
#manejar dos excepciones a la vez
except (ZeroDivisionError, ArithmeticError):
    print("PROBLEMAAA al operar")

except: #excepción general
    print ("Algo ha cascao aquí...")

print ("FIN")