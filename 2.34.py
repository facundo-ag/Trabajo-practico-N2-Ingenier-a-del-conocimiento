def analizar_encuestas(encuestas):
    resultados = {}
    for pregunta, respuestas in encuestas.items():
        frecuencia = {}
        for r in respuestas:
            frecuencia[r] = frecuencia.get(r, 0) + 1
        resultados[pregunta] = frecuencia
    return resultados
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultados = analizar_encuestas(encuestas)
print(resultados)
