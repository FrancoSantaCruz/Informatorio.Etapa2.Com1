# CTRL + C CORTA LA EJECUCIÓN DEL PROGRAMA.

# BUCLE: llamamos al bloque de código que va a ejecutar el for o while. 
# A cada ejecución de bucle le vamos a llamar ITERACION

# -----WHILE -> Mientras
# También requerimos de una condición para ejecutar. 
# El bucle while lo utilizamos cuando queremos ejecutar un bloque de código MIENTRAS se esté cumpliendo la condición. 
# Una vez que ya no se cumpla, deja de iterar.

# Estructura: 
# while <condicion>:
#       Acción
#       Acción
#       Acción
#       contador

# Ejemplo N°1:

# i = 1 #Contador

# Mientras i sea menor o igual a 5, ejecuta el print con el valor de i.
# while i<=5:
    # print(palabra)
    # i += 1
# print("Terminó de imprimir :D")


# Ejemplo N°2: Encontrar todos los numeros PARES que estan en esta lista. 

# una_lista = [42, 564, 12, 969, 42, 92, 23, 75]
# impares = []
# pares = []
# i = 0

# while i < len(una_lista): 
#     print(f"Vuelta n°{i}.")

#     if una_lista[i]%2 == 0: #Si el numero es par. 
#         pares.append(una_lista[i])
#     else:
#         impares.append(una_lista[i])
#     i+=1

# print(pares)
# print(impares)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Al contador se los puede encontrar como Variable especial. 
# 3 tipos de variables especiales
#       - Contador.
#       - Acumulador.
#       - Bandera.

# Acumulador:

# una_lista = [2, 10, 5, 4, 8]
# i=0
# acumulador = 0

# while i<len(una_lista):
#     acumulador = acumulador + una_lista[i] #el acumulador está acumulando la suma de los elementos de mi lista.
#     i+=1 #el contador me está controlando la cantidad de iteraciones.

# print(acumulador)




# Bandera (True or False)

# Ejemplo N°1:
# Quiero ingresar por teclado y verificar si el numero ingresado se encuentra en la lista. 
# una_lista = [42, 564, 12, 969, 67, 92, 23, 75]

# nro_buscar = int(input("Ingresa el número que quieras buscar en la lista: "))
# i=0
# encontrado = False

# while i<len(una_lista):
#     print(f"vueltas{i}")
#     if una_lista[i] == nro_buscar:
#         encontrado = True
#         break
#     i+=1

# if encontrado:
#     print("El numero si se encuentra en la lista!")
# else: 
#     print("El numero NO se encuentra en la lista. :( ")
    

# Ejemplo N°2:
# bandera = True

# while bandera==True:
#     num = input("Ingresa un numero entre 1 y 5: ")
#     if(num.isdigit() and int(num)>=1 and int(num)<=5):
#         print("El numero que ingresó está perfecto!.")
#         bandera = False
#     else: 
#         print("Datos incorrectos, intentelo nuevamente!.")


# Ejemplo N°3

# user = input("Ingresar nombre de Usuario: ")
# password = input("Ingresar tu contraseña: ")

# while user != 'Informatorio' or password != '123asd':
#     # Mientras las credenciales sean invalidas, yo quiero repetir este bloque de código
#     print("El usuario o contraseña ingresados son incorrectos.\nIntentá nuevamente!.")
#     user = input("Ingresar nombre de Usuario: ")
#     password = input("Ingresar tu contraseña: ")
#     # Una vez que AMBAS credenciales sean correctas, permito el acceso. 
# else: 
#     print("Credenciales ingresadas correctas.")



# Caracteristicas que podemos concluir de la estructura repetitiva WHILE: 

# - No sabemos cuantas veces se va a iterar el bucle. 
# - El final del bucle está controlado por una condición. 
# - El conjunto de acciones (bucle) se ejecutan MIENTRAS la evaluación de la condición
# devuelva un resultado verdadero (True)
# - El ciclo se puede ejecutar 0 o más veces.

# REFRESCANDO LA MEMORIA:
# Estructuras de control: 
# 1) Condicionales (if, elif, else)
# 2) Repetitivas
#    a) While
#           i- Podemos iterar 0 o indefinida cantidad de veces.
#    b) For

# Mientras
# while condicion:
    # accion
    # accion
    # accion
    # accion
    # contador/bandera

# ----FOR

# Estructura:

# for variable in secuencia:
#       acción
#       acción

# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1

# Ejemplo con Listas:
# numeros = [4, 92, 52, 18, 30, 75]
# for num in numeros: 
#     print(num)


# Ejemplo con Strings:
# palabra = "Informatorio".lower() 
# cant_vocales = 0
# for letra in palabra:
#     if(letra == "a" or letra == "o" or letra == "i" or letra == "e" or letra == "u"):
#         cant_vocales+=1
#     print(letra)
# print(f"La palabra {palabra} tiene {cant_vocales} vocales.")


# Ejemplo con Diccionario: 
# estudiantes = {
#     "Luis" : "Dellamea",
#     "Galo" : "Guini",
#     "Esteban" : "Ortiz"
# }

# for estudiante in estudiantes:
#     print(estudiante)

# for estudiante in estudiantes.values():
#     print(estudiante)

# for nombre, apellido in estudiantes.items():
#     print(nombre, apellido)


# Ejemplo con un rango de numeros: 
# range()

# Pedi al usuario un numero e imprimi todos los valores incluyendo el numero ingresado.
# limite = int(input("Ingresar un numero:"))
# for i in range(1, limite+1):
#     print(i)

# break y Continue
# Nos ayuda a controlar el flujo de nuestra estructura repetitiva. 

# Break: 

# numeros = [1, 2, 3, 4, 5, 6]

# for num in numeros:
#     if(num == 3):
#         break
#     print(num)

# num_buscar = int(input("Ingresa el numero que queres buscar en la lista: "))

# for num in numeros:
#     print(num)
#     if num == num_buscar:
#         print("SI SE ENCUENTRA EL NUMERO")
#         break

# Continue:
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numeros: 
#     if num%2==0: 
#         continue
#     print(num)