#11) Escribí un programa con el cual se procesarán las notas de un final de la materia. Para esto, se solicitará el ingreso del número de alumno y la nota recibida, 
#hasta que se ingrese un número de alumno igual a cero, en
#cuyo caso se deberá imprimir en pantalla la leyenda 'Aprobados: ' y la cantidad de aprobados junto con la
#leyenda 'Desaprobados: ' y la cantidad de desaprobados. Se deberá tener en cuenta que se aprueba con una
#nota mayor a 4.

aprobados= 0 
desaprobados = 0 
while True :
    numero_de_alumno=int(input("ingrese el numero de alumno: "))
    if numero_de_alumno==0:
        break
    nota=int(input("ingrese la nota: ")) 
    if nota > 4: 
        aprobados+= 1
    elif nota<= 4:
        desaprobados+= 1
    
print("la cantidad de alumnos aprobados es: ", aprobados)
print("la cantidad de alumnos desaprobados es: ", desaprobados)
        


 