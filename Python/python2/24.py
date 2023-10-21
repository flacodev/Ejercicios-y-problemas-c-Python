# 24) Solicitá al usuario que ingrese nombres de ciudades y el país al que pertenecen (cortar cuando se ingresa la
# ciudad “zz”). Luego informá: cuántas ciudades ingresó en total y cuántas ciudades por cada país (para esto
# último, utilizá un diccionario). Implementá dos soluciones algorítmicas diferentes de para este mismo
# ejercicio:
# a) En una de ellas, las ciudades no se almacenarán a medida que se las ingresa.
# b) En la otra, se almacenará cada ciudad con su país en una lista (cada elemento será una lista con 2 strings).
# Ejemplo: [ [“Colonia”, “Uruguay”], [“Granada”, “España”], [“Inverness”, “Escocia”], [“Salto”, “Uruguay”],
# [“Piriápolis”, “Uruguay”], [“Aberdeen”, “Escocia”] ]. Luego de haber terminado la carga de datos en la lista, se
# procesará la misma para calcular la cantidad de ciudades por país.

dict={}
cantidad=0
cuidad=input("ingrese una cuidad:")
while cuidad!="zz":
    pais=input("ingrese su pais:")
    cantidad+=1
    dict[pais]=cuidad
    cuidad=input("ingrese la cuidad")
cantidad_valores_paises= len(dict.values)
print("se ingresaron",cantidad,"cuidades y",cantidad_valores_paises,"por pais")