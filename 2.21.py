
def ordenar_puntuaciones(puntuaciones):
    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
resultado = ordenar_puntuaciones(puntuaciones)
print(resultado)
