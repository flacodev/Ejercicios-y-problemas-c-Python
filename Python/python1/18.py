#18) Escribí un programa que solicite el ingreso de una cadena de caracteres e informe qué vocales (mayúsculas y
#minúsculas indistintamente) aparecen en la cadena, sin repetir. Por ejemplo, para 'Programando' debería
#informar: a, i, o.

cadena=input("ingresar una cadena de texto: ")
cadena=cadena.lower()
vocales="aeiouáéíóú"
vocales_encon=""
for letras in cadena:
    if letras in vocales and letras not in vocales_encon:
        vocales_encon = vocales_encon + letras

print(vocales_encon)     
    


