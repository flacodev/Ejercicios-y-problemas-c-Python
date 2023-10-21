#10) Calcular e imprimir la suma de los primeros 25 números de la sucesión de Fibonacci. La sucesión comienza con
#los números 0 y 1 y, a partir de estos, cada elemento es la suma de los dos números anteriores en la secuencia:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
num1= 0 
num2=1
suma= 0

for i in range(25):
    suma+=num1
    num3=num1 + num2
    num1=num2
    num2=num3
print(suma)
