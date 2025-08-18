
def calcular_goles(resultados):
    goles_anotados = 0
    goles_recibidos = 0
    
    for rival, (anotados, recibidos) in resultados.items():
        goles_anotados += anotados
        goles_recibidos += recibidos
    
    return goles_anotados, goles_recibidos

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

anotados, recibidos = calcular_goles(resultados)

print(f"Total de goles anotados: {anotados}")
print(f"Total de goles recibidos: {recibidos}")
