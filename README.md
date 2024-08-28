# Reto-11
### Matrices

Las matrices en programación se puede decir que son una lista que contiene una cierta cantidad de vectores, siendo así la cantidad de elementos que hay en cada vector (que por cierto, todos los vectores deben tener la misma cantidad de elementos) es equivalente a la cantidad de columnas la matriz y la cantidad de vectores está directamente relacionada con la cantidad de filas que tiene la matriz. Entonces se podría decir que este reto es similar al previo de "Arreglos y listas", y que en lo único en que varia es en la presentación de las listas.

Este reto esta compuesto de 5 puntos los cuales piden calculos matemáticos de orden matricial y cálculos de columnas o filas de una matriz definida.

### Punto 1 / Suma de matrices.
La suma de matrices consiste de tener dos matrices con las mismas dimensiones y sumar cada elemento con su correspondiente en la otra matriz.
<p align="center">
<img src="https://github.com/user-attachments/assets/b5b66a6e-a471-4e8d-95a2-80a8256faf34" />
</p
  
Por ejemplo:

<p align="center">
<img src="https://github.com/user-attachments/assets/f5302493-5993-42a2-97de-29f09ab2e04d" />
</p

Siendo así la base que tocaba seguir, la tome en cuenta para crear el siguiente programa que hace esos cálculos.
```py
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
```

Lo que nos importa aquí es el ciclo "for" que esta dentro de la definición de la función, ya que este nos ayuda a sacar todos los elementos contenidos en las matrices A y B, y luego sumarlas, para luego añadirlos a una nueva lista la cual va a tener todos los valores totales de esas sumas.

### Punto 2 / Multiplicación de matrices
