#9) Modificar el programa anterior para que, si se ingresa un número negativo, no se sume pero continúe con el
#proceso. Finalmente, mostrar por separado la suma de los números positivos pares e impares ingresados.

#numerospedidos= int(input("cantidad de numeros: "))
#suma = 0 
#for contador in range(numerospedidos):
#    suma += int(input("numeros a sumar"))
#    print(suma)

numerospedidos= int(input("cantidad de numeros a sumar: "))
suma=0
suma_pares= 0 
suma_impares=0
for i in range(numerospedidos):
    numeros=int(input("ingrese numero a sumar: "))
    if numeros >= 0:
        suma += numeros
        if numeros % 2 == 0:
            suma_pares += numeros
        elif numeros % 2 == 1:
            suma_impares += numeros

print("la suma total es: ", suma)
print("la suma de los pares es: ", suma_pares)
print("la suma de los impares es: ", suma_impares)

        
    