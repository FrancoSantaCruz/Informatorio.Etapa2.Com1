'''
- Estructura repetitiva For. 
- Repaso general de todos los temas dados hasta el momento. 
- Calculadora
- Ejercitación individual.
'''

# Tipos de datos: 
    # int ej. 1, 2, 3, 4, -1, -2, -3
    # float ej. 1.323 , 4.50549, -50.239
    # boolean ej True , False
    # str ej "2", "True", "pizza", "Informatorio"

    # listas []
    # tuplas ()
    # conjuntos o sets {}
    # diccionarios { clave:valor }

    # input
    # edad = input("Ingresar tu edad: ")
    # print(type(edad))

    # len -> length -> longitud.
    # x = len([5, 2, 1, 4, 3])
    # print(x)
    
# Estructuras condicionales: 

# edad = int(input("Ingresa tu edad: "))

# if edad>=16 and edad<18:
#     print("Podes votar pero es opcional.")
# elif edad>=18 and edad<70:
#     print("Debes votar obligatoriamente")
# elif edad>=70:
#     print("Podes votar pero es opcional.")
# else:
#     print("No podes votar, sos menor.")

# Estructuras de datos: 
# indice  0     1     2      3
# listas = [1, "hola", True, 9.587]
# print(listas)
# listas.append("Informatorio")
# print(listas)
# indice  0     1     2      3
# tuplas = (1, "hola", True, 9.587)

# set = { 1, "hola", 9.587, "hola", 1, 8}
# print(set)
# Diccionarios.

# CALCULADORA

# print("Ingresar la operación que desea realizar.")
# print("Las opciones son:\n+ suma.\n- resta.\n* multiplicación.\n// división entera")
# opcion = input("-> ")

# valor_uno, valor_dos = input("Ingresar los valores a operar separados por espacios: ").split()
# valor_uno = int(valor_uno)
# valor_dos = int(valor_dos)

# resultado = 0

# if opcion == "+":
#     resultado = valor_uno + valor_dos
# elif opcion == "-":
#     resultado = valor_uno - valor_dos
# elif opcion == "*":
#     resultado = valor_uno * valor_dos
# elif opcion == "//":
#     resultado = valor_uno // valor_dos
# else:
#     print("Dale flaquito, te di las opciones, escribí bien!")


# print(f"El resultado de la operacion \"{opcion}\" es {resultado}")

