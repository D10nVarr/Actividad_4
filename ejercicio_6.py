package_weight=int(input("Ingrese en kg el peso del paquete: "))
delivery_distance=float(input("Ingrese en km la distancia de entrega: "))
urgent_package=input("¿El paquete es urgente? si/no: ").lower()
package_size=input("Ingrese el tamaño del paquete (pequeño/mediano/grande): ").lower()

urgency_surcharge=0
size_surcharge=0
discount=0
weight_price=0
delivery_price=0

if urgent_package == "si":
    urgency_surcharge=50
elif urgent_package == "no":
    urgency_surcharge=0

if package_size=="grande":
    size_surcharge=30
else:
    size_surcharge=0

if urgent_package == "no" and package_weight<5:
    discount=-20
else:
    discount=0

if package_weight<=10:
    weight_price=10
elif package_weight>10:
    weight_price=5*(package_weight-10)+10

if delivery_distance<=5:
    delivery_price=20
elif delivery_distance>5:
    delivery_price = 10 * (delivery_distance-5) + 20


print("")
print("El precio de la entrega es el siguiente:")
print(f"El peso de {package_weight}kg tiene un costo de Q{weight_price}")
print(f"El transporte de una distancia de {delivery_distance}km tiene un costo de Q{delivery_price}")
print(f"El recargo por urgencia tiene un costo de Q{urgency_surcharge}")
print(f"El recargo por tamaño tiene un costo de Q{size_surcharge}")
print(f"Descuento aplicable Q{discount}")

print("-------------------------------------")

print("El precio total de la entrega es de Q",urgency_surcharge+size_surcharge+discount+weight_price+delivery_price)
