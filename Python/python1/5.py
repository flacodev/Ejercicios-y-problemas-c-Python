#5) Solicitar al usuario que ingrese el día de la semana y la cantidad de artículos comprados por un cliente en una
#tienda. Finalmente, imprimir “accede al descuento” si el día es lunes y el cliente compró más de 3 artículos. En
#caso contrario, no imprimir nada.
dia=input("Ingrese el dia: ")
cant_art=int(input("Cantidad de articulos comprados: "))
if dia==("lunes") and cant_art > 3:
    print("Accede al descuento")
