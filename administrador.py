from functools import reduce
import os

administrador = {
    "nombre": "administrador",
    "dni": "42456789",
    "contraseña": "admin123"
}
def iniciar_sesion_admin(administrador):
    intentos_maximos = 3
    for intento in range(1, intentos_maximos +1):
        dni = input("Ingrese su DNI:")
        contraseña = input("Ingrese su contraseña:")
        if dni ==administrador["dni"] and contraseña == administrador["contraseña"]:
           print("¡¡¡Inicio de sesión exitoso!!!")
           print ("Bienvenido: ", administrador["nombre"])
           return True
        restantes = intentos_maximos - intento
        if restantes > 0:
            print("El DNI y la constraseña son incorrectos. Intentos restantes:", restantes)
    print("El DNI y la contraseña son incorrectos")
    return False

def mostrar_todas_reservas(reservas, clientes):
    """
    Muestra todas las reservas registradas.
    Para cada reserva se muestra el nombre del cliente si se encuentra
    registrado, además del DNI, cancha, fecha, horario y precio total.
    """
    if len(reservas)==0:
        print("No hay reservas registradas")
        return
    
    print("------------------")
    print("Todas las reservas")
    print("------------------")
    
    for reserva in reservas:
        nombre_cliente="Desconocido"
        
        for cliente in clientes:
            if cliente["dni"]== reserva[1]:
                nombre_cliente=cliente["nombre"]
                break
        
        print("Cliente: ", nombre_cliente)
        print("DNI: ", reserva[1])
        print("Cancha: ", reserva[0])
        print("Fecha: ", reserva[2])
        print("Horario: ", reserva[3], "-", reserva[4])
        print("Precio total: $", reserva[5])

def buscar_reservas_clientes(reservas, clientes):
    """
    Busca y muestra las reservas correspondientes a un cliente
    mediante su DNI.
    """
    if len(reservas)==0:
        print("No hay reservas registradas")
        return
    
    dni=input("Ingrese el DNI del cliente: ")
    nombre_cliente="Desconocido"
    
    for cliente in clientes:
        if cliente["dni"]==dni:
            nombre_cliente= cliente["nombre"]
            break
    
    reservas_encontradas = [reserva for reserva in reservas if reserva[1] == dni]
    
    print("---------------------")
    print("Reservas del cliente")
    print("---------------------")
    
    if not reservas_encontradas:
        print("No se encontraron reservas para ese DNI.")
        return
    
    for reserva in reservas_encontradas:
        print("Cliente:", nombre_cliente)
        print("DNI:", reserva[1])
        print("Cancha:", reserva[0])
        print("Fecha:", reserva[2])
        print("Horario:", reserva[3], "-", reserva[4])
        print("Precio total: $", reserva[5])
        
def buscar_reservas_cancha(reservas, canchas):
    """
    Busca y muestra todas las reservas realizadas para una cancha
    mediante su número.
    """
    if len(reservas)==0:
        print("No hay reservas registradas")
        return
    
    try:
        numero_cancha = int(input("Ingrese el número de la cancha: "))
    except ValueError:
        print("Debe ingresar un número de cancha válido.")
        return
    
    existe_cancha = any(cancha["numero"] == numero_cancha for cancha in canchas)
    
    if not existe_cancha:
        print("No existe una cancha con ese número")
        return
    
    reservas_encontradas=[ reserva for reserva in reservas if reserva[0] == numero_cancha]
    
    print("---------------------")
    print("Reservas de la cancha")
    print("---------------------")
    
    if not reservas_encontradas:
        print("La cancha existe, pero no tiene reservas")
        return
    
    for reserva in reservas:
        if reserva[0] == numero_cancha:
            print("Cliente:", reserva[0])
            print("DNI:", reserva[1])
            print("Fecha:", reserva[2])
            print("Horario:", reserva[3], "-", reserva[4])
            print("Precio total: $", reserva[5])

        
def calcular_recaudacion(reservas):
    """
    Calcula la recaudación total de todas las reservas.
    """
    precios = [reserva[5] for reserva in reservas]
    recaudacion = reduce(lambda total, precio: total + precio, precios, 0)
    return recaudacion 


def recaudacion_por_cancha(reservas, canchas):
    """Devuelve la recaudación de cada cancha, incluyendo las que recaudaron $0."""
    recaudacion = {}

    for cancha in canchas:
        recaudacion[cancha["numero"]] = 0

    for reserva in reservas:
        numero_cancha = reserva[0]
        precio = reserva[5]

        if numero_cancha not in recaudacion:
            recaudacion[numero_cancha] = 0

        recaudacion[numero_cancha] += precio

    return recaudacion


def cantidad_reservas(reservas):
    """
    Retorna la cantidad total de reservas registradas.
    """
    return len(reservas)

def reservas_por_cliente(reservas, clientes):
    """
    Muestra cuántas reservas tiene cada cliente registrado.
    """
    if len(clientes)==0:
        print("No hay clientes registrados")
        return
    
    dnis_con_reservas=set() #pregunto
    for reserva in reservas:
        dnis_con_reservas.add(reserva[1])
        
    print("--------------------")
    print("Reservas por cliente")
    print("--------------------")
    
    for cliente in clientes:

        reservas_cliente = list(
            filter(lambda reserva: reserva[1] == cliente["dni"], reservas)
        )

        cantidad = len(reservas_cliente)

        print("Cliente: ", cliente["nombre"])
        print("DNI: ", cliente["dni"])
        print("Cantidad de reservas: ", cantidad)
    print("Calcular de clientes con reservas: ", len(dnis_con_reservas))
        
