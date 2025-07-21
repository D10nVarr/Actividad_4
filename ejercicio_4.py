num_prices=int(input("Ingrese cantidad de precios que deseee agregar: "))
total_price=0

for i in range(num_prices):

    any_price=int(input(f"Ingrese el precio del producto {i}"))
    total_price+=any_price

print("El total del producto", total_price)

