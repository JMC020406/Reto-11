# Programa de una matriz transpuesta

def trans_de_matriz (A=list, f=int, c=int)->list:

    At = []

    for wa in range (c):
        At1 = []
        for we in range (f):
            at = (A[we][wa])
            At1.append (at)
        At.append (At1)

    return At

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

print ("Matriz original: ")
for fila in A:
    print (fila)

print ("Matriz transpuesta: ")
for fila in (trans_de_matriz(A,f,c)):
    print (fila)