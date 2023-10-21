#6) Solicitar el ingreso de un número entero e imprimir los números correlativos desde el ingresado hasta el doble
#del mismo. Por ejemplo, si se ingresa un 6, se deberá mostrar: 6, 7, 8, 9, 10, 11, 12.
#num=int(input("Ingrese un numero entero: "))

num= int(input("ingrese un num entero: "))
for num in range(num-1, num * 2):
    print(num+1)
