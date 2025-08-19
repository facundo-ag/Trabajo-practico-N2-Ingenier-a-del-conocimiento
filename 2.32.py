def simular_ventas(*ventas):
    total_ingresos = 0
    for producto, cantidad, precio in ventas:
        total_ingresos += cantidad * precio
        print(f"{producto}: {cantidad} unidades x {precio} = {cantidad * precio}")
    return total_ingresos

total = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print("Total de ingresos:", total)
