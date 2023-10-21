#2) Dada la lista L = [ 5, 6, [9, 5], 2, 5 ], utilizar una instrucción para contar cuántas veces aparece el elemento 5.
L = [ 5, 6, [9, 5], 2, 5 ]
print(L.count(5))
for elementos in L:
    if type(elementos)== list:
        for i in elementos:
            print(i)
    else:
        print(elementos)