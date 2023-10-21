#7) Solicitar el ingreso de un número entero. Si es número ingresado es impar, se deberán imprimir los números
#correlativos desde el ingresado hasta el doble del mismo. Si el número ingresado es par, se deberán mostrar los
#números pares desde el ingresado hasta el doble del ingresado. Por ejemplo, si se ingresa un 8, se mostrará 8,
#10, 12, 14, 16. Si se ingresa un 5, se mostrarán 5, 6, 7, 8, 9, 10

num= int(input("ingrese un num entero: "))

if num % 2 == 1:
    for num in range(num-1, num*2):
        print(num+1)
elif num % 2 == 0:
  for num in range(num, num* 2+ 1,2):
           print(num )