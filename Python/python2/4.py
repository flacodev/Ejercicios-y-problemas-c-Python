#4) Escribir un programa que pida al usuario el ingreso por teclado de una serie de nombres, terminando al leer
#un nombre en blanco. A medida que se ingresan, agregar cada nombre al final de una lista. Al finalizar el
#ingreso se deben imprimir los elementos de dicha lista, iterando por ella

hombres=[]  #crear lista vacia
nombre=input("ingrese un nombre")
while nombre!="":
    hombres.append(nombre) #agregar el nombre a la lista vacia
    nombre=input("ingrese un nombre") #solicitar otro nombre, si no es un string vacio, repetir

for nombre in hombres:
    print(nombre)