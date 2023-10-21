# 13) Dadas dos listas, una con datos de ciudades y otra con datos de personas, con el siguiente formato:
# - La lista de ciudades contiene listas con nombres de ciudades y la provincia a la que pertenecen. Ejemplo:
# [ ["Rosario","Santa Fe"], ["Carlos Paz","Córdoba"], ["Balcarce","Buenos Aires"], ["Cosquín","Córdoba"] ]
# - La lista de personas contiene listas con nombre, DNI y ciudad de cada persona. Ejemplo:
# [ ["Juan Perez",26782345,"Carlos Paz"], ["María Gomez",40173542,"Rosario"], ["Ana Ríos",9216378,"Cosquín"] ]
# a) Escribir la función obtenerCiudad(personas, DNI) que, dada la lista de personas y el DNI de una persona,
# retorne la ciudad donde vive.
# b) Escribir la función obtenerProvincia(personas, ciudades, DNI) que, dadas las dos listas y el DNI de una
# persona retorne la provincia donde vive. Utilizar la función del inciso a.
# c) Escribir la función contarPoblacion(personas, ciudades, provincia) que, dadas las dos listas y una
# provincia, informe cuántas personas viven en esa provincia. Utilizar la función del inciso b

ciudades= ["Rosario","Santa Fe"], ["Carlos Paz","Córdoba"], ["Balcarce","Buenos Aires"], ["Cosquín","Córdoba"]
personas=  ["Juan Perez",26782345,"Carlos Paz"], ["María Gomez",40173542,"Rosario"], ["Ana Ríos",9216378,"Cosquín"]

def obtenerCiudad(personas, DNI):
    for dato in personas:
        if dato[1] == DNI:
            return dato[2]
        return " "
        

def obtenerProvincia(personas, ciudades, DNI):
    ciudad= obtener_ciudad(personas, DNI)
    if ciudad != " ":
        for dato in ciudades:
            if dato[0] == ciudad:
                return dato[1]
            return " "
           

def contarPoblacion(personas, ciudades, provincia):
    for dato in personas:
        prov= obtener_provincia(personas, ciudades, dato[1])
        if prov == provincia:
            cant= cant + 1
    return cant