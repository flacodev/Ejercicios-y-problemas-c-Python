#19) Escribí un programa que permita al usuario ingresar una frase y luego un carácter (string de longitud 1) y luego
#muestre la frase ingresada, pero con todas las ocurrencias del carácter indicado por el usuario reemplazadas por
#“*”. Nota: no utilizar replace().
cadena=input("ingrese una frase: ")

while True:
    caracter=input("ingrese UN caracter: ")
    if len(caracter)!=1:
        print("debe ser un solo caracter")
        break
    texto = ""
    if len(caracter)==1:
        for i in cadena:
            if i==caracter:
                texto = texto + "*"
            else:
                texto = texto + i

print(texto)


