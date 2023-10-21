#22) Escribí un programa que, dada una frase, imprima una a una las palabras que la contienen. Se toma como
#precondición que cada palabra está separada por un espacio y que no existen espacios al principio ni al final de
#la frase ingresada. Ejemplo: si la frase es “aquí me pongo a cantar” se imprimirá:

frase=input("ingrese una frase: ")
#strip quita los espacios al principio y al final del string
frase.strip()
palabras=frase.split()
#split divide el string en substring para poder separar por palabras
for i in palabras: 
    print(i)
