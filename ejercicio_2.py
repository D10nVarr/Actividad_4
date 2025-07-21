anual_income=int(input("Ingrese su ingreso anual: "))
num_person=int(input("Ingrese el numero de personas: "))

if anual_income<40000 and num_person>2:
    print("Felicidades, usted no paga impuestos")

elif anual_income<=30000 and anual_income>=0:
    taxes=(anual_income*0.05)-1000*num_person
    if taxes>0:
        print(f"Su impuesto a pagar es de Q{taxes} anual")
    else:
        print(f"Su impuesto a pagar es de Q0 anual")

elif anual_income <= 60000 and anual_income >= 30001:
    taxes = (anual_income * 0.1) - 1000 * num_person
    if taxes > 0:
        print(f"Su impuesto a pagar es de Q{taxes} anual")
    else:
        print(f"Su impuesto a pagar es de Q0 anual")

elif anual_income <= 100000 and anual_income >= 600001:
    taxes = (anual_income * 0.15) - 1000 * num_person
    if taxes > 0:
        print(f"Su impuesto a pagar es de Q{taxes} anual")
    else:
        print(f"Su impuesto a pagar es de Q0 anual")

elif anual_income>100000:
    taxes = (anual_income * 0.2) - 1000 * num_person
    if taxes > 0:
        print(f"Su impuesto a pagar es de Q{taxes} anual")
    else:
        print(f"Su impuesto a pagar es de Q0 anual")
