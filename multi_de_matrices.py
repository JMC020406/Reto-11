# Programa que hace la multiplicación de matrices

def multi_de_matrices (A=list, B=list, fa=int, cb=int, x=int)->list:

    M = []

    for i in range(fa):
        M1 = []
        for e in range(cb):
            m = 0
            for k in range(x):
                m += A[i][k] * B[k][e]
            M1.append(m)
        M.append(M1)

    return M

if __name__ == "__main__":
    x=int(input("Número de columnas que va a tener A y filas que va a tener B: "))
    fa=int(input("Número de filas que va a tener A: "))
    cb=int(input("Número de columnas que va a tener B: ")) 
    A=[]
    B=[]

    for wa in range (fa):
        A1=[]
        for we in range (x):
            a=float(input(f"Ingrese el valor que ira en la posición ({wa+1} , {we+1}) en la matriz A: "))
            A1.append (a)
        A.append (A1)

    for wa in range (x):
        B1=[]
        for we in range (cb):
            b=float(input(f"Ingrese el valor que ira en la posición ({wa+1} , {we+1}) en la matriz B: "))
            B1.append (b)
        B.append (B1)

producto_matrices = multi_de_matrices(A,B,fa,cb,x)

print (f"El producto de las matrices es: \n {A} x {B} = {producto_matrices}")
