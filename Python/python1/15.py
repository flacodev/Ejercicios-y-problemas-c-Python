#15) Escribí un programa que solicite al usuario el ingreso de un número mayor que 1 por teclado e informe si el
#número es primo o no. Nota: los números primos son los que sólo son divisibles por 1 y por sí mismos.

num=int(input("ingrese un numero mayor a 1: "))

es_primo= True
for i in range(2, num):
    if num % i == 0:
        es_primo=False
        break

if es_primo:
    print("el numero es primo")
else:
    print("el numero no es primo")