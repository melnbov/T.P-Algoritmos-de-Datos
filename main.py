import clientes
import administrador
import canchas
import reservas

def menu_cliente(cliente_actual, lista_clientes, lista_canchas, lista_reservas):
    """ 
    Muestra el menú de opciones disponibles para un cliente.

    Parámetros:
    cliente_actual: datos del cliente que inició sesión.
    lista_clientes: matriz que contiene los clientes registrados.
    lista_canchas: matriz que contiene las canchas registradas.
    lista_reservas: matriz que contiene las reservas registradas.
    """
    #dias para alquilar la cancha
    dias=[ 
        "28/08/2026",
        "29/08/2026",
        "30/08/2026",
        "31/08/2026",
        "01/09/2026",
        "02/09/2026",
        "03/09/2026"
    ]
    opcion=0
    while opcion!=5:
        print("Menú Cliente")
        print("1. Consultar canchas")
        print("2. Realizar una reserva")
        print("3. Consultar mis reservas")
        print("4. Cancelar una reserva")
        print("5. Cerrar sesión")
        
        opcion=int(input("Ingrese una opcion: "))
        
        if opcion== 1: 
            canchas.mostrar_canchas(lista_canchas)
        elif opcion==2:
            reservas.crear_reserva(lista_canchas, lista_reservas, dias, cliente_actual)
        elif opcion==3:
            reservas.mostrar_reserva(lista_reservas)
        elif opcion==4:
            reservas.cancelar_reserva(lista_reservas, cliente_actual)
        elif opcion==5:
            print("Sesión cerrada")
        else:
            print("Opción invalida")
    
def menu_administrador(datos_administrador, lista_clientes, lista_canchas, lista_reservas):
    """
    Muestra el menú de opciones disponibles para el administrador.

    Parámetros:
    datos_administrador: datos del administrador.
    lista_clientes: matriz que contiene los clientes.
    lista_canchas: matriz que contiene las canchas.
    lista_reservas: matriz que contiene las reservas.
    """
        
    opcion=0
    while opcion !=9:
        print("Menpu Administrador")
        print("1. Registrar cancha")
        print("2. Consultar canchas")
        print("3. Modificar cancha")
        print("4. Eliminar cancha")
        print("5. Consultar todas las reservas")
        print("6. Buscar reservas por cliente")
        print("7. Buscar reservas por cancha")
        print("8. Generar reporte")
        print("9. Cerrar sesión")
            
        opcion=int(input("Ingrese una opción: "))
        if opcion == 1:
            canchas.registrar_cancha(lista_canchas)
        elif opcion == 2:
            canchas.mostrar_canchas(lista_canchas)
        elif opcion == 3:
            canchas.modificar_cancha(lista_canchas)
        elif opcion == 4: 
            canchas.eliminar_cancha(lista_canchas)
        elif opcion == 5: 
            administrador.mostrar_todas_reservas(lista_reservas, lista_clientes)
        elif opcion == 6:
            administrador.buscar_reservas_clientes(lista_reservas, lista_clientes)
        elif opcion == 7:
            administrador.buscar_reservas_cancha(lista_reservas, lista_canchas)
        elif opcion == 8:
           administrador.generar_reporte(lista_reservas, lista_clientes, lista_canchas)
        elif opcion == 9:
            print("Sesión cerrada")
        else:
            print("Opción inválida")
                
def main():
    """
    Ejecuta el programa principal y permite acceder al sistema
    como cliente o como administrador.
    """
    #matriz de clientes
    lista_clientes=[]
    
    #matriz de canchas
    lista_canchas=[]
    
    #matriz de reservas
    lista_reservas=[]
    
    #datos del admin
    datos_administrador=[
        "Administrador",
        "42456789",
        "admin123"
    ]
    
    opcion=0
    
    while opcion !=3:
        print("Sistema de alquiler de canchas de padel")
        print("1. Ingresar como cliente")
        print("2. Ingresar como administrador")
        print("3. Salir")
        
        opcion=int(input("Ingrese una opcion: "))
        
        if opcion == 1: 
            opcion_cliente=0
            while opcion_cliente!=3:
                print("Cliente")
                print("1. Registrarse")
                print("2. Iniciar sesión")
                print("3. Volver")
                
                opcion_cliente= int(input("Ingrese una opción: "))
                
                if opcion_cliente == 1:
                    clientes.registrar_clientes(lista_clientes)
                if opcion_cliente == 2:
                    cliente_actual=clientes.iniciar_sesion_cliente(lista_clientes)
                    if cliente_actual is not None: 
                        menu_cliente(cliente_actual, lista_clientes, lista_canchas, lista_reservas)
                elif opcion_cliente == 3:
                    print("Volviendo al menú principal....")
                else:
                    print("Opción inválida")
                    
        elif opcion == 2: 
            acceso_correcto=administrador.iniciar_sesion_admin(datos_administrador)
            
            if acceso_correcto:
                menu_administrador(datos_administrador, lista_clientes, lista_canchas, lista_reservas)
        
        elif opcion == 3:
            print("¡¡Gracias por utilizar nuestro sistema!!")
        else:
            print("Opcion inválida")
            
main()