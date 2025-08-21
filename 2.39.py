def simulacion_mercado(precios_diarios, operaciones):
    beneficio = 0
    acciones = 0  
    
    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        
        if operacion == "compra":
            beneficio -= precio
            acciones += 1
        elif operacion == "venta" and acciones > 0:
            beneficio += precio
            acciones -= 1
    
    return beneficio

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

resultado = simulacion_mercado(precios_diarios, operaciones)
print("Beneficio total:", resultado)
