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
    dni = input("Ingrese su DNI:")
    telefono = input("Ingrese su número de teléfono:")

    while not validar_nombre(nombre):
        print ("Nombre inválido")
        nombre = input("Ingrese nuevamente su nombre:")
        return

    while not validar_telefono (telefono):
        print ("Teléfono inválido")
        telefono = input("Ingrese nuevamente su teléfono:")
        return

    while not validar_dni (dni):
        print("DNI inválido")
        dni = input("Ingrese nuevamente su DNI:")
        return

    for cliente in clientes:
        if cliente [1] == dni:
            print ("Ya existe un cliente con ese DNI ")
            return

    nuevo_cliente = [
        nombre,
        dni,
        telefono,
    ]

    clientes.append(nuevo_cliente)
    print ("Cliente registrado correctamente")

def iniciar_sesion_cliente(clientes):
    dni = input("Ingrese su dni:")
    for cliente in clientes:
        if cliente[1] == dni:
            print("Inicio de sesión exitoso")
            print("Bienvenido/a: ", cliente[0])
            return cliente
    print("No existe un cliente registrado con este DNI")
    return None