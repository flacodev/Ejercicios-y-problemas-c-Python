#17) Escribí un programa que solicite el ingreso de una cadena de texto e informe:
#a) La cantidad de palabras que posee la cadena.
#b) La cantidad de caracteres que posee cada palabra.
#c) La palabra más larga que contiene la cadena.
#Nota: cada palabra estará separada por un espacio en blanco (puede haber espacios al comienzo y al final de la
#cadena).
texto=input("ingrese el texto ")
palabras=texto.split()
cant_palabras= len(palabras)

max_caracteres=0
palabra_larga=""
for letras in palabras:
    cantidad_caracteres=len(letras)
    print("la palabra, ", letras, " tiene : ",cantidad_caracteres)
    if cantidad_caracteres>max_caracteres:
        max_caracteres=cantidad_caracteres
        palabra_larga=letras

print("la cantidad de plabras es: ",cant_palabras)  
print("la palabra mas larga es: ", palabra_larga)