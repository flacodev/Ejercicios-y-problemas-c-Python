#14) Escribí un programa que solicite el ingreso de números enteros positivos. Se deberán analizar los dígitos que
#componen a cada número ingresado informando:
#a) La cantidad de dígitos pares e impares que posee cada número ingresado.
#b) Cuántas veces apareció en total el dígito 5 en todos los números procesados.
#La lectura de números finaliza al leer el valor -1.

digitos_pares= 0 
digitos_impares=0 
cant_de_5=0
num_analizar=int(input("ingrese numeros para analizar(-1 para finalizar): "))

while num_analizar != -1: 
    while num_analizar!= 0:
        digito=num_analizar %10
        if digito%2==0:
            digitos_pares+=1
        else:
            digitos_impares+=1
        if digito==5:
            cant_de_5+=1

        num_analizar //=10

    print("cantidad de digitos pares: ", digitos_pares)
    print("cantidad de digitos impares: ", digitos_impares)
    print("cantidad de 5 en el numero: ", cant_de_5)
    digitos_pares= 0 
    digitos_impares=0 
    cant_de_5=0
    num_analizar=int(input("ingrese numeros para analizar(-1 para finalizar): "))