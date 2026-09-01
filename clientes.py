import re

def es_numero(texto):
    """Si los numeros ingresados son menores a 0 o mayores que 9 el dni es invalido"""
    for caracter in texto:
        if caracter <"0" or caracter >"9":
            return False
    return True

def validar_dni(dni):
    patron = r"^\d{8}$"
    if re.match(patron,dni):
        return True
    return False

def  validar_telefono(telefono):
    patron = r"^\d{8,}$"
    if re.match(patron, telefono):
        return True
    return False

def validar_nombre(nombre):
    if len(nombre) >=3:
        return True
    return False

def registrar_clientes(clientes):
    nombre = input ("Ingrese su nombre:")
    dni = input("Ingrese su dni:")
    telefono = input("ingrese su numero de telefono:")

    while not validar_nombre(nombre):
        print ("nombre invalido")
        nombre = input("ingrese nuevamente su nombre:")

    while not validar_telefono (telefono):
        print ("telefono invalido")
        telefono = input("ingrese nuevamente su telefono:")

    while not validar_dni (dni):
        print("dni invalido")
        dni = input("ingrese nuevamente su dni:")

    for cliente in clientes:
        if cliente [1] == dni:
            print ("Ya existe un cliente con ese dni ")

    nuevo_cliente = [
        nombre,
        dni,
        telefono,
    ]

    clientes.append(nuevo_cliente)
    print ("cliente registrado correctamente")

def iniciar_sesion_cliente(clientes):
    dni = input("ingrese su dni:")
    for cliente in clientes:
        if cliente[1] == dni:
            print("inicio de sesion exitoso")
            print("bienvenido/a", cliente[0])
            return cliente
    print("no existe un cliente registrado con este dni")
    return None