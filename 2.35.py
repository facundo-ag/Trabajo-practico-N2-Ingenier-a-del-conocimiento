def optimizar_rutas(rutas, distancias_max):
    rutas_validas = []
    for ruta in rutas:
        origen, destino, distancia = ruta
        for max_d in distancias_max:
            if distancia <= max_d:
                rutas_validas.append(ruta)
                break  
    return rutas_validas

rutas = [
    ("Madrid", "Barcelona", 620),
    ("Madrid", "Valencia", 350),
    ("Barcelona", "Valencia", 350)
]
distancias_max = [600, 400, 500]

resultado = optimizar_rutas(rutas, distancias_max)
print(resultado)
