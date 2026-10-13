from canchas import mostrar_canchas
from datetime import date, timedelta

DIAS_SEMANA=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

def verificar_numero_cancha(buscado,canchas):
    """Verifica si existe una cancha con el numero ingresado por el usuario
        Parámetros:
        buscado: número de cancha ingresado por el usuario.
        canchas: lista que contiene las canchas registradas.
        Retorna:True si existe una cancha con ese número.False si no existe.
    """
    for cancha in canchas: 
        if cancha[0] == buscado:
            return True
    return False

def obtener_precio_cancha(canchas,num_cancha):
    """Busca el precio por hora de una determinada cancha
        Parámetros:
        canchas: lista que contiene las canchas registradas.
        num_cancha: número de la cancha cuyo precio se desea obtener.
        Retorna:El precio por hora de la cancha indicada.
    """
    for cancha in canchas: 
        if cancha[0] == num_cancha:
            return cancha[3]

def generar_dias(cantidad):
    """Genera la lista de días disponibles para realizar reservas.
    Parte desde la fecha actual y avanza día por día, omitiendo los domingos,
    hasta completar la cantidad pedida. Así la lista se actualiza sola cada día.
    Parámetros:
        cantidad: cantidad de días que se desean generar.
    Retorna: lista de fechas de lunes a sábado.
    """
    dias=[]
    dia=date.today()
    while len(dias) < cantidad:
        if dia.weekday() != 6:
            dias.append(dia)
        dia += timedelta(days=1)
    return dias

def seleccionar_dia(dias):
    """Permite al usuario seleccionar el día en el que desea realizar la reserva.
    Muestra los días numerados junto con el nombre del día de la semana, y pide
    una opción hasta que el usuario ingrese un número válido.
    Parámetros:
        dias: lista de fechas (objetos date) disponibles para reservar.
    Retorna: la fecha (objeto date) seleccionada por el usuario.
    """
    print("Seleccione el día: ")
    for i,dia in enumerate(dias, start=1):
        nombre_dia=DIAS_SEMANA[dia.weekday()]
        print(f"{i} - {nombre_dia} {dia.strftime('%d/%m/%Y')}")
    while True:
        try:
            opcion=int(input("Ingrese una opcion: "))
            if 1 <= opcion <= len(dias):
                return dias[opcion - 1]
            print("La opcion ingresada no es valida")
        except ValueError:
            print("Debe ingresar un numero")

def validar_horario(horario_entrada,horario_salida):
    """Verifica que el horario este dentro del horario de funcionamiento y que la entrada sea menor que la salida
        Parámetros:
        horario_entrada: hora en la que comienza la reserva.
        horario_salida: hora en la que finaliza la reserva.
        Retorna:Los horarios de entrada y salida una vez validados.
    """
    validado = False
    while validado == False:
        if horario_entrada < 9 or horario_salida > 23:
            print("El horario debe estar entre las 9 y las 23.")
        elif horario_entrada >= horario_salida:
            print("El horario de entrada debe ser menor que al horario de salida")
        else:
            print("Horarios ingresados correctamente")
            validado=True

        if validado == False:
            horario_entrada=int(input("Ingrese nuevamente la hora de entrada: "))
            horario_salida=int(input("Ingrese nuevamente la hora de salida: "))

    return horario_entrada,horario_salida

def seleccionar_horario():
    """Solicita al usuario el horario de entrada y salida y valida los datos ingresados
        Retorna: El horario de entrada y el horario de salida validados
    """
    print("\nLos horarios disponibles son de 9 a 23.")

    horario_entrada=int(input("Ingrese el horario de entrada: "))
    horario_salida=int(input("Ingrese el horario de salida: "))

    return validar_horario(horario_entrada,horario_salida)


def verificar_horario_reserva(reservas, num_cancha, fecha, horario_entrada, horario_salida):
    """Verifica que el horario elegido no se superponga con otra reserva de la misma cancha y fecha
        Parámetros:
        reservas: lista que contiene las reservas realizadas.
        num_cancha: número de la cancha que se desea reservar.
        fecha: día en el que se desea realizar la reserva.
        horario_entrada: hora de inicio de la nueva reserva.
        horario_salida: hora de finalización de la nueva reserva.
    Retorna:True si el horario está disponible.False si existe una reserva que se superpone.
    """
    reservas_dia=list(filter(lambda reserva: reserva[0] == num_cancha and reserva[2] == fecha, reservas))

    for reserva in reservas_dia:
        if horario_entrada < reserva[4] and horario_salida > reserva[3]:
            return False
    return True

def calcular_precio(horario_entrada,horario_salida,precio_hora):
    """Calcula el precio total de una reserva segun la cantidad de horas reservada y el precio de una cancha.
        Parámetros:
        horario_entrada: hora de inicio de la reserva.
        horario_salida: hora de finalización de la reserva.
        precio_hora: precio de la cancha por una hora.
        Retorna:El precio total de la reserva. 
    """
    precio_total = (horario_salida - horario_entrada) * precio_hora

    return precio_total

def guardar_reserva(reservas,cliente,num_cancha,fecha,horario_entrada,horario_salida,precio_total):
    """Agrega una nueva reserva a la lista de reservas.
        Parámetros:
        reservas: lista que contiene las reservas realizadas.
        cliente: datos del cliente que realiza la reserva.
        num_cancha: número de la cancha reservada.
        fecha: día de la reserva.
        horario_entrada: hora de inicio de la reserva.
        horario_salida: hora de finalización de la reserva.
        precio_total: precio total de la reserva.
        Retorna:
        No retorna ningún valor. Agrega la nueva reserva a la lista.
    """
    nueva_reserva = [num_cancha,cliente[1],fecha,horario_entrada,horario_salida,precio_total]
    reservas.append(nueva_reserva)

def crear_reserva(canchas, reservas, cliente):
    """Permite al cliente crear una nueva reserva.
    Parámetros:
        canchas: lista que contiene las canchas registradas.
        reservas: lista que contiene las reservas realizadas.
        dias: lista de días disponibles.
        cliente: datos del cliente que realiza la reserva.
    Retorna:No retorna ningún valor. Guarda la nueva reserva en la lista.
    """

    print("\n================================")
    print("CREAR RESERVA")
    print("================================")

    # Genera dias
    dias=generar_dias(7)
    # Seleccionar día
    fecha = seleccionar_dia(dias)
    # Mostrar canchas
    mostrar_canchas(canchas)
    # Seleccionar cancha
    while True:
        try:
            num_cancha = int(input("\nIngrese el número de cancha: "))
            if num_cancha == 0:
                print("Reserva cancelada.")
                return
            if verificar_numero_cancha(num_cancha,canchas):
                break
            print("Ese numero de cancha no existe.")
        except ValueError:
            print("Debe ingresa un numero entero valido")

    # Seleccionar horario
    horario_entrada, horario_salida = seleccionar_horario()

    # Verificar disponibilidad
    while verificar_horario_reserva(reservas,num_cancha,fecha,horario_entrada,horario_salida) == False:

        print("\nEse horario ya está ocupado.")
        print("Por favor, seleccione otro horario.")

        horario_entrada, horario_salida = seleccionar_horario()

    # Obtener precio
    precio_hora = obtener_precio_cancha(canchas,num_cancha)

    # Calcular precio total
    precio_total = calcular_precio(horario_entrada,horario_salida,precio_hora)

    # Guardar reserva
    guardar_reserva(reservas,cliente,num_cancha,fecha,horario_entrada,horario_salida,precio_total)

    print("\n================================")
    print("   RESERVA REALIZADA")
    print("================================")
    print("Cliente:", cliente[0])
    print("DNI:", cliente[1])
    print("Cancha:", num_cancha)
    print("Fecha:", fecha)
    print("Horario:", horario_entrada, "-", horario_salida)
    print("Precio por hora: $", precio_hora)
    print("Precio total: $", precio_total)


def mostrar_reserva(reservas, cliente):
    """Esta funcion permite al usuario ver todas las reservas realizadas
    Parámetros:reservas: lista que contiene las reservas realizadas
    Retorna:No retorna ningún valor. Muestra las reservas en pantalla. 
    """
    mis_reservas=[reserva for reserva in reservas if reserva[1] == cliente[1]]
    if len(mis_reservas) == 0:
        print("No hay reservas realizadas")
    else:
        print("\n================================")
        print(" MIS RESERVAS ")
        print("================================")

        for reserva in mis_reservas:
            print("Cancha:", reserva[0])
            print("DNI:", reserva[1])
            print("Fecha:", reserva[2])
            print("Horario:", reserva[3], "-", reserva[4])
            print("Precio total: $", reserva[5])

            print("-------------------------------- ")


def cancelar_reserva(reservas, cliente):
    """Se cancela una reserva, ingresando numero de cancha, fecha y horario porque como se puede hacer varias
    reservas de la misma cancha se pide verificar con fecha y horario de entrada y luego se lo elimina de la matriz reserva
     Parámetros:
        reservas: lista que contiene las reservas realizadas.
        cliente: datos del cliente que desea cancelar la reserva.
    Retorna:No retorna ningún valor. Elimina la reserva si se encuentra.
    """

    mostrar_reserva(reservas,cliente)

    try:
        num_cancha = int(input("Ingrese el número de cancha (0 para salir): "))
        if num_cancha == 0:
            print("Operacion cancelada.")
            return
        fecha = input("Ingrese la fecha de la reserva: ")
        horario_entrada = int(input("Ingrese el horario de entrada: "))
    except ValueError:
        print("Dato invalido. Operacion cancelada.")
        return

    for reserva in reservas:
        if (cliente[1] == reserva[1] and num_cancha == reserva[0] and fecha == reserva[2] and horario_entrada == reserva[3]):
            reservas.remove(reserva)
            print("Reserva cancelada correctamente.")
            return

    print("No se encontró una reserva con esos datos.")
    
            



    










