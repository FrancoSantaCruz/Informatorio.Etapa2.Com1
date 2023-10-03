# Estructuras de control -> Condicionales | Repetitivas. 

# ESTRUCTURAS CONDICIONALES.

# La pregunta que me tiene que devolver un Si o No la llamamos CONDICION.
# Si o No -> True o False. 


# Si... 
# if condicion:
#     accion
#     accion
#     accion

# Condicional Simple: 
# Programa que me diga si tengo permitido entrar al boliche. 
# Mayor de edad. Ingresar mi edad por consola. 
# edad = int(input("Ingresa tu edad para corroborar: "))
# if edad>18:
#     print("Podes pasar!")

# print("Estoy fuera del if")

# Condicional encadenado:
# edad = int(input("Ingresa tu edad para corroborar: "))
# if edad>18:
#     print("Podes pasar!")
# if edad<18:
#     print("No papi sos menor, anda a tu casa.")

# Condicion anidado:
# edad = int(input("Ingresa tu edad para corroborar si podes votar: "))
# if edad>=16:
#     print("Usted puede votar")
#     if edad>70: 
#         print(" pero es opcional.")

# Condicionales con operadores lógicos: 

# && -> "y lógico" conjunción   -> and
# || -> "ó lógico" disyunción   -> or 
# ! -> negación                 -> not

# edad = int(input("Ingresa tu edad para corroborar: "))

#   True     y     True   -> True  -> Se tiene que ejecutar el print. 
#   True     y     False  -> False -> no debería hacer nada
#   False     y     True  -> False -> no debería hacer nada
# if edad>=16 and edad<24 and edad!=20:
#     print("Votar es opcional pero podes.")
# 16 y 24 pero no puede ser 20
 
#   True     o     True     -> True   -> Se tiene que ejecutar el print. 
#   True     o     False    -> True   -> Se tiene que ejecutar el print.
#   False    o     True     -> True   -> Se tiene que ejecutar el print.
#   False    o     False    -> False  ->
# if edad>=16 or edad<18:
#     print("Votar es opcional pero podes.")

# NOT -> Negar
# auxiliar = False
# not True -> False
# not False -> True
# if not auxiliar:
    # print("Estoy dentro")

# Condicional Alternativo. (else)
# edad = int(input("Ingresa tu edad para corroborar: "))

# if edad>18:
#     print("Podes pasar!") #Esto es el camino del True
# else:
#     print("No nenx, anda a tu casa.") #Esto es el camino del False.

# Si edad es mayor a 18:
#     imprimir("podes pasar")
# Sino:
#     imprimir("noo nenx blabla")

# Programita de las notas: 
# <6 "Eu no estas practicando los ejercicios del CENIT. Repasa para la proxima"
# <8 "Re bien, felicidades, quedan cositas por pular pero perfecto! 🙏"
# "Que te voy a enseñar, enseñame vos a mi GENIX"

# nota = int(input("Ingresar nota del Alumno: "))

# if nota<6:
#     print("Eu no estas practicando los ejercicios del CENIT. Repasa para la proxima")
# else: 
#     if nota<8: #6 y 7
#         print("Re bien, felicidades, quedan cositas por pular pero perfecto! 🙏")
#     else: # 8 9 y 10
#         if nota<9:
#             print("")
#         else:
#             print("Que te voy a enseñar, enseñame vos a mi GENIX")

# Condicional Multiple (elif)
# switch - Java. 
# nota = int(input("Ingresar nota del Alumno: "))
# # elif -> Sino, si... 
# if nota<3: #2
#     print("Eu no estas practicando los ejercicios del CENIT. Repasa para la proxima")
# elif nota<6: #5
#     print("Re bien, felicidades, quedan cositas por pulir pero perfecto! 🙏")
# elif nota<8: #7
#     print("Soy menor que 8")
# elif nota<9: #8
#     print("Soy menor que 9 :D")
# else:
#     print("Que te voy a enseñar, enseñame vos a mi GENIX")

# EJERCITACIÓN:

# 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
#   mayor de edad (18 años o más) o no.

# edad = int(  input("Ingresa tu edad, por favor 🙏: ")   )

# if edad>=18:
#     print("Es mayor de edad")
# else:
#     print("No es mayor de edad.")

# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

# d, m, a = input("Ingresa tu fecha de nacimiento en el siguiente formato dd/mm/aaaa *SEPARADO POR ESPACIOS*: ").split("/")

# print(f"Día: {d}")
# print(f"Tipo de dato:{type(d)}")
# print(f"Mes: {m}")
# print(f"Año: {a}")

# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a".

# cadena_caracteres = input("Ingresa una palabra cualquiera: ")
# # in -> en


# if "a" in cadena_caracteres or "A" in cadena_caracteres:
#     print(f"Si se encuentra la letra A en {cadena_caracteres}")
# else: 
#     print(f"No se encuentra la letra A en {cadena_caracteres}")
