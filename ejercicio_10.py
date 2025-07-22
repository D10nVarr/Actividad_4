date_1=input("Ingrese una fecha en formato dd/mm/yyyy: ")
date_a=date_1.split("/")
date_2=input("Ingrese otra fecha en formato dd/mm/yyyy: ")
date_b=date_1.split("/")

day=int(date_a[0])
month=int(date_a[1])
year=int(date_a[2])

day_b=int(date_b[0])
month_b=int(date_b[1])
year_b=int(date_b[2])


#verificación de la fecha mayor
if year>year_b:
    print("La fecha mayor es date_1")

