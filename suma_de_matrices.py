# Programa que hace la suma de matrices

def sum_de_matrices (A=list , B=list)->list:

    S=[]
    S1=[]

    for wa in range (f):
        for we in range (c):
            s = (A[wa][we]) + (B[wa][we])
            S1.append (s)
        S.append (S1)
        S1 = []

    return S

if __name__ == "__main__":
    c=int(input("Ingrese la cantidad de columnas que van a tener las matrices: "))
    f=int(input("Ingrese la cantidad de filas que van a tener las matrices: "))
    A=[]
    A1=[]
    B=[]
    B1=[]

    for wa in range (f):
        for we in range (c):
            a=float(input(f"Ingrese el valor que ira en ({wa+1} , {we+1}) en la matriz A: "))
            A1.append (a)
        A.append (A1)
        A1 = []

    for wa in range (f):
        for we in range (c):
            b=float(input(f"Ingrese el valor que ira en ({wa+1} , {we+1}) en la matriz B: "))
            B1.append (b)
        B.append (B1)
        B1 = []

total_matrices = sum_de_matrices(A,B)

print (f"La sumatoria de las matrices es: \n {A} + {B} = {total_matrices}")
