# 7) Escribí la función dos_minimos(lista) que reciba una lista de elementos comparables entre sí y devuelva los
# dos valores menores encontrados en la lista dada. Si la lista tuviera menos de dos elementos, retornar None
# por cada elemento faltante.
# Ejemplos: dos_minimos([23, 456, 12, 16, -4, 56])retorna(-4, 12)
# dos_minimos([4]) retorna (4, None)
# dos_minimos([]) retorna (None, None)

def dos_minimos(lista):
    if len(lista)==0:
        return None, None
    elif len(lista)==1:
        return lista[0], None
    
    minimo1, minimo2 = lista[0], lista[1]
    if minimo1 > minimo2:
        minimo1, minimo2=minimo2, minimo1   
        # swap
    for i in lista[2:]:
        if i < minimo2:
            minimo2=i
            if minimo2 < minimo1:
                minimo2=minimo1
                minimo1=i
            else:
                minimo2=i
    return minimo1, minimo2

lista=[]
print(dos_minimos(lista))    
