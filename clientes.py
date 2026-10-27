import re

def es_numero(texto):
    """ Verifica que todos los caracteres ingresados sean números. 
    Parámetros: texto: cadena de caracteres que se desea verificar. 
    Retorna: True si todos los caracteres son números del 0 al 9. False si se encuentra algún carácter que no sea numérico."""
    for caracter in texto:
        if caracter <"0" or caracter >"9":
            return False
    return True

def validar_dni(dni):
    """ Verifica que el DNI tenga exactamente 8 dígitos numéricos. 
    Parámetros: dni: DNI del cliente que se desea validar. 
    Retorna: True si el DNI tiene exactamente 8 números. 
    False si no cumple con el formato. """
    patron = r"^\d{8}$"
    if re.match(patron,dni):
        return True
    return False

def  validar_telefono(telefono):
    """ Verifica que el número de teléfono tenga al menos 8 dígitos numéricos. 
    Parámetros: telefono: número de teléfono que se desea validar. 
    Retorna: True si el teléfono tiene 8 o más dígitos. False si no cumple con el formato. """
    patron = r"^\d{8,}$"
    if re.match(patron, telefono):
        return True
    return False

def validar_nombre(nombre):
    """
    Verifica que el nombre tenga al menos 3 caracteres
    y que contenga únicamente letras y espacios.
    Parámetros:nombre: nombre del cliente que se desea validar.
    Retorna:True si el nombre tiene 3 o más caracteres y contiene únicamente letras y espacios.
    False si no cumple con estas condiciones.
    """
    patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$"

    if len(nombre) >= 3 and re.match(patron, nombre):
        return True
    return False

def validar_contraseña(contraseña):
    """ Verifica que la contraseña tenga al menos 6 caracteres. 
    Parámetros: contraseña: contraseña que se desea validar. 
    Retorna: True si la contraseña tiene 6 o más caracteres. False si no cumple con el formato. """
    if len(contraseña) >= 6:
        return True
    return False

def pedir_dato(mensaje, validador, mensaje_error):
    """ Pide un dato por teclado y lo vuelve a pedir hasta que sea valido.
    Si el dato no pasa la validacion, lanza una excepcion ValueError y la captura para mostrar el mensaje de error al usuario.
    Parametros: mensaje: texto que se muestra al pedir el dato.
    validador: funcion que recibe el dato y retorna True si es valido.
    mensaje_error: texto que se muestra si el dato es invalido.
    Retorna: el dato ingresado ya validado"""

    while True:
        try:
            dato = input(mensaje)
            if not validador(dato):
                raise ValueError(mensaje_error)
            return dato
        except ValueError as error:
            print("Error en el dato ingresado")

def pedir_dni_nuevo(clientes):
    """ Pide un DNI y lo vuelve a pedir hasta que tenga formato valido y no este registrado. Usa excepciones ValueError para ambos casos.
    Parametros: clientes: lista que contiene diccionarios con los datos de los clientes registrados.
    Retorna: un DNI de 8 digitos que no existe en la lista de clientes. """

    while True:
        try: 
            dni = input("Ingrese su DNI: ")
            if not validar_dni(dni):
                raise ValueError("DNI invalido: deben ser 8 digitos numericos")
            for cliente in clientes:
                if cliente["dni"] == dni:
                    raise ValueError("Ya existe un cliente con ese DNI")
            return dni
        except ValueError as error:
            print(error)

def registrar_clientes(clientes):
    """ 
    Solicita los datos de un nuevo cliente y lo registra en la lista. Se solicitan el nombre, DNI, número de teléfono y contraseña del cliente. 
    Cada dato se valida en el momento en que se ingresa, antes de pedir el siguiente. 
    Parámetros: clientes: lista que contiene diccionarios con los datos de los clientes registrados. 
    Retorna: No retorna ningún valor. Agrega el nuevo cliente a la lista recibida como parámetro. 
    """
    nombre = pedir_dato ("Ingrese su nombre:", validar_nombre, "Nombre invalido: minimo 3 letras, sin numeros ni simbolos")
    dni = pedir_dni_nuevo (clientes)
    telefono = pedir_dato("Ingrese su número de teléfono:", validar_telefono, "Telefono invalido: minimo 8 digitos numericos")
    contraseña = pedir_dato("Cree su contraseña: "), validar_contraseña, "Contraseña invalida: minimo 6 caracteres"

    nuevo_cliente = {
    "nombre": nombre,
    "dni": dni,
    "telefono": telefono,
    "contraseña": contraseña
    }

    clientes.append(nuevo_cliente)
    print ("Cliente registrado correctamente")

def iniciar_sesion_cliente(clientes):
    """ 
    Permite iniciar sesión a un cliente utilizando su DNI y contraseña. 
    Primero se solicita el DNI, con un máximo de 3 intentos para ingresar uno registrado. 
    Luego se solicita la contraseña, también con un máximo de 3 intentos, sin volver a pedir el DNI. 
    Parámetros: clientes: lista que contiene diccionarios con los datos de los clientes registrados. 
    Retorna: El cliente encontrado si el DNI y la contraseña son correctos. None si se agotan los intentos. 
    """
    intentos_maximos = 3
    cliente_encontrado = None

    for intento in range(1, intentos_maximos + 1):
        dni = input("Ingrese su dni:")
        for cliente in clientes:
            if cliente["dni"] == dni:
                cliente_encontrado = cliente
        if cliente_encontrado is not None:
            break
        restantes = intentos_maximos - intento 
        if restantes > 0:
            print("No existe un cliente registrado con este DNI.")
    if cliente_encontrado is None:
        print("Demasiados intentos fallifos")
        return None

    for intento in range(1, intentos_maximos +1):
        contraseña = input("Ingrese su contraseña: ")
        if contraseña == cliente_encontrado["contraseña"]:
            print("Inicio de sesion exitoso")
            print("Bienvenido/a", cliente_encontrado["nombre"])
            return cliente_encontrado
        restantes = intentos_maximos - intento
        if restantes > 0:
            print("Contraseña incorrecta. Intentos restantes:", restantes)
    
    print("Demasiados intentos fallidos")
    return None