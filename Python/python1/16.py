#16) Escribí un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
#finalizando cuando se reciba un cero y mostrando la cantidad de números primos ingresados.
cant_primos=0

while True:
    num=int(input("ingrese num"))
    if num==0:
        print("Programa finalizado")
        break
    if num > 1:
        for i in range(2, num):
            if num % i==0:
                cant_primos+=0
                break
        else:
            cant_primos+=1
            
print("la cantidad de primos es: ",cant_primos)

