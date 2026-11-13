from datetime import date

import clientes
import canchas
import reservas
import administrador


def mostrar_resultado(numero, tipo, funcion, datos, esperado, obtenido):
    """Compara el resultado esperado con el obtenido e imprime el detalle."""
    if obtenido == esperado:
        estado = "APROBADA"
    else:
        estado = "NO APROBADA"

    print("Prueba", numero, "-", tipo)
    print("  Función:", funcion)
    print("  Datos:", datos)
    print("  Resultado esperado:", esperado)
    print("  Resultado obtenido:", obtenido)
    print("  Estado:", estado)
    print("--------------------------------------------")

    return obtenido == esperado


# ======================= CASOS VÁLIDOS (4) =======================

def prueba_1_validar_dni_valido():
    """
    Comprueba que la función validar_dni acepte un DNI válido.
    """
    obtenido = clientes.validar_dni("42456789")
    return mostrar_resultado(1, "Caso válido", "clientes.validar_dni",
                             "dni = '42456789'", True, obtenido)


def prueba_2_calcular_precio_valido():
    """
    Comprueba que se calcule correctamente el precio de una reserva de 3 horas.
    """
    # 3 horas (de 18 a 21) a $12000 la hora
    obtenido = reservas.calcular_precio(18, 21, 12000)
    return mostrar_resultado(2, "Caso válido", "reservas.calcular_precio",
                             "entrada = 18, salida = 21, precio_hora = 12000",
                             36000, obtenido)


def prueba_3_calcular_recaudacion_valida():
    """
    Comprueba que se calcule correctamente la recaudación de varias reservas activas.
    """
    lista_reservas = [
        {"numero_cancha": 1, "precio_total": 10000, "estado": "Activa"},
        {"numero_cancha": 2, "precio_total": 15000, "estado": "Activa"},
        {"numero_cancha": 1, "precio_total": 5000, "estado": "Activa"},
    ]
    obtenido = administrador.calcular_recaudacion(lista_reservas)
    return mostrar_resultado(3, "Caso válido", "administrador.calcular_recaudacion",
                             "3 reservas con precios 10000, 15000 y 5000",
                             30000, obtenido)


def prueba_4_obtener_canchas_disponibles_valido():
    """
    Comprueba que se obtengan solamente las canchas que están disponibles.
    """
    lista_canchas = [
        {"numero": 1, "piso": "Cemento", "techo": "Techada", "precio": 8000, "estado": "Disponible"},
        {"numero": 2, "piso": "Resina", "techo": "No techada", "precio": 9000, "estado": "No disponible"},
        {"numero": 3, "piso": "Cesped sintetico", "techo": "Techada", "precio": 10000, "estado": "Disponible"},
    ]
    obtenido = []
    for cancha in canchas.obtener_canchas_disponibles(lista_canchas):
        obtenido.append(cancha["numero"])
    return mostrar_resultado(4, "Caso válido", "canchas.obtener_canchas_disponibles",
                             "3 canchas: la 1 y la 3 disponibles, la 2 no disponible",
                             [1, 3], obtenido)


# ======================= CASOS INVÁLIDOS (3) =======================

def prueba_5_validar_telefono_invalido():
    """
    Comprueba que la función validar_telefono rechace un teléfono que contiene letras.
    """
    obtenido = clientes.validar_telefono("11ABC456")
    return mostrar_resultado(5, "Caso inválido", "clientes.validar_telefono",
                             "telefono = '11ABC456' (contiene letras)", False, obtenido)


def prueba_6_validar_contrasenia_invalida():
    """
    Comprueba que la función validar_contraseña rechace una contraseña de menos de 6 caracteres.
    """
    obtenido = clientes.validar_contraseña("abc")
    return mostrar_resultado(6, "Caso inválido", "clientes.validar_contraseña",
                             "contraseña = 'abc' (menos de 6 caracteres)", False, obtenido)


