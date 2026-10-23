def existe_cancha(canchas, numero): 
    """
    Verifica si un número de cancha ya se encuentra registrado.
    Parámetros:
        canchas: lista de canchas registradas.
        numero: número de cancha que se desea verificar.
    Retorna:
        True si la cancha existe y False si no existe.
    """
    existe = False
    
    for cancha in canchas:
        if cancha["numero"] == numero:
            existe = True
    return existe

def pedir_numero():
    numero_valido = False

    while not numero_valido:
        try:
            numero = int(input("Ingrese el numero de cancha del 1 al 20: "))

            if numero < 1 or numero > 20:
                print("El numero debe estar entre 1 y 20")
            else: 
                numero_valido = True

        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
    
    return numero
    
def elegir_tipo_piso():
    """
    Muestra los tipos de piso disponibles y solicita al usuario que seleccione uno.
    Valida que la opción ingresada sea correcta.
    Retorna: El tipo de piso seleccionado: Cemento, Cesped sintetico o Resina.
    """
    print("Tipos de piso de las canchas: ")
    print("1. Cemento")
    print("2. Cesped sintético")
    print("3. Resina")
    
    numero_tipo_piso = input("Ingrese el número que identifica al tipo de piso: ")
    
    while numero_tipo_piso not in ["1", "2", "3"]:
        print("Opción inválida.")
        numero_tipo_piso = input("Ingrese nuevamente una opción: ")
    
    match numero_tipo_piso:
        case "1":
            tipo_piso = "Cemento"
        case "2":
            tipo_piso = "Cesped sintetico"
        case "3":
            tipo_piso = "Resina"

    return tipo_piso

def elegir_tipo_techo(): 
    """
    Muestra los tipos de techo disponibles y solicita al usuario que seleccione uno.
    Valida que la opción ingresada sea correcta.
    Retorna: El tipo de techo seleccionado: Techada o No techada.
    """

    print("Tipos de techo de las canchas: ")
    print("1. Techada")
    print("2. No techada")

    numero_tipo_techo = input("Ingrese el número que identifica al tipo de techo: ")

    while numero_tipo_techo not in ["1", "2"]:
        print("Opción inválida.")
        numero_tipo_techo = input("Ingrese nuevamente una opción: ")
        
    match numero_tipo_techo:
        case "1":
            tipo_techo = "Techada"
        case "2":
            tipo_techo = "No techada"
    return tipo_techo

def pedir_opcion():
    opcion = input("¿Quiere registrar una cancha? Ingrese 1 para SI y 2 para NO: ")

    while opcion != "1" and opcion != "2":
        opcion = input("Opción inválida, ingrese 1 para SI y 2 para NO: ")

    return opcion

def pedir_numero_cancha(canchas):
        
    numero_valido = False

    while not numero_valido:
        try:
            numero = int(input("Ingrese un número del 1 al 20 para identificar la cancha: "))

            if numero < 1 or numero > 20:
                print("Número inválido. Debe estar entre 1 y 20.")

            else:
                existe = existe_cancha(canchas, numero)

                if existe:
                    print("Ya existe una cancha con ese número de identificación. Ingrese otro.")
                else:
                    numero_valido = True

        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")
    
    return numero

def pedir_precio():
    
    precio_valido = False

    while not precio_valido:
        try:
            precio = float(input("Ingrese el precio por hora: "))

            if precio > 0:
                precio_valido = True
            else:
                print("El precio debe ser mayor que cero.")

        except ValueError:
            print("Entrada inválida. Debe ingresar un precio numérico.")
    return precio

def registrar_cancha(canchas):
    """
    Permite registrar una o más canchas en el sistema.
    Solicita el número de cancha, verifica que no esté registrado previamente,
    permite seleccionar el tipo de piso y techo, solicita el precio por hora
    y registra la cancha con estado Disponible.
    Parámetros:
        canchas: lista donde se almacenan las canchas registradas.
    Retorna:
        No retorna ningún valor. Modifica la lista canchas.
    """

    opcion = pedir_opcion()

    while opcion == "1":

        # numero de cancha
        numero = pedir_numero_cancha(canchas)

        #Llamando a la funcion de tipo de piso
        tipo_piso = elegir_tipo_piso()

        # Llamando a al funcion de tipos de techo
        tipo_techo = elegir_tipo_techo()

        # precio
        precio = pedir_precio()

        nueva_cancha = {"numero": numero, "piso": tipo_piso, "techo": tipo_techo, "precio": precio, "estado": "Disponible"}
        canchas.append(nueva_cancha)

        print("Cancha registrada correctamente.")

        opcion = input("¿Quiere registrar otra cancha? Ingresar 1 para SI y 2 para NO: ")

    

