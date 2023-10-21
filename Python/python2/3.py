#3) Dada la lista a = [ False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True ] utilizar instrucciones que permitan:
#a) Obtener el primero y el último elemento.
#b) Eliminar el primer elemento
#c) Eliminar los tres últimos elementos
#d) Insertar el valor 9 en el primer lugar de la lista (desplazando al resto)
#e) Reemplazar el valor 'ix' por el valor 4
#f) Agregar el valor 5 al final de la lista
#g) Obtener, mediante una rebanada, los primeros 3 elementos
#h) Insertar la lista al final de la misma lista, es decir, la lista a deberá contener a la lista a
#i) Determinar si el elemento ‘dos’ pertenece a la lista y si el elemento 3.0 pertenece a la lista
#j) Determinar cuántas veces aparece el elemento 1 en la lista y cuántas veces aparece el elemento 4
#k) Imprimir cada elemento de la lista (iterando)
#l) Imprimir cada elemento de la lista en forma inversa (iterando)
a = [ False, 1, 'dos', 3.0, 'ix', (5,), [3, 3], True ]
#a) 
    print(a[0])
    print(a[-1])
#b)
    a.pop(0)
    print(a)"""  """
#c)
    a=a[0: -3]
    print(a)
#d)
    a.insert(0, 9)
#e)
    a[a.index('ix')]= 4
#f)
    a.append(5)
#g)
    print(a[0: 3])
#h)
    a.append(a)
#i)
if 'dos' in a:
    print("dos esta en la lista")
else:
    print("dos no esta en la lista")
if 3.0 in a:
    print("esta el 3.0")
else:
0    print("3.0 no esta en la lista")

#j)
    print("la cantidad de 1 es:", a.count(1))
    print("la cantidad de 4 es:", a.count(4))

#k) 
   for i in a:
       a[0: -1]
       print(i)
#l)
   a.reverse()
   for i in a:
       a[0: -1]
       print(i)