#2) Escribí un programa que solicite el ingreso de un número entero e informe si el valor leído es o no es mayor queel número 10.
n_ent=int(input("ingrese un numero ent: "))
if n_ent > 10:
    print("es mayor que 10")
elif n_ent == 10:
    print("es igual a 10")
else :
    print("es menor a 10")