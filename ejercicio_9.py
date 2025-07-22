age_person=int(input("Ingrese su edad: "))
week_day=input("Ingrese el día de la semana: ").lower()
student_prs=input("¿Es estudiante? si/no: ")

ticket_price=0
two_one=False

if age_person<13:
    print("Ustede no puede ver películas para mayores de 15 años")

elif student_prs=="si":
    ticket_price=35
else:
    ticket_price=50

if week_day=="miércoles":
    print("Es día 2x1")
    two_one=True

if two_one==True:
    tickets=2
else:
    tickets=1

print("")
print(f"Su total sería de Q{ticket_price} por {tickets} ticket")


