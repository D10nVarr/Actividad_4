any_date=input("Ingrese una fecha: ").split("/")

if (any_date[0]<0 or any_date[0]>31) or (any_date[1]<0 or any_date[1]>12) or (any_date[2]<0):
    print("La fecha no es válida")

elif any_date[1]==2:
    if any_date[2]%4==0:
        if any_date[0]<=29:
            print("Fecha válida")
    else:
        print("La fecha no es válida")