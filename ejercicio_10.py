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

gt_day=int(greater_date[0])
gt_month=int(greater_date[1])
gt_year=int(greater_date[2])

ls_day=int(lesser_date[0])
ls_month=int(lesser_date[1])
ls_year=int(lesser_date[2])

days_btwn=0

if year==year_b and month==month_b and day==day_b:
    print("No hay días de diferencia entre ambas")

elif (gt_day != ls_day) and gt_month==ls_month and gt_year==ls_year:
    days_btwn=gt_day-ls_day
    print(f"La diferencia de días es de {days_btwn}")

elif gt_day == ls_day and gt_month!=ls_month and gt_year==ls_year:
    days_btwn= (gt_month-ls_month)*30
    print(f"La diferencia de días es de {days_btwn}")



