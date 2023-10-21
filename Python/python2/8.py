# Escribí la función digitos(numero) que retorne una lista con los dígitos que componen al número pasado por
# parámetro. Ejemplo: digitos(18413) retornará [1, 8, 4, 1, 3].
def digitos(numero):
    lista=[]
    while numero!=0:
        digito=numero%10
        numero= numero//10
        lista.append(digito)
    lista.reverse()
    return lista

numero=int(input("ingrese: "))
print(digitos(numero))