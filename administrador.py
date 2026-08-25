administador = [
    "administrador",
    "42456789",
    "admin123"
]
def iniciar_sesion_admin(administrador):
        dni = input("Ingrese su dni:")
        contraseña = input("ingrese su contraseña:")
        if dni ==administador[1] and contraseña == administador[2]:
            print("inicio de sesion exitoso")
            print ("bienvenido", administador[0])
            return True
        print("el dni y la contraseña son incorrectos")
        return False