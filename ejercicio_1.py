full_name=input("Por favor ingrese su nombre completo: ").lower()
dpi_number=int(input("Ingrese su número de dpi: "))
name_department=input("Ingrese su departamento: ").lower()
year_birth=int(input("Ingrese su año de nacimiento"))

if len(dpi_number)<13 or len(dpi_number)>13:
    print("Número de DPI incorrecto")

elif year_birth>2007 and name_department !="alta verapaz" or name_department =="petén":
    print("Usted es menor de edad, no puede votar")
