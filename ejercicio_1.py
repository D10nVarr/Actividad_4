full_name=input("Por favor ingrese su nombre completo: ").lower().split()
dpi_number=int(input("Ingrese su número de dpi: "))
name_department=input("Ingrese su departamento: ").lower()
year_birth=int(input("Ingrese su año de nacimiento: "))

cant_name=len(full_name[0])
cant_dpi=len(str(dpi_number))

if cant_dpi!=13:
    print("Número de DPI incorrecto")

elif year_birth>2007 and name_department !="alta verapaz" or name_department =="petén":
    print("Usted es menor de edad, no puede votar")

elif cant_name<5:
    print("El nombre ingresado no es válido")

else:
    print(f"Bienvenido {full_name}, su centro de votación está en {name_department}")