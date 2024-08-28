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

### Punto 2 / Multiplicación entre matrices.
Este ejercicio es un poco más complejo ya que la información que toca procesar y organizar es mucho mayor. Con eso me refiero a que en la multiplicación entre matrices toca tomar dos matrices las cuales compartan una dimensión en común, pero que no sea la misma (si una tiene 2 filas la otra deberia tener 2 columnas para poder hacer el calculo). Seguido de eso se toman las dimensiones que son distintas y se organizan de tal forma que se pueda hacer una sumatoria de los productos resultantes de multiplicar los elemetos de las filas o columnas.

<p align="center">
<img src="https://github.com/user-attachments/assets/3f707834-665c-49e8-b906-979e1664ffac"
" />
</p

Por ejemplo:

<p align="center">
<img src="https://github.com/user-attachments/assets/467b1c5d-46f2-4905-bd7d-3d3128037b3e"
" />
</p

Y algo peculiar de la naturaleza de este cálculo es que no cumple la propiedad conmutativa, pero si la distributiva y la modular.

Con esta información me aventure a crear el siguiente código para solucionar este tedioso proceso más fácilmente.
```py
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
```

En este programa como se puede apreciar se contienen 3 ciclos "for" dentro de la función, pues eso se debe a la naturaleza de este calculo, el cual requiere hacer multiples multiplicaciones de los elementos de las matrices para luego sumarlos. Entonces los ciclos nos ayudan nuevamente a pasar por todos los elementos y la parte siguiente nos ayuda a llevar a cabo la sumatoria de los productos de los elementos que se vayan llamando. El resto del código es para cerar las matrices y mostrar los resultados obtenidos (algo que me falto aclarar en el anterior punto).

### Punto 3 / Matriz transpuesta.
A comparación del punto previo esta es más fácil ya que no son cálculos tediosos, es básicamente rotar la matriz con respecto a una diagonal que va de la parte superior derecha hacia abajo con un comportamiento decreciente. Se podría decir que es como ver la matriz con una simetría de eje.

Matriz original:
<p align="center">
<img src="https://github.com/user-attachments/assets/719b3744-766e-4c47-a5e7-9a171cefc075"
" />
</p

Matriz transpuesta:
<p align="center">
<img src="https://github.com/user-attachments/assets/0c4a44b3-2c1e-42d1-abdb-3f159f6cb2b3"
" />
</p

Siendo este el programa que hice para replicar esa transformación de las matrices.
```py
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
```
Como se puede apreciar el código es MUY similar al de los previos puntos del reto, y si eso se debe a que otra vez use la misma estructura para contruir la matriz y para llamar a los elementos dentro de esta. Pero lo que nos importa nuevamente está en la función, la cual hace que los elementos de la matriz A sean llamados pero con unos indices invertidos a los que deberia tener en el orden natural de la matriz original. Eso permite que al anexar los elementos a una matriz nueva esta quede como la matriz transpuesta de la original.

### Punto 4 y 5 / Suma de una fila o columna determianda de una matriz.
Estos dos puntos al ser tan similares los incluire en la misma explicación, además de que esto no tiene mucho misterio a comparación de esos 3 puntos previos los cuales son para sentarse un rato y entender como realmente funcionan.

#### Suma de una columna.
```py
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
```

#### Suma de una fila.
```py
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
```

Compuestas de 3 partes estos programas en lo único que difieren es en la posición que toma x (columna o fila la cual se quiere sumar), el cual esta dentro del ciclo "for" el cual nos ayuda a llamar a todos los valores de esa fila o columna para luego sumarlos. El resto del código es creación de la matriz y la impresión de los resultados.

Todas las imagenes e información fue sacada de Wikipedia:

https://es.wikipedia.org/wiki/Adición_matricial

https://es.wikipedia.org/wiki/Multiplicación_de_matrices

https://es.wikipedia.org/wiki/Matriz_transpuesta
