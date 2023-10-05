
# def str_to_int(list):
#     int_lista = []
#     for valor in list:
#         int_lista.append(int(valor))
#     return int_lista

def sumar(*args):
    resultado=0 
    for num in args:
        resultado += num
    return resultado

def restar(*args):
    pass

def multiplicar(*args):
    pass

def operaciones(config):
    if config["operacion"] == 1:
        resultado = sumar(*config["valores"])
        print(f"El resultado de la operacion es: {resultado}\n")

    elif config["operacion"] == 2:
        resultado = restar(*config["valores"])
        print(f"El resultado de la operacion es: {resultado}\n")

    elif config["operacion"] == 3:
        resultado = multiplicar(*config["valores"])
        print(f"El resultado de la operacion es: {resultado}\n")

    else:
        print("Dale flaquito, leeme bien el mensajito. \nIngresa la operacion correspondiente.")



def menu():
    menu_msg = ''' Ingresa el NUMERO de operacion que desea realizar: 
    1) Suma
    2) Resta
    3) Multiplicacion
    '''
    print(menu_msg)
    operacion = int(input("-> "))
    valores = input("Ingresa los valores a operar: ").split() 
    valores = [ int(valor) for valor in valores ]
    return { "operacion": operacion , "valores" : valores }



def calculadora():
    bandera = True
    while bandera:
        
        config = menu()
        # config = { "operacion": 1 , "valores" : [1, 4, 2, 6, 8] }
        operaciones(config)
        
        salir = input("¿Deseas continuar? \nPresiona ENTER si queres continuar\nó ingresa cualquier caracter para salir.\n-> ")
        # Si la variable salir TIENE un dato dentro -> True porque EXISTE
        # Si la variable salir NO TIENE un dato dentro -> False porque no EXISTE
        if salir:
            bandera=False
        else:
            bandera=True


calculadora()


