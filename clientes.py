def es_numero(texto):
    """Si los numeros ingresados son menores a 0 o mayores que 9 el dni es invalido"""
    for caracter in texto:
        if caracter <"0" or caracter >"9":
            return False
    return True

def validar_dni(dni):
    if len(dni) == 8 and es_numero(dni):
        return True
    return  False

def  validar_telefono(telefono):
    if len(telefono) >= 8 and es_numero(telefono):
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
        return

    while not validar_telefono (telefono):
        print ("telefono invalido")
        telefono = input("ingrese nuevamente su telefono:")
        return

    while not validar_dni (dni):
        print("dni invalido")
        dni = input("ingrese nuevamente su dni:")
        return

    for cliente in clientes:
        if cliente [1] == dni:
            print ("Ya existe un cliente con ese dni ")
            return

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