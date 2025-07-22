#En este programa todos los meses tienen 30 días

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

greater_date=0
lesser_date=0

if ((day<0 or day>30) or (month<0 or month>12) or (year<0)) or (day_b<0) or (month_b<0) or (year_b<0):
    print("La fecha no es válida")

#verificación de la fecha mayor
elif year>year_b:
    greater_date=date_a
    lesser_date=date_b
    print(f"La fecha mayor es {date_1}")
elif year<year_b:
    greater_date = date_b
    lesser_date = date_a
    print(f"La fecha mayor es {date_2}")
elif year==year_b:
    if month > month_b:
        greater_date = date_a
        lesser_date = date_b
        print(f"La fecha mayor es {date_1} y esta en el mismo año que {date_2}")
    elif month < month_b:
        greater_date = date_b
        lesser_date = date_a
        print(f"La fecha mayor es {date_2}")
    elif month == month_b:
        if day > day_b:
            greater_date = date_a
            lesser_date = date_b
            print(f"La fecha mayor es {date_1} y esta en el mismo mes y año que {date_2}")
        elif day < day_b:
            greater_date = date_b
            lesser_date = date_a
            print(f"La fecha mayor es {date_2}")
        elif day == day_b:
            print(f"Son la misma fecha")

#verificador de distancias entre fechas

date_1_a=year*365+month*30+day
date_2_b=year_b*365+month_b*30+day_b

days_btwn=0

if greater_date==date_a:
    days_btwn=date_1_a-date_2_b
    print(f"Los días entre {date_1} y {date_2} son {days_btwn}")
elif greater_date==date_b:
    days_btwn=date_2_b-date_1_a
    print(f"Los días entre {date_1} y {date_2} son {days_btwn}")


