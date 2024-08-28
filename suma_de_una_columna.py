# Programa para sumar una columna de una matriz

def suma_columna (A=list, f=int, x=int)->float:

    sum_col = 0
    for wa in range (f):
        sum_col += (A[wa][x-1])

    return sum_col

if __name__ == "__main__":
    f=int(input("Ingrese la cantidad de filas que tendra la matriz A: "))
    c=int(input("Ingrese la cantidad de columnas que tendra la matriz A: "))
    
    A = []

    for wa in range (f):
        A1 = []
        for we in range (c):
            a=float(input(f"Indique cual valor ira en ({wa+1} , {we+1}): "))
            A1.append (a)
        A.append (A1)

    x=int(input("Cual columna quiere sumar: "))

suma_col = suma_columna(A,f,x)

print (f"La suma de los elementos de la {x} columna de la matriz {A} es igual a {suma_col}")