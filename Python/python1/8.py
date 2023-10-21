#8) Escribí un programa que solicite ingresar una cantidad de números enteros a procesar. Luego, permitir al
#usuario ir ingresando uno a uno la cantidad pedida de números. Una vez finalizado el ingreso, se deberá mostrar
#la suma total de los números ingresados.

numerospedidos= int(input("cantidad de numeros: "))
suma = 0 
for contador in range(numerospedidos):
    suma += int(input("numeros a sumar"))
    print(suma)