def mostrar_canchas(canchas):
    """
    Muestra los datos de todas las canchas registradas.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        No retorna ningún valor. Muestra la información en pantalla.
    """

    if len(canchas) == 0:
        print("No hay canchas registradas.")
    else:

        canchas_ordenadas = canchas.copy() #uso copy para no modificar la lista original, sino que crearme una copia para modificar

        canchas_ordenadas.sort(key=lambda cancha: cancha["numero"])

        print("\n--- CANCHAS REGISTRADAS ---")
        for cancha in canchas_ordenadas:
            print("Número de cancha:", cancha["numero"])
            print("Tipo de piso:", cancha["piso"])
            print("Tipo de techo:", cancha["techo"])
            print("Precio por hora: $", cancha["precio"])
            print("Estado:", cancha["estado"])
            print("--------------------------")

def buscar_cancha(canchas):
    """
    Permite buscar una cancha mediante su número.
    Muestra los números de las canchas registradas, solicita al usuario
    el número que desea buscar y, si existe, muestra todos sus datos.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        No retorna ningún valor. Muestra el resultado de la búsqueda en pantalla.
    """

    if len(canchas) == 0:
        print("No hay canchas registradas.")
    else:
        print("Canchas registradas:")

        for cancha in canchas:
            print("Cancha N°", cancha["numero"])

        numero_a_buscar = pedir_numero()

        encontrada = False

        for cancha in canchas:
            if cancha["numero"] == numero_a_buscar:
                encontrada = True

                print("\n--- CANCHA ENCONTRADA ---")
                print("Número:", cancha["numero"])
                print("Tipo de piso:", cancha["piso"])
                print("Tipo de techo:", cancha["techo"])
                print("Precio por hora: $", cancha["precio"])
                print("Estado:", cancha["estado"])
                print("-------------------------")

        if encontrada == False:
            print("No existe una cancha con ese número.")

def buscar_posicion_cancha(canchas, numero):
    """
    Busca la posición de una cancha dentro de la lista utilizando su número.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
        numero: número de cancha que se desea buscar.
    Retorna:
        La posición de la cancha si se encuentra registrada.
        Retorna -1 si la cancha no existe.
    """

    for i in range(len(canchas)):
        if canchas[i]["numero"] == numero:
            return i
    return -1

def elegir_estado():
    """
    Permite seleccionar el estado de una cancha.
    El usuario puede elegir entre Disponible y No disponible.
    La función valida que la opción ingresada sea correcta.
    Retorna:
        El estado seleccionado: Disponible o No disponible.
    """
    print("Opciones de estado:")
    print("1. Disponible")
    print("2. No disponible")

    opcion = input("Ingrese una opción: ")

    while opcion != "1" and opcion != "2":
        print("Opción inválida.")
        opcion = input("Ingrese nuevamente una opción: ")

    match opcion:
        case "1":
            estado = "Disponible"
        case "2":
            estado = "No disponible"
    return estado


def mostrar_datos_cancha(cancha):
    """
    Muestra todos los datos correspondientes a una cancha.
    Parámetros:
        cancha: lista que contiene el número, tipo de piso, tipo de techo,
        precio por hora y estado de una cancha.
    Retorna:
        No retorna ningún valor. Muestra los datos en pantalla.
    """

    print("Número:", cancha["numero"])
    print("Tipo de piso:", cancha["piso"])
    print("Tipo de techo:", cancha["techo"])
    print("Precio por hora: $", cancha["precio"])
    print("Estado:", cancha["estado"])

def modificar_dato_cancha(canchas, pos):
    """
    Permite modificar un dato de una cancha determinada.
    El administrador puede modificar el tipo de piso, tipo de techo,
    precio por hora o estado de la cancha.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
        pos: posición de la cancha que se desea modificar.
    Retorna:
        No retorna ningún valor. Modifica directamente la cancha seleccionada.
    """
    
    print("\n¿Qué dato desea modificar?")
    print("1. Tipo de piso")
    print("2. Tipo de techo")
    print("3. Precio por hora")
    print("4. Estado")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            canchas[pos]["piso"] = elegir_tipo_piso()
        case "2":
            canchas[pos]["techo"] = elegir_tipo_techo()
        case "3":
            canchas[pos]["precio"] = float(input("Ingrese el nuevo precio por hora: "))
        case "4":
            canchas[pos]["estado"] = elegir_estado()
        case "5":
            print("No se realizaron modificaciones.")
        case _:
            print("Opción incorrecta.")

