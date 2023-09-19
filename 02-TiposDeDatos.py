# Las variables son espacios de memoria donde almacenamos datos.

# Que sería eso? Que nosotros vamos a crear una variable, 
# y en ella vamos a guardar un valor que querramos
# Piensen que cuando crean una variable es porque
# le ponen nombre a una caja y en la caja van a guardar algo
# por ejemplo: 
caja_uno = "Ropa de Invierno"

# Estructura de una variable.
# <nombre_variable> = <valor>

# Esta variable va a llevar un listado de las ropas de invierno.
caja_ropa_invierno = ["gorro", "camiseta", "guantes"]


# Los datos son los "valores" que le damos a la variable. 
# Y claramente no es lo mismo darle a una variable 
# el valor "hola" que un 10. Son diferentes, con un 10 podemos hacer
# operaciones matemáticas y "hola" es un texto. 
# Esos son los tipos de datos que vamos a ver ahora: 

# Los tipos de datos básicos de python son: 
        # Numéricos (int, float, complex)
                # int -> integer = Entero.     Ej: 2 19 4 20 19239129391239129391239. 
                # float -> Decimales.          Ej:  2.424 - 19.2 - 4.1
        # Booleanos (bool) True y False
        # Cadena de caracteres (str)
                # str -> string -> cadena. ej. "hola" "pizza" "2" "19"
                # "2" + "2" != 2 + 2


##### Tipos de datos: 

### int (Enteros):
un_numero = 10
print(un_numero)
print(type(un_numero))

### Convertir a int -> int()
un_float = 9.1234
float_to_int = int(un_float)

### Float:
num_float = 0.12035
print(num_float)
print(type(num_float))

### Booleanos:
# Se puede declarar variables booleanas:
x = True
# Evaluar una expresión me devuelve un booleano también:
print(1 > 0) #True
print(1 <= 0) #False
print(9 == 9) #True

### Uso con if:
if x:
    print('Es True')
else:
    print('No lo es')



### Cadena de caracteres o Strings:
nombre = "Franco"
segundo_nombre = 'Agustin'
texto = ''' 
        Oracion 1
        Oracion 2
        Oracion 3
        '''
# Secuencias de escape: (\)
s_escape = "Esto es un ejemplo de \" dentro de comillas"
print(s_escape)

# lo mismo con \n
s_escape = "Esto es una oración \ny esta oración irá abajo"


### Formateo de cadenas:
# 1) + y str()
x = 5
texto = "El número es: "+ str(x)
print(texto)
# 2) format
texto = "Los números son {} y {}".format(5, 10)
# 3) nombrar los elementos y format
texto = "Los números son {a} y {b}".format(a=5, b=10)
# 4) fstrings
a=5
b=10
texto = f"Los números son {a} y {b}"


### Ejemplos Operaciones con strings:
# Suma
oracion = "Hola, me llamo"+" "+"Franco" #"Hola, me llamo Franco"
# Multiplicación
saludo_excesivo = "Hola" * 3 #"HolaHolaHola"
# Longitud con len()
cant_letras = len("Franco") #6

### Conjuntos o set
# Los conjuntos son colecciones de elementos únicos y no ordenados.
# Se crean utilizando llaves {} o la función set().
# Útiles para eliminar duplicados y verificar la pertenencia de elementos.
mi_set = {1, 2, 3, 3, 4}
print(mi_set)  # Salida: {1, 2, 3, 4}

### Listas o List
# Las listas son colecciones ordenadas y mutables de elementos.
# Se crean utilizando corchetes [].
# Útiles para almnacear secuencias de datos.
mi_lista = [1, 2, 3, 4]
print(mi_lista)  # Salida: [1, 2, 3, 4]

### Tuplas o Tuples
# Las tuplas son colecciones ordenadas e inmutables de elementos.
# Se crean utilizando paréntesis ().
# Útiles cuando los datos no deben cambiar.
mi_tupla = (1, 2, 3)
print(mi_tupla[0])  # Salida: 1

### Diccionarios o Dict
# Los diccionarios son colecciones de pares clave-valor.
# Se crean utilizando llaves {} con la sintaxis clave: valor.
# Útiles para almacenar y recuperar datos de forma eficiente.
mi_dict = {
    'nombre': 'Juan', 
    'edad': 30
    }

print(mi_dict['nombre'])  # Salida: 'Juan'

### None
# None es un valor especial que representa la ausencia de un valor o un valor nulo en Python.
# Se utiliza en variables o como valor de retorno de funciones cuando no hay un valor significativo para asignar.
valor = None
if valor is None:
    print("El valor es nulo.")
