# 1-Escribe un programa que pida al usuario una palabra y luego imprima cada
# letra de la palabra en una línea separada.
'''
palabra = input("Ingresar una palabra: ")
for letra in palabra:
    print(letra)
'''
# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.
'''
limite = int(input("Ingresa un valor: "))

acum=0
for num in range(1, limite+1):
    acum+=num

print(acum)
'''
# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.
'''
valor = int(input("¿A que tabla de multiplicar queres acceder? -> "))
for num in range(1, 11):
    print(f"{num}*{valor}={num*valor}")
'''
# 4-Escribe un programa que imprima los números pares del 1 al 100.
'''
'''
# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.
'''
'''
# 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
# palabra pero con las letras en orden inverso.
# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).
# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.
# 9-Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.
# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.
# 11-Escribe un programa que pida al usuario un número y calcule su factorial.
# Un factorial es el producto que resulta de multiplicar un número entero positivo
# dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# de 4 es 4! = 4 × 3 × 2 × 1 = 24.
# 12-Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio.
# 13-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****
'''
18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1          = 1
2 3        = 2
4 5 6      = 3
7 8 9 10   = 4
numero = int(input("Ingresa un número: "))
contador=1
fila=1
while contador <= numero:
    for i in range(fila):
        print(contador, end=" ")
        contador+=1
    fila+=1
    print()
'''



