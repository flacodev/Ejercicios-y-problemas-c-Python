# 9) Escribí la función borrar_adyacentes(lista) que recibe una lista donde sus elementos son caracteres (strings de
# longitud 1) y retorna una lista en la que queda una única ocurrencia de todos los caracteres adyacentes
# repetidos. Ejemplo: borrar_adyacentes(['a', 'a', '*', 'b', '=', '=', 'c', 'a']) retornará ['a', '*', 'b', '=', 'c', 'a'].


def borrar_adyacentes(lista):
    caracter=lista[0]
    listaf=[lista[0]]
    for i in lista:
        if i !=caracter:
            listaf.append(i)
            caracter=i
    return listaf


lista=["a","a","a","a","a"]
print(borrar_adyacentes(lista))
