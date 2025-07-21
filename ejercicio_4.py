num_prices=int(input("Ingrese cantidad de precios que deseee agregar: "))
sub_price=0

for i in range(num_prices):

    any_price=int(input(f"Ingrese el precio del producto {i+1}: "))
    sub_price+=any_price

amount_tip=input("Desea dejar popina, escoja: si o no: ").lower()
if amount_tip=="si":
    amount_tip=int(input("Ingrese el porcentaje que desee: "))
    amount_tip = amount_tip/100
elif amount_tip=="no":
    amount_tip=0

client_member=input("Posee tarjeta de cliente frecuente, escoja: si o no: ").lower()
if client_member=="si":
    client_member=0.1
elif client_member=="no":
    client_member=0

iva_tax=sub_price*(0.12)
tip=sub_price*amount_tip
discount=sub_price*client_member

total_price=sub_price+iva_tax+tip-discount

print("Su factura dettallada es:")
print("Subtotal   ", sub_price)
print("+ IVA      ", iva_tax)
print("+ Propina  ", tip)
print("- Descuento", discount)
print("-------------------------------------")
print("TOTAL:     ", total_price)







