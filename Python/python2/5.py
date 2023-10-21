#5) Producir una nueva lista con los nombres de la lista generada en el ejercicio anterior, donde los nombres
#hayan sido convertidos completamente a mayúsculas.
hombres=[]  #crear lista vacia
nombre=input("ingrese un nombre").upper()
while nombre!="":
    hombres.append(nombre) #agregar el nombre a la lista vacia
    nombre=input("ingrese un nombre").upper() #solicitar otro nombre, si no es un string vacio, repetir
for nombre in hombres:
    print(nombre)