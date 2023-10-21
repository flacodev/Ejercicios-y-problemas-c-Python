# 22) Se ingresan todos los datos de los socios del club 'CAVUL'. Para cada socio se solicita: Nombre, apellido, DNI,
# edad y si tiene o no su cuota al día. La lectura de los datos finaliza cuando se ingresa el DNI '0'. Almacenar la
# información de los socios en una estructura adecuada para realizar búsquedas por DNI. Se pide:
# a) Informar la cantidad de socios del club.
# b) Informar la cantidad de socios morosos.
# c) Informar el nombre y apellido del socio cuyo DNI es 25.123.555. En caso que no exista un socio con dicho
# documento, se deberá informar la situación.
# d) Dar de alta a un nuevo socio cuyos datos son: DNI: 40.151.724, apellido: 'Quito', nombre: 'Esteban' y edad:
# 17. Dicho socio acaba de pagar su cuota inicial.
# e) Informar el número de documento del socio de mayor edad.
# f) Dar de baja al socio con el DNI 15.188.125, asegurándose primero que esa persona efectivamente sea socio
# del club. No deberá aceptarse la baja del socio si éste no tiene su cuota al día.
# g) Registrar que el socio cuyo DNI es 28.731.431 acaba de pagar la cuota de este mes.

socios={}
dni=int(input("ingrese un dni: "))
while dni!=0:
    nombre=input("ingrese nombre: ")
    apellido=input("ingrese apellido: ")
    edad=int(input("edad: "))
    al_dia= input("cuota al dia?(s/n): ")
    if al_dia=="s":
        al_dia=True
    else:
        al_dia=False
    socios[dni]=[nombre, apellido, edad, al_dia]
    dni=int(input("ingrese un dni: "))
print("socios", len(socios))
morosos=0
for nombre, apellido, edad, al_dia in socios.values():
    if al_dia==0:
        morosos+=1

if  "25123555" in socios:
    print("nombre: ", socios[25123555][0],"apellido: ", socios[25123555][1])
else:
    print("No se encuentra el socio")

socios[40151724]=["esteban", "quito", 17, "s"]
max_edad=-1

for dni, datos in socios.items():
    if datos[2]>=max_edad:
        max_edad=datos[2]
        dni_mayor=dni
print("el socio mas grande es", dni_mayor)
dni=15188126
if dni in socios:
    if socios[dni][3] == "s":
        del socios[dni]
    else:
        print("el socio debe")
else:
    print("no existe el socio")

socios[28731431][3]="s"