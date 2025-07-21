num_prices=int(input("Ingrese cantidad de precios que deseee agregar: "))
total_price=0

for i in range(num_prices):

    any_price=int(input(f"Ingrese el precio del producto {i+1}: "))
    total_price+=any_price

amount_tip=input("Desea dejar popina, escoja: si o no: ").lower()
if amount_tip=="si":
    amount_tip=int(input("Ingrese el porcentaje que desee: "))
    amount_tip = amount_tip/100
elif amount_tip=="no":
    amount_tip=0

client_tarjet=input("Posee tarjeta de cliente frecuente, escoja: si o no: ").lower()
if client_tarjet=="si":
    client_tarjet=0.1
elif client_tarjet=="no":
    client_tarjet=0



