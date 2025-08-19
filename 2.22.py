
def planificar_viajes(paquetes):
    viajes = {}
    for destino, precio, dias in paquetes:
      
        total = precio * dias
        viajes[destino] = total
    return viajes


paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

resultado = planificar_viajes(paquetes)

print(resultado)
