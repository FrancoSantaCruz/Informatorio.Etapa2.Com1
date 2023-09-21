# ESTRUCTURAS DE DATOS.
# guardar datos dentro de variables:   x = 5
# controlar el flujo del programa:  if elif else 
# Como organizar y almacenar los datos: Estructuras de datos.

# Existen 4 tipos de estructuras de datos: 
# - Listas (List)
# - Tuplas (Tuple)
# - Conjuntos (Set)
# - Diccionarios (Dict)

# *******LISTAS [ elementos, elementos ]

# Las listas son una colección ordenada y mutables de elementos que puede contener
# diferentes tipos de datos.

        #  0  1  2
# numeros = [1, 2, 3]
# indices:     0          1           2       3     
# nombres = ["Esteban", "Santiago", "Javier", "Ana"]

# lista_con_todo = [2, "Santiago", [1, 2, 3], 5.98, "Esteban"]
# print(lista_con_todo[2])
# print(type(lista_con_todo))
# print(lista_con_todo[2][1])

# Slicing -> Acceder a un rango de elementos. 
# print(nombres[1:5])
# print(nombres[:5])
# print(nombres[3:])
# print(nombres[::-1]) #Reversa

# Cambiar los valores de los elementos
# nombres[2] = 3.14
# print(nombres)

# Métodos
# nombres = ["Esteban", "Santiago", "Javier", "Ana", "Santiago", "Santiago", "Santiago"] #Lista
# Ejemplos:
# .append() me permite agregar un elemento al final de mi lista.
# print(nombres)
# nombres.append("Franco")
# print(nombres)

# .insert(indice, elemento) me permite agregar un elemento en una posición particular
# print(nombres)
# nombres.insert(1, "Franco")
# print(nombres)

# .remove(elemento)
# print(nombres)
# nombres.remove("Santiago")
# print(nombres)

# .clear() me elimina todos los elementos
# print(nombres)
# nombres.clear()
# print(nombres)

# .count(elemento) me cuenta cuantas veces aparece ese elemento en la lista
# print(nombres)
# contador = nombres.count("Santiago")
# print(contador)

# .reverse() me da vuelta la lista.
# print(nombres)
# nombres.reverse()
# print(nombres)

# .pop()
# print(nombres)
# removido = nombres.pop()
# print(nombres)
# print(removido)

# *******TUPLAS ( elementos, elementos )

# Es también una colección de elementos ordenados pero las tuplas son inmutables.
# Por lo tanto no se pueden agregar, modificar o eliminar elementos. 

# mi_tupla = "Manuel", "Tiago", "Nestor"
# una_tupla= ("Manuel",)

# mi_tupla = ("Manuel", "Tiago", "Nestor")
# print(mi_tupla)
# mi_tupla = ("Manuel", "Tiago", "Nestor", "Manuel", "Manuel")
# print(mi_tupla.count("Manuel"))
# print(len(mi_tupla))

# Unificar tuplas
# tupla_uno = (1, 2, 3, 4)
# tupla_dos = (5, 6, 7, 8)
# tupla_total = tupla_uno + tupla_dos
# print(tupla_total)

# ***** CONJUNTOS(SET) { elementos, elementos }

# Una coleccion de elementos pero que son DESORDENADOS y sus elementos son UNICOS.
# conjuntos = {1, 5, "Hola", "Mundo", 3.14, "Hola", 5}
# print(conjuntos)

# ***** DICCIONARIOS (dict) 

# clave : valor    ó     key : value
# Registros - Diccionarios - Objetos

# nombre_dict = {
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor",
#     "clave":"valor"
# }

# mi_dict = {
#     "Nombre":"Franco",
#     "Edad": 24, 
#     "Estudiante": True,
#     "Nacionalidad": "Argentina"
# }

# mi_dict["administrador"] = False
# print(mi_dict)

# Modificar un valor en el diccionario
# mi_dict["Edad"] = 28
# print(mi_dict)

# print(mi_diccionario["Estudiante"])

# lista_usuario = [  ("Nombre","Franco"),("Edad", 24), ("Estudiante", True), ("Nacionalidad", "Argentina")]
# un_diccionario = dict(lista_usuario)
# print(un_diccionario)
# print(type(un_diccionario))

# .clear()
# print(mi_dict)
# mi_dict.clear()
# print(mi_dict)

# .keys() -> me devuelve todas las claves(keys) de mi diccionario
# print(mi_dict.keys())

# .values() -> me devuelve todos los valores(values) de mi diccionario
# print(mi_dict.values())

# .pop(clave) -> Elimina la clave dada y me la devuelve.
# print(mi_dict)
# removido = mi_dict.pop("Edad")
# print(mi_dict)
# print(removido)

# .items()
# print(mi_dict.items())

