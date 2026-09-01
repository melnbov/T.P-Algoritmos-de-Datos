administrador = [
    "administrador",
    "42456789",
    "admin123"
]
def iniciar_sesion_admin(administrador):
        dni = input("Ingrese su dni:")
        contraseña = input("ingrese su contraseña:")
        if dni ==administrador[1] and contraseña == administrador[2]:
            print("inicio de sesion exitoso")
            print ("bienvenido", administrador[0])
            return True
        print("el dni y la contraseña son incorrectos")
        return False