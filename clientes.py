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
            print(error)

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
    """ Solicita los datos de un nuevo cliente y lo registra en la lista. Se solicitan el nombre, DNI y número de teléfono del cliente. 
    Los datos son validados antes de realizar el registro. 
    Parámetros: clientes: lista que contiene diccionarios con los datos de los clientes registrados. 
    Retorna: No retorna ningún valor. Agrega el nuevo cliente a la lista recibida como parámetro. """
    nombre = input ("Ingrese su nombre:")
    dni = input("Ingrese su DNI:")
    telefono = input("Ingrese su número de teléfono:")

    nuevo_cliente = {
    "nombre": nombre,
    "dni": dni,
    "telefono": telefono
    }

    clientes.append(nuevo_cliente)
    print ("Cliente registrado correctamente")

def iniciar_sesion_cliente(clientes):
    """ Permite iniciar sesión a un cliente utilizando su DNI. Busca el DNI ingresado dentro de la lista de clientes registrados. 
    Si encuentra una coincidencia, devuelve los datos del cliente. 
    Parámetros: clientes: lista que contiene diccionarios con los datos de los clientes registrados. 
    Retorna: El cliente encontrado si el DNI coincide. None si no existe un cliente registrado con ese DNI. """
    dni = input("Ingrese su dni:")
    for cliente in clientes:
        if cliente["dni"] == dni:
            print("Inicio de sesión exitoso")
            print("Bienvenido/a: ", cliente["nombre"])
            return cliente
    print("No existe un cliente registrado con este DNI")
    return None