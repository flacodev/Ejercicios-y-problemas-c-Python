# 20) Almacenar el número de habitantes de cada ciudad en una estructura que te permita acceder directamente a
# dicho número sabiendo el nombre de la ciudad. Los datos son: Junín: 102.023, Rojas: 28.654, Pergamino:
# 80.569. Escribí instrucciones que permitan:
# a) Informar la cantidad de habitantes que tiene Pergamino.
# b) Agregar a Lincoln con 42.036 habitantes.
# c) Eliminar a Junín.
# d) Incrementar los habitantes de Rojas en 1.000.
# e) Modificar la cantidad de habitantes de Pergamino por 91.399.

ciudades={
    "junin": 102023 , 
    "rojas":28654 , 
    "pergamino": 80569,
      }

print(ciudades["pergamino"])

ciudades["lincoln"]=42036

del ciudades["junin"]

ciudades["rojas"]+=1000

ciudades["pergamino"]=91399
