NAME_USER_1="Juan21"
PASS_USER_1="1234"

NAME_USER_2="ManuXD"
PASS_USER_2="bu1u"

NAME_USER_3="Chad01"
PASS_USER_3="1111"

num_try=3

while True:

    name_user=input("Ingrese su nombre de usuario: ")
    pass_user=input("Ingrese la contraseña de ese usuario: ")

    if (name_user==NAME_USER_1 and pass_user==PASS_USER_1) or (name_user==NAME_USER_2 and pass_user==PASS_USER_2) or (name_user==NAME_USER_3 and pass_user==PASS_USER_3):
        print(f"Bienvenido de nuevo {name_user} que acción desea realizar: ")
        print("1. Ver perfil")
        print("2. Cambiar contraseña")
        print("3. Cerrar Sesión")
        break

    else:
        print(f"El usuario o la contraseña no coinciden le quedan {num_try} intentos")

    if num_try == 0:
        print("ACCESO DENEGADO")
        break
    num_try-=1