def prueba_7_horario_superpuesto_invalido():
    """
    Comprueba que no se permita realizar una reserva en un horario que ya está ocupado.
    """
    reservas_existentes = [
        {"numero_cancha": 1, "fecha": "2026-11-10", "hora_inicio": 18,
         "hora_fin": 20, "estado": "Activa"}
    ]
    # Se intenta reservar de 19 a 21, que pisa la reserva de 18 a 20
    obtenido = reservas.verificar_horario_reserva(reservas_existentes, 1,
                                                  date(2026, 11, 10), 19, 21)
    return mostrar_resultado(7, "Caso inválido", "reservas.verificar_horario_reserva",
                             "cancha 1, 2026-11-10, de 19 a 21 (ya reservada de 18 a 20)",
                             False, obtenido)


# ======================= CASOS LÍMITE (2) =======================

def prueba_8_nombre_con_minimo_de_caracteres():
    """
    Comprueba que se acepte un nombre que tiene exactamente 3 caracteres.
    """
    # El mínimo permitido es 3 caracteres
    obtenido = clientes.validar_nombre("Ana")
    return mostrar_resultado(8, "Caso límite", "clientes.validar_nombre",
                             "nombre = 'Ana' (justo 3 caracteres)", True, obtenido)


def prueba_9_horario_consecutivo_sin_superposicion():
    """
    Comprueba que se permita reservar cuando el horario comienza justo al finalizar otra reserva.
    """
    reservas_existentes = [
        {"numero_cancha": 1, "fecha": "2026-11-10", "hora_inicio": 18,
         "hora_fin": 20, "estado": "Activa"}
    ]
    # Empieza justo cuando termina la otra reserva (20), no se pisan
    obtenido = reservas.verificar_horario_reserva(reservas_existentes, 1,
                                                  date(2026, 11, 10), 20, 22)
    return mostrar_resultado(9, "Caso límite", "reservas.verificar_horario_reserva",
                             "cancha 1, 2026-11-10, de 20 a 22 (la otra termina a las 20)",
                             True, obtenido)


# ======================= PRUEBA ADICIONAL (1) =======================
# Problemática del sistema: el administrador aumenta los precios de las canchas.

def prueba_10_aumentar_precios():
    """
    Comprueba que se aumenten correctamente los precios de las canchas según el porcentaje indicado.
    """
    lista_canchas = [
        {"numero": 1, "piso": "Cemento", "techo": "Techada", "precio": 10000, "estado": "Disponible"},
        {"numero": 2, "piso": "Resina", "techo": "No techada", "precio": 20000, "estado": "Disponible"},
    ]

    # aumentar_precios guarda en canchas.json: lo reemplazo por una función
    # vacía para que la prueba no modifique el archivo real del sistema.
    guardar_original = canchas.guardar_canchas
    canchas.guardar_canchas = lambda lista: None

    nuevas = canchas.aumentar_precios(lista_canchas, 10)

    canchas.guardar_canchas = guardar_original

    obtenido = []
    for cancha in nuevas:
        obtenido.append(round(cancha["precio"], 2))

    return mostrar_resultado(10, "Prueba adicional", "canchas.aumentar_precios",
                             "precios 10000 y 20000, aumento del 10%",
                             [11000.0, 22000.0], obtenido)


# ======================= EJECUCIÓN =======================

def ejecutar_pruebas():
    """
    Ejecuta todas las pruebas unitarias y muestra la cantidad de pruebas aprobadas.
    """
    print("======== PRUEBAS UNITARIAS ========\n")

    resultados = [
        prueba_1_validar_dni_valido(),
        prueba_2_calcular_precio_valido(),
        prueba_3_calcular_recaudacion_valida(),
        prueba_4_obtener_canchas_disponibles_valido(),
        prueba_5_validar_telefono_invalido(),
        prueba_6_validar_contrasenia_invalida(),
        prueba_7_horario_superpuesto_invalido(),
        prueba_8_nombre_con_minimo_de_caracteres(),
        prueba_9_horario_consecutivo_sin_superposicion(),
        prueba_10_aumentar_precios(),
    ]

    aprobadas = resultados.count(True)
    print("Pruebas aprobadas:", aprobadas, "de", len(resultados))


ejecutar_pruebas()
