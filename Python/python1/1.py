#1) Escribí un programa que solicite el ingreso de dos números enteros y que imprima el resultado de su suma, suresta, su multiplicación, el cociente de la división, el resto de la división, la división entera entre ambos y el valorabsoluto de ambos.
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))
opera=input("ingrese el calculo: ")
if opera == "+":
    print(n1+n2)
elif opera == "-":
    print(n1-n2)
elif opera == "*":
    print(n1*n2)
elif opera=="/":
    print(n1/n2)
elif opera=="%":
    print(n1%n2)