def modificar_cancha(canchas):
    """
    Permite seleccionar una cancha registrada y modificar sus datos.
    Solicita el número de cancha, busca su posición, muestra sus datos actuales
    y permite seleccionar qué información se desea modificar.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        No retorna ningún valor. Puede modificar los datos de una cancha.
    """

    if len(canchas) == 0:
        print("No hay canchas registradas.")
    else:
        print("Canchas registradas:")

        for cancha in canchas:
            print("Cancha N°", cancha["numero"])

        numero_a_modificar = pedir_numero()

        #Llamo a la funcion que vos le das el numero de cancha y te devuelva la posicion y si no la encuentra, que te de -1
        pos = buscar_posicion_cancha(canchas, numero_a_modificar)

        if pos == -1:
            print("No existe una cancha con ese número")

        else:
            print("\nDatos actuales de la cancha:")

            mostrar_datos_cancha(canchas[pos])

            modificar_dato_cancha(canchas, pos)

def eliminar_cancha(canchas):
    """
    Permite eliminar una cancha registrada.
    Solicita el número de cancha, verifica que exista, muestra sus datos
    y pide confirmación antes de eliminarla.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        No retorna ningún valor. Puede eliminar una cancha de la lista.
    """

    if len(canchas) == 0:
        print("No hay canchas registradas.")

    else:
        print("Canchas registradas:")

        for cancha in canchas:
            print("Cancha N°", cancha["numero"])

        numero_a_eliminar = pedir_numero()

        # Busco la posición de la cancha
        pos = buscar_posicion_cancha(canchas, numero_a_eliminar)

        if pos == -1:
            print("No existe una cancha con ese número.")
            input("Presione Enter para volver al menú...")
        else:
            print("\nDatos de la cancha que desea eliminar:")

            mostrar_datos_cancha(canchas[pos])

            opcion = input("¿Está seguro que desea eliminar esta cancha? Ingrese 1 para SI y 2 para NO: ")

            if opcion == "1":
                del canchas[pos]
                print("Cancha eliminada correctamente.")
            elif opcion == "2":
                print("No se eliminó la cancha.")
            else:
                print("Opción inválida.")

def obtener_canchas_disponibles(canchas):
    """
    Obtiene las canchas que se encuentran disponibles.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        Una lista con las canchas cuyo estado es Disponible.
    """
    disponibles = list(filter(lambda cancha: cancha["estado"] == "Disponible", canchas)) #va tomando cada cancha de canchas y pregunta:¿esta disponible? Si da True, la conserva. Si da False, no la incluye.

    return disponibles

def mostrar_disponibilidad(canchas):

    """
    Muestra las canchas que se encuentran disponibles.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
    Retorna:
        No retorna ningún valor. Muestra las canchas disponibles.
    """

    if len(canchas) == 0:
        print("No hay canchas registradas.")
    else:
        disponibles = obtener_canchas_disponibles(canchas)

        if len(disponibles) == 0:
            print("No hay canchas disponibles.")
        else:
            print("\n--- CANCHAS DISPONIBLES ---")
            for cancha in disponibles:
                print("Cancha N°", cancha["numero"])


def aumentar_precios(canchas, porcentaje):
    """
    Aumenta el precio por hora de todas las canchas registradas.
    Aplica el porcentaje de aumento indicado a cada cancha utilizando
    las funciones map() y lambda, y genera una nueva lista con los
    precios actualizados.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
        porcentaje: porcentaje que se desea aumentar a los precios.
    Retorna:
        Una nueva lista de canchas con los precios actualizados.
    """

    canchas_actualizadas = list(map(
        lambda cancha: {
            "numero": cancha["numero"],
            "piso":   cancha["piso"],
            "techo":  cancha["techo"],
            "precio": cancha["precio"] * (1 + porcentaje / 100),
            "estado": cancha["estado"]
            }, canchas
    ))

    return canchas_actualizadas
