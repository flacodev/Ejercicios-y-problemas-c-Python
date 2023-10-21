# 17) Escribí un programa que solicite el ingreso de números enteros hasta leer uno que no tenga dígitos repetidos.
# Se pide informar:
# a) Para cada número, la suma de los dígitos que se repiten en ese número.
# b) Para cada número, la cantidad de dígitos que se repiten en ese número.
# c) Al finalizar, el porcentaje de números procesados mayores que 478.
# d) Al finalizar, el promedio de los números procesados.

numeros=int(input("ingrese numeros: "))
conjun={}
for i in range(numeros):
    i=numeros%10
    conjun.add(i)
    numeros//10
print(conjun)