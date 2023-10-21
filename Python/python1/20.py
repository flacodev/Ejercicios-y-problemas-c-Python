#20) Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo carácter), uno por vez. La
#repetición finalizará cuando se ingrese un string que no tenga longitud 1, o cuando el string ingresado
#corresponda al dígito numérico 0. Al finalizar, mostrar el string completo que se formó con todos los caracteres
#ingresados y qué porcentaje de caracteres del total fueron la letra “z” (minúscula).
caract=input("ingrese un caracter (terminar con 0 o dos caracteres): ")
cadena=""

while caract !="0":
    cant_caract=len(caract)
    if cant_caract==1:
        cadena=cadena+caract
        caract=input("ingrese un caracter (termina con 0 o dos caracteres): ")
    else:
        break
    
porcentaje= cadena.count("z") / len(cadena) * 100 
print(cadena)
print("el porcentaje de z es %",porcentaje) 
