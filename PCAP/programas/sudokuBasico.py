tablero=[]
sudoku = True
for i in range(9):
    fila = input("Introduce fila"  + str(i)+":")
    if not fila.isnumeric():
        print("Error, no es un número")
        break
    elif sorted(fila)!=list("123456789"):
        print(sorted(fila))
        print("error debe estar entre 1 y 9")
        break
    else:
        sudoku=True
        tablero.append(fila)


if sudoku:
    print("El sudoku si es válido")
else:
    print("El sudoku no es válido")

    
