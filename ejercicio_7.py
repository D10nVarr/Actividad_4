students_name=[]
students_notes=[]

for i in range(5):
    name=input(f"Ingrese el nombre del estudiante {i+1}: ")
    note_1=int(input(f"Ingrese el nota 1: "))
    note_2 = int(input(f"Ingrese el nota 2: "))
    note_3 = int(input(f"Ingrese el nota 3: "))

    students_name.append(name)
    students_notes.append(note_1)
    students_notes.append(note_2)
    students_notes.append(note_3)

average_1=(students_notes[0]+students_notes[1]+students_notes[2])/3
average_2=(students_notes[3]+students_notes[4]+students_notes[5])/3
average_3=(students_notes[6]+students_notes[7]+students_notes[8])/3
average_4=(students_notes[9]+students_notes[10]+students_notes[11])/3
average_5=(students_notes[12]+students_notes[13]+students_notes[14])/3

if average_1<70 and average_2<70 and average_3<70 and average_4<70 and average_5<70:
    print("Los estudiantes aplican a curva")

    for i in range(15):
        if (students_notes[i])<=95:
            students_notes[i]+=5
        elif (students_notes[i])>95:
            students_notes[i]=100

    new_average_1=(students_notes[0]+students_notes[1]+students_notes[2])/3
    new_average_2=(students_notes[3]+students_notes[4]+students_notes[5])/3
    new_average_3=(students_notes[6]+students_notes[7]+students_notes[8])/3
    new_average_4=(students_notes[9]+students_notes[10]+students_notes[11])/3
    new_average_5=(students_notes[12]+students_notes[13]+students_notes[14])/3

    total_average=[new_average_1,new_average_2,new_average_3,new_average_4,new_average_5]

    for i in range(5):
        print(f"Nombre del estudiante {students_name[i]}        Promedio: {total_average[i]}")

else:
    total_average = [average_1, average_2, average_3, average_4, average_5]
    for i in range(5):
        print(f"Nombre del estudiante {students_name[i]}        Promedio: {total_average[i]}")




