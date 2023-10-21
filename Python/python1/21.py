#21) Escribí un programa que solicite al usuario el título de su libro preferido. Imprimir luego “Tu libro preferido es:
#[nombre del libro ingresado]” donde el nombre del libro debe mostrarse con la primera letra en mayúscula y el
#esto en minúscula, independientemente de cómo lo haya ingresado el usuario. Esto es, si el usuario ingresó “el
#SEÑOR DE LOS ANILLOS” se debería mostrar: “Tu libro preferido es: El señor de los anillos”. Nota: no usar
#capitalize(). Se debe construir el algoritmo que convierta el string al formato pedido.

libro_fav=input("ingrese su libro favorito: ").lower()
libro_fav=libro_fav[0].upper() + libro_fav[1:]
#.upper hace q la letra con index 0, osea, la primer letra, la hace mayuscula y luego se concatena con el string libro fav desde [1:]
print("tu libro favorito es: ",libro_fav)