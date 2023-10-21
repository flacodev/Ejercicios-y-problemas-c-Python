#12) Escribí un programa que solicite el ingreso del monto de cada venta realizada en una tienda durante la última
#semana. Luego, se deberá mostrar el monto total de las ventas. Si se lee un monto negativo, se debe informar el
#problema sin interrumpir el ingreso de los datos. La lectura de la información finaliza al leer un monto igual a
#cero. 
total_ventas=0 
ventas=float(input("ingrese el monto de las ventas: "))
while ventas !=0:
    if ventas < 0: 
        print("error")
    else:
        total_ventas+=ventas
    ventas=float(input("ingrese el monto de las ventas: "))
print("el monto total de la semana es: ", total_ventas)






