#3) Modificá el programa anterior para que ahora solicite el ingreso de dos números enteros, y que luego informe si
#el primero es o no es mayor que el segundo, usando el formato 'X es mayor que Y' (o ‘X no es mayor que Y’). Si
#ambos números fueran iguales, deberá informar 'X es igual a Y'. Por ejemplo, si se ingresan 23 y 42, se mostraría
#'23 no es mayor que 42'.
n_ent1=int(input("ingrese un numero ent: "))
n_ent2=int(input("ingrese otro numero ent: "))
if n_ent1 > n_ent2:
    print(n_ent1, "es mayor que", n_ent2)
elif n_ent1 < n_ent2:
    print(n_ent1, "no es mayor que", n_ent2)
else :
    print(n_ent1, "es igual a", n_ent2)
