inicial_date=input("Ingrese una fecha: ")
any_date=inicial_date.split("/")

day=int(any_date[0])
month=int(any_date[1])
year=int(any_date[2])

century=year//100
year_century=year-(century*100)

if (day<0 or day>31) or (month<0 or month>12) or (year<0):
    print("La fecha no es válida")

elif month==2:
    if year%4==0:
        if day<=29:
            zeller=(day+((13*(month+1))//5)+year_century+(year_century//4)+(century//4)+5*(century))%7

            if zeller==0:
                print(f"La fecha {inicial_date} fue un sábado")
            elif zeller==1:
                print(f"La fecha {inicial_date} fue un domingo")
            elif zeller==2:
                print(f"La fecha {inicial_date} fue un lunes")
            elif zeller==3:
                print(f"La fecha {inicial_date} fue un martes")
            elif zeller==4:
                print(f"La fecha {inicial_date} fue un miércoles")
            elif zeller==5:
                print(f"La fecha {inicial_date} fue un jueves")
            elif zeller==6:
                print(f"La fecha {inicial_date} fue un viernes")
        else:
            print("La fecha no es válida")
    else:
        print("La fecha no es válida")

elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if day<=31:
        zeller=(day+((13*(month+1))//5)+year_century+(year_century//4)+(century//4)+5*(century))%7
        if zeller == 0:
            print(f"La fecha {inicial_date} fue un sábado")
        elif zeller == 1:
            print(f"La fecha {inicial_date} fue un domingo")
        elif zeller == 2:
            print(f"La fecha {inicial_date} fue un lunes")
        elif zeller == 3:
            print(f"La fecha {inicial_date} fue un martes")
        elif zeller == 4:
            print(f"La fecha {inicial_date} fue un miércoles")
        elif zeller == 5:
            print(f"La fecha {inicial_date} fue un jueves")
        elif zeller == 6:
            print(f"La fecha {inicial_date} fue un viernes")
    else:
        print("La fecha no es válida")

elif month==4 or month==6 or month==9 or month==11:
    if day<=30:
        zeller=(day+((13*(month+1))//5)+year_century+(year_century//4)+(century//4)+5*(century))%7
        if zeller == 0:
            print(f"La fecha {inicial_date} fue un sábado")
        elif zeller == 1:
            print(f"La fecha {inicial_date} fue un domingo")
        elif zeller == 2:
            print(f"La fecha {inicial_date} fue un lunes")
        elif zeller == 3:
            print(f"La fecha {inicial_date} fue un martes")
        elif zeller == 4:
            print(f"La fecha {inicial_date} fue un miércoles")
        elif zeller == 5:
            print(f"La fecha {inicial_date} fue un jueves")
        elif zeller == 6:
            print(f"La fecha {inicial_date} fue un viernes")
    else:
        print("La fecha no es válida")