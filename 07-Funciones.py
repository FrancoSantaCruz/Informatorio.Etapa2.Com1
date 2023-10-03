# Funciones y Módulos. 
# Concepto: Las funciones son un fragmento de código con un nombre asociado
#           que realiza una serie de tareas.


# Estructura básica: 
# def <nombre>():
    # acciones
    # acciones
    # acciones

# Ejemplo N°1:
# def saludar():
#     print("Hola")
# saludar()

# Ejemplo N°2:
# def saludar(nombre, apellido, edad, localidad): #El parámetro es nombre
#     print(f"Los datos de {nombre} {apellido} son: Edad:{edad}\n de la ciudad de {localidad}")

# saludar("Franco", "Santa Cruz", 23, "Resistencia") 
# Los valores que reciben los parámetros son los argumentos.

# Ejemplo N°3:

# def sumar(valor_uno, valor_dos):
#     resultado = valor_uno + valor_dos
#     return resultado

# # print(sumar(2,4))
# res_suma = sumar(2, 4)
# print(res_suma)

# Ejemplo N°4: 
# def sumar(valor_uno, valor_dos):
#     """
#         Esta función suma dos valores pasados por parámetros.
#         y retorna el resultado.
#     """
#     resultado = valor_uno + valor_dos

#     return resultado

# res_suma = sumar(2, 4)
# print(f"El resultado de la suma es: {res_suma}")

# print(sumar.__doc__)

# Los parámetros los podemos DEFINIR según:
#   1) Su posición
#   2) Su Nombre
#   3) Un valor por defecto

# 1) Su posición:

# def sumar(valor_uno, valor_dos):
#     resultado = valor_uno + valor_dos
#     return resultado

# res_suma = sumar(2, 4)
# print(res_suma)

# 2) Su nombre:

# def sumar(valor_uno, valor_dos):
#     print(valor_dos)
#     resultado = valor_uno + valor_dos
#     return resultado
 
# res_suma = sumar(valor_dos=4, valor_uno=2)
# print(res_suma)

# 3) Valor por defecto: 
# def saludar(nombre="usuario"):
#     print(f"Hola {nombre}!")

# saludar()
# saludar("")

# Argumentos Indeterminados...

# ... posicionales (*args):
#   - A todos los argumentos recibidos los guarda en una tupla.
#   - Una tupla es ordenada (tupla[2]) pero es inmutable (tupla[2] = "Fernet")

# def lista_supermercado(*productos):
#     # productos = ("Leche", "Harina", "Huevo", "Aceite", "Fideo", "9 de oro", "Yerba") Es una previsualización de lo que contiene productos en este momento.

#     for producto in productos:
#         print(f"Debo comprar: {producto}")

# lista_supermercado("Leche", "Harina", "Huevo", "Aceite", "Fideo", "9 de oro", "Yerba")

# ... de palabras clave (**kwargs):
# - La forma en que definimos el parámetro en la función.
# - La forma en que pasamos los argumentos.
# - En lugar de crear una tupla con todos los argumentos, me crea un diccionario (dict)

# def lista_supermercado(**productos):
#     for producto, cantidad in productos.items():
#         print(f"Debo comprar {cantidad} de {producto}")

# lista_supermercado(Leche="3 lts", Harina="1 kg", Huevo= "1 doc", Aceite="5 lts", Fideo="2 paq")

# posiciales & con palabras clave:

# def calculadora(*valores, **usuario):
#     # valores = (2, 2, 2, 4, 6, 8)
#     # usuario = { "mentor" : "Franco" }

#     resultado=0
#     # Estructura de datos (tuplas)
#     for valor in valores: #aprendimos a recorrer estructuras de datos
#         resultado+= valor #Estructuras repetitivas aprendimos a hacer acumuladores, contadores y banderas

#     for profesion, nombre in usuario.items():
#         print(f"Bienvenido {profesion} {nombre}!. El resultado de la suma es {resultado}.")


# calculadora(2, 2, 2, 4, 6, 2, 6, alumno="Gustavo")

