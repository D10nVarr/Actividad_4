date_1=input("Ingrese una fecha en formato dd/mm/yyyy: ")
date_a=date_1.split("/")
date_2=input("Ingrese otra fecha en formato dd/mm/yyyy: ")
date_b=date_2.split("/")

day=int(date_a[0])
month=int(date_a[1])
year=int(date_a[2])

day_b=int(date_b[0])
month_b=int(date_b[1])
year_b=int(date_b[2])

if ((day<0 or day>31) or (month<0 or month>12) or (year<0)) or (day_b<0) or (month_b<0) or (year_b<0):
    print("La fecha no es válida")

#verificación de la fecha mayor
elif year>year_b:
    print(f"La fecha mayor es {date_1}")
elif year<year_b:
    print(f"La fecha mayor es {date_2}")
elif year==year_b:
    if month > month_b:
        print(f"La fecha mayor es {date_1} y esta en el mismo año que {date_2}")
    elif month < month_b:
        print(f"La fecha mayor es {date_2}")
    elif month == month_b:
        if day > day_b:
            print(f"La fecha mayor es {date_1} y esta en el mismo mes y año que {date_2}")
        elif day < day_b:
            print(f"La fecha mayor es {date_2}")
        elif day == day_b:
            print(f"Son la misma fecha")

