administador = [
    "administrador",
    "42456789",
    "admin123"
]
def iniciar_sesion_admin(administrador):
    dni = input("Ingrese su DNI:")
    contraseña = input("Ingrese su contraseña:")
    if dni ==administador[1] and contraseña == administador[2]:
        print("¡¡¡Inicio de sesión exitoso!!!")
        print ("Bienvenido: ", administador[0])
        return True
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
            if cliente[1]== reserva[1]:
                nombre_cliente=cliente[0]
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
    encontrado=False
    nombre_cliente="Desconocido"
    
    for cliente in clientes:
        if cliente[1]==dni:
            nombre_cliente= cliente[0]
            break
    
    print("---------------------")
    print("Reservas del cliente")
    print("---------------------")
    
    for reserva in reservas:
        if reserva[1] == dni:
            print("Cliente:", nombre_cliente)
            print("DNI:", reserva[1])
            print("Cancha:", reserva[0])
            print("Fecha:", reserva[2])
            print("Horario:", reserva[3], "-", reserva[4])
            print("Precio total: $", reserva[5])
            encontrado = True
    if not encontrado:
        print("No se encontraron reservas para ese DNI")
        
def buscar_reservas_cancha(reservas, canchas):
    """
    Busca y muestra todas las reservas realizadas para una cancha
    mediante su número.
    """
    if len(reservas)==0:
        print("No hay reservas registradas")
        return
    
    numero_cancha=int(input("Ingrese el número de la cancha: "))
    existe_cancha=False
    
    for cancha in canchas:
        if cancha[0]== numero_cancha:
            existe_cancha=True
            break
        
    if not existe_cancha:
        print("No existe una cancha con ese número")
        return
    encontrado=False
    
    print("---------------------")
    print("Reservas de la cancha")
    print("---------------------")
    
    for reserva in reservas:
        if reserva[0] == numero_cancha:
            print("Cliente:", reserva[0])
            print("DNI:", reserva[1])
            print("Fecha:", reserva[2])
            print("Horario:", reserva[3], "-", reserva[4])
            print("Precio total: $", reserva[5])
            encontrado = True
    if not encontrado:
        print("La cancha existe, pero no tiene reservas")
        
def calcular_recaudacion(reservas):
    """
    Calcula la recaudación total de todas las reservas.
    """
    recaudacion=0
    for reserva in reservas:
        recaudacion+= reserva[5]
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
    
    print("--------------------")
    print("Reservas por cliente")
    print("--------------------")
    
    for cliente in clientes:
        cantidad=0
        
        for reserva in reservas:
            if reserva[1]==cliente[1]:
                cantidad+=1

        print("Cliente: ", cliente[0])
        print("DNI: ", cliente[1])
        print("Cantidad de reservas: ", cantidad)
        
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
    
    cancha_mas_reservada_numero=0
    mayor_cantidad=0
    
    for cancha in canchas:
        cantidad=0
        
        for reserva in reservas:
            if reserva[0]==cancha[0]:
                cantidad+=1
        
        if cantidad > mayor_cantidad:
            mayor_cantidad= cantidad
            cancha_mas_reservada_numero= cancha[0]
    
    if cancha_mas_reservada_numero is None:
        print("Ninguna cancha tiene reservas")
        return None
    
    print("--------------------")
    print("Cancha mas reservada")   
    print("--------------------")
    print("Cancha: ", cancha_mas_reservada_numero)
    print("Cantidad de reservas: ", mayor_cantidad)
    
    return cancha_mas_reservada_numero

def generar_reporte(reservas, clientes, canchas):
    """
    Genera un reporte general con los principales datos del sistema:
    cantidad de reservas, recaudación total, reservas por cliente
    y cancha más reservada.
    """
    print("===============")
    print("REPORTE GENERAL")    
    print("===============")
    
    print("Cantidad total de reservas: ", cantidad_reservas(reservas))
    print("Recaudación total: $ ", calcular_recaudacion(reservas))
    
    print("Reservas por cliente:")
    reservas_por_cliente(reservas, clientes)
    
    print("Cancha mas reservada:")
    cancha_mas_reservada(reservas, canchas)