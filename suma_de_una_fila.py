# Programa pasa sumar una fila de una matriz

def suma_fila (A=list, c=int, x=int)->float:

    sum_fil = 0
    for wa in range (c):
        sum_fil += (A[x-1][wa])

    return sum_fil

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

    x=int(input("Cual fila quiere sumar: "))

suma_fil = suma_fila(A,c,x)

print (f"La suma de los elementos de la {x} fila de la matriz {A} es igual a {suma_fil}")