def cancha_mas_reservada(reservas, canchas):
    """
    Determina cuál es la cancha que tiene mayor cantidad de reservas.
    Retorna el número de la cancha más reservada.
    """
    if len(reservas)==0:
        print("No hay reservas registradas")
        return None

    if len(canchas)==0:
        print("No hay canchas registradas")
        return None
    
    cancha_mas_reservada_numero=None
    mayor_cantidad=0
    
    for cancha in canchas:
        cantidad=0
        
        for reserva in reservas:
            if reserva[0]==cancha["numero"]:
                cantidad+=1
        
        if cantidad > mayor_cantidad:
            mayor_cantidad= cantidad
            cancha_mas_reservada_numero= cancha["numero"]
    
    if cancha_mas_reservada_numero is None:
        print("Ninguna cancha tiene reservas")
        return None
    
    print("--------------------")
    print("Cancha mas reservada")   
    print("--------------------")
    print("Cancha: ", cancha_mas_reservada_numero)
    print("Cantidad de reservas: ", mayor_cantidad)
    
    return cancha_mas_reservada_numero

def mostrar_canchas_nunca_reservadas(reservas, canchas):
    """Muestra las canchas que todavía no tienen reservas."""
    print("\nCanchas que nunca fueron reservadas:")
    hay_sin_reservas = False

    for cancha in canchas:
        tiene_reservas = False
        for reserva in reservas:
            if reserva[0] == cancha["numero"]:
                tiene_reservas = True
                break
        if not tiene_reservas:
            print("Cancha:", cancha["numero"])
            hay_sin_reservas = True

    if not hay_sin_reservas:
        print("Todas las canchas tienen al menos una reserva.")


def generar_reporte(reservas, clientes, canchas):
    """Muestra el reporte general y lo guarda en un archivo de texto."""
    lineas = []
    lineas.append("===============")
    lineas.append("REPORTE GENERAL")
    lineas.append("===============")
    lineas.append("Cantidad total de reservas: " + str(cantidad_reservas(reservas)))
    lineas.append(f"Recaudación total: $ {calcular_recaudacion(reservas):.2f}")

    lineas.append("")
    lineas.append("RESERVAS POR CLIENTE")

    if len(clientes) == 0:
        lineas.append("No hay clientes registrados")
    else:
        dnis_con_reservas = set()

        for reserva in reservas:
            dnis_con_reservas.add(reserva[1])

        for cliente in clientes:
            reservas_cliente = list(
                filter(lambda reserva: reserva[1] == cliente["dni"], reservas)
            )
            cantidad = len(reservas_cliente)

            lineas.append("Cliente: " + cliente["nombre"])
            lineas.append("DNI: " + cliente["dni"])
            lineas.append("Cantidad de reservas: " + str(cantidad))
            lineas.append("--------------------")

        lineas.append("Cantidad de clientes con reservas: " + str(len(dnis_con_reservas)))

    lineas.append("")
    lineas.append("CANCHA MÁS RESERVADA")

    if len(reservas) == 0:
        lineas.append("No hay reservas registradas")
    elif len(canchas) == 0:
        lineas.append("No hay canchas registradas")
    else:
        cancha = None
        mayor_cantidad = 0

        for cancha_actual in canchas:
            cantidad = 0

            for reserva in reservas:
                if reserva[0] == cancha_actual["numero"]:
                    cantidad += 1

            if cantidad > mayor_cantidad:
                mayor_cantidad = cantidad
                cancha = cancha_actual["numero"]

        if cancha is None:
            lineas.append("Ninguna cancha tiene reservas")
        else:
            lineas.append("Cancha: " + str(cancha))
            lineas.append("Cantidad de reservas: " + str(mayor_cantidad))

    lineas.append("")
    lineas.append("RECAUDACIÓN POR CANCHA")
    recaudacion = recaudacion_por_cancha(reservas, canchas)

    if len(recaudacion) == 0:
        lineas.append("No hay canchas registradas")
    else:
        for numero in sorted(recaudacion):
            lineas.append(
                f"Cancha {numero} - Recaudación: $ {recaudacion[numero]:.2f}"
            )

    lineas.append("")
    lineas.append("CANCHAS QUE NUNCA FUERON RESERVADAS")
    numeros_reservados = [reserva[0] for reserva in reservas]
    hay_sin_reservas = False

    if len(canchas) == 0:
        lineas.append("No hay canchas registradas")
    else:
        for cancha in canchas:
            if cancha["numero"] not in numeros_reservados:
                lineas.append("Cancha: " + str(cancha["numero"]))
                hay_sin_reservas = True

        if not hay_sin_reservas:
            lineas.append("Todas las canchas tienen al menos una reserva.")

   
    contenido_reporte = "\n".join(lineas)

    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(carpeta_actual, "reporte_general.txt")

    try:
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_reporte)

        print("Reporte guardado correctamente.")
        print("Ubicación:", ruta_archivo)

    except OSError as error:
        print("No se pudo guardar el reporte.")
        print("Error:", error)

    print("\n" + contenido_reporte)

