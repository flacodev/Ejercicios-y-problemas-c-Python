#4) Escribí un programa que solicite el ingreso de un número entero y, si el número leído es par, imprima la leyenda
#'El número es PAR'. En caso contrario, deberá mostrar el texto 'El número es IMPAR'. Un número es par si el
#resto de dividirlo por 2 es 0

num=int(input("Ingrese un numero"))
if num % 2 == 0:
    print("El numero es PAR")
else : 
    print("El numero es impar")