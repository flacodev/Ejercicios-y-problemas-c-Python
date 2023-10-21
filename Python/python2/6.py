# 6) Implementar la funcion minimo_elemento(lista) que recibe como parámetro una lista de elementos
# comparables entre sí y devuelve el mínimo valor encontrado en dicha lista o None si la lista fuera vacía.
# Ejemplos: minimo_elemento([4, 8, 15, 16, 23, 42]) retorna 4
# minimo_elemento("PYTHON") retorna 'H'

def minimo_elemento(lista):
    if len(lista)== 0:
        return None
    else:
        menor=lista[0]
        for i in lista[1:]:
            if i < menor:
                menor=i
        return menor
lista=[]
valores=int(input("ingrese valores: "))
while valores!=0:
    lista.append(valores)
    valores=int(input("ingrese  valores: "))

print(minimo_elemento(lista))