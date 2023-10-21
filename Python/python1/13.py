#13) Escribí un programa que solicite el ingreso de 20 números enteros que se encuentren entre -10 y 10 e imprima
#la sumatoria de los valores negativos, la cantidad de valores iguales a cero y el promedio de los valores
#positivos. Se deberá pedir el reingreso de un número si éste estuviera fuera del rango dado.

iguales_a_cero= 0 
negativos= 0 
positivos= 0 
suma_posit=0
for i in range(20):
    numero=int(input("ingrese un numero dentro del rango -10, 10: "))
    while numero < -10 or numero > 10:
        print("el numero esta fuera del rango")
        numero=int(input("ingrese un numero dentro del rango -10, 10: "))
    if numero == 0: 
        iguales_a_cero+=1
    if numero < 0:
        negativos+= numero
    if numero> 0:
        positivos+=1
        suma_posit+= numero
    if positivos>0: 
        promedio_pos= suma_posit/positivos

print("la cantidad de valores iguales a 0 son: ", iguales_a_cero)
print("la suma de los numeros negativos es: ", negativos)
print("el promedio de los numeros positivos es: ", promedio_pos)

        
     