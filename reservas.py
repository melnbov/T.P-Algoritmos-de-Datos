import json
import os
from canchas import mostrar_canchas
from datetime import date, timedelta
RUTA_RESERVAS = os.path.join(
    os.path.dirname(__file__), "reservas.json")
DIAS_SEMANA=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

#Archivo JSON

def guardar_reservas(reservas):
    """Guarda todas las reservas en el archivo reserva.json"""
    with open (RUTA_RESERVAS,"w",encoding="utf-8")as archivo:
        json.dump(reservas,archivo,indent=4,ensure_ascii=False)

def cargar_reservas():
    """Carga las reservas almacenadas en reservas.json. Si el archivo no existe, retorna una lista vacia"""
    try:
        with open(RUTA_RESERVAS,"r",encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return[]

#Validaciones

def verificar_numero_cancha(buscado,canchas):
    """Verifica si existe una cancha con el numero ingresado por el usuario
        Parámetros:
        buscado: número de cancha ingresado por el usuario.
        canchas: lista que contiene las canchas registradas.
        Retorna:True si existe una cancha con ese número.False si no existe.
    """
    for cancha in canchas: 
        if cancha["numero"] == buscado and cancha["estado"] == "Disponible":
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
        if cancha["numero"] == num_cancha:
            return cancha["precio"]

def generar_dias(cantidad):
    """
    Genera fechas disponibles para el dia actual, omitiendo los domingos
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
        except ValueError:
            print("Debe ingresar un numero")
            continue
        
        if 1 <= opcion <= len(dias):
            return dias[opcion - 1]
        print("La opcion ingresada no es valida")


def validar_horario(horario_entrada, horario_salida):
    """Verifica que el horario esté entre las 9 y las 23."""

    while True:
        if horario_entrada < 9 or horario_salida > 23:
            print("El horario debe estar entre las 9 y las 23.")
        elif horario_entrada >= horario_salida:
            print("La hora de entrada debe ser menor que la de salida.")
        else:
            print("Horarios ingresados correctamente")
            return horario_entrada, horario_salida

        try:
            horario_entrada = int(input("Ingrese nuevamente la hora de entrada: "))
            horario_salida = int(input("Ingrese nuevamente la hora de salida: "))
        except ValueError:
            print("Debe ingresar números enteros.")
            horario_entrada = 0
            horario_salida = 0


def seleccionar_horario():
    """Solicita al usuario el horario de entrada y salida y valida los datos ingresados
        Retorna: El horario de entrada y el horario de salida validados
    """
    print("\nLos horarios disponibles son de 9 a 23.")

    while True:
        try:
            horario_entrada = int(input("Ingrese el horario de entrada: "))
            horario_salida = int(input("Ingrese el horario de salida: "))

            return validar_horario(horario_entrada, horario_salida)

        except ValueError:
            print("Debe ingresar números enteros.")


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
    reservas_dia=list(filter(lambda reserva:reserva["numero_cancha"] == num_cancha 
                                and reserva["fecha"] == fecha.isoformat() and reserva["estado"] == "Activa",reservas))

    for reserva in reservas_dia:
        if horario_entrada < reserva["hora_fin"] and horario_salida > reserva["hora_inicio"]:
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
        Crea una reserva utilizando un diccionario y la agrega a la lista.
        Luego actualiza el archivo JSON.
    """
    
    nueva_reserva = {
        "numero_cancha":num_cancha,
        "dni_cliente": cliente["dni"],
        "fecha": fecha.isoformat(),
        "hora_inicio": horario_entrada,
        "hora_fin": horario_salida,
        "precio_total": precio_total,
        "estado": "Activa"
    }
    reservas.append(nueva_reserva)
    guardar_reservas(reservas)

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
            num_cancha = int(input("\nIngrese el número de cancha (0 para salir): "))
            if num_cancha == 0:
                print("Reserva cancelada.")
                return
            if verificar_numero_cancha(num_cancha,canchas):
                break
            print("La cancha no existe o no se encuentra disponible")
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
    print("Cliente:", cliente["nombre"])
    print("DNI:", cliente["dni"])
    print("Cancha:", num_cancha)
    print("Fecha:", fecha)
    print("Horario:", horario_entrada, "-", horario_salida)
    print("Precio por hora: $", precio_hora)
    print("Precio total: $", precio_total)

    print("\nLa reserva quedo guardada correctamente.")

def mostrar_reserva(reservas, cliente):
    """Esta funcion permite al usuario ver todas las reservas realizadas
    Parámetros:reservas: lista que contiene las reservas realizadas
    Retorna:No retorna ningún valor. Muestra las reservas en pantalla. 
    """
    mis_reservas = list(filter(lambda reserva:reserva["dni_cliente"] == cliente["dni"] and reserva["estado"] == "Activa", reservas))
    if len(mis_reservas) == 0:
        print("No hay reservas realizadas")
    else:
        print("\n================================")
        print(" MIS RESERVAS ")
        print("================================")

        for reserva in mis_reservas:
            print("Cancha:", reserva["numero_cancha"])
            print("DNI:", reserva["dni_cliente"])
            print("Fecha:", reserva["fecha"])
            print("Horario:", reserva["hora_inicio"], "-", reserva["hora_fin"])
            print("Precio total: $", reserva["precio_total"])

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
        if (cliente["dni"] == reserva["dni_cliente"] and num_cancha == reserva["numero_cancha"] and fecha == reserva["fecha"] and horario_entrada == reserva["hora_inicio"] and reserva["estado"] == "Activa"):
            reserva["estado"] = "Cancelada"
            guardar_reservas(reservas)
            print("Reserva cancelada correctamente.")
            return

    print("No se encontró una reserva con esos datos.")
    
            
def obtener_numeros_sin_reservas(canchas,reservas):
    """
    Calcula qué canchas no tienen reservas activas.
    Retorna:
        Un conjunto con los números de cancha sin reservas.
    """
    todas = {cancha["numero"] for cancha in canchas if cancha["estado"] == "Disponible"}
    reservadas = {reserva["numero_cancha"] for reserva in reservas if reserva["estado"] == "Activa"}
    return todas - reservadas


def filtrar_canchas_por_numero(canchas, numeros):
    """
    Selecciona las canchas cuyo número está en el conjunto recibido.
    Retorna:
        Una lista con los diccionarios de esas canchas, en su orden original.
    """
    return [cancha for cancha in canchas if cancha["numero"] in numeros]


def imprimir_cancha(cancha):
    """Imprime por pantalla la información completa de una cancha."""
    print(f"Cancha N° {cancha['numero']}")
    print(f"  Piso:   {cancha['piso']}")
    print(f"  Techo:  {cancha['techo']}")
    print(f"  Precio: ${cancha['precio']:.2f} por hora")
    print(f"  Estado: {cancha['estado']}")
    print("-------------------------------")


def mostrar_canchas_sin_reservas(lista_canchas, lista_reservas):
    """
    Muestra la información completa de las canchas sin reservas activas.
    No retorna ningún valor.
    """
    numeros = obtener_numeros_sin_reservas(lista_canchas, lista_reservas)
    canchas_libres = filtrar_canchas_por_numero(lista_canchas, numeros)

    if not canchas_libres:
        print("\nTodas las canchas tienen al menos una reserva.")
        return

    print("\n===== Canchas sin reservas =====")
    for cancha in canchas_libres:
        imprimir_cancha(cancha)


    










