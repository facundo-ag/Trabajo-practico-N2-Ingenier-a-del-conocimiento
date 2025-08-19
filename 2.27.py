def estadisticas_ventas(ventas):
    total = sum(ventas) 
    promedio = total / len(ventas) 
    max_venta = max(ventas)  
    mes_max = ventas.index(max_venta) + 1  
    
    return {
        "total_ventas": total,
        "promedio_mensual": promedio,
        "mes_mayores_ventas": mes_max,
        "valor_mayor_venta": max_venta
    }

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
resultado = estadisticas_ventas(ventas_mensuales)
print(resultado